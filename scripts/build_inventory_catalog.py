"""
7 Days to Die — Inventory Object Catalog
=========================================

Parses items.xml, blocks.xml, and item_modifiers.xml to build
a complete HTML catalog of all inventory-compatible game objects,
with icons, internal names, English and Russian display names,
and Russian descriptions.

Usage
-----
    .venv/Scripts/python.exe scripts/build_inventory_catalog.py

Output
------
    build/inventory_catalog.html — searchable, filterable catalog.
"""

import os
import csv
from lxml import etree

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
CONFIG_DIR = os.path.join(ROOT_DIR, "Data", "Config")
BUILD_DIR = os.path.join(ROOT_DIR, "build")
ICONS_DIR = os.path.join(ROOT_DIR, "Data", "ItemIcons")

ITEMS_XML = os.path.join(CONFIG_DIR, "items.xml")
BLOCKS_XML = os.path.join(CONFIG_DIR, "blocks.xml")
ITEM_MODIFIERS_XML = os.path.join(CONFIG_DIR, "item_modifiers.xml")
LOCALIZATION_TXT = os.path.join(CONFIG_DIR, "Localization.txt")
OUTPUT_HTML = os.path.join(BUILD_DIR, "inventory_catalog.html")


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

SOURCES = [
    (ITEMS_XML, "item", "Items"),
    (BLOCKS_XML, "block", "Blocks"),
    (ITEM_MODIFIERS_XML, "item_modifier", "Item Modifiers"),
]


def parse_objects(xml_path: str, tag: str, source_label: str) -> list[dict]:
    """Parse all objects from an XML file, resolving CustomIcon via Extends."""
    tree = etree.parse(xml_path)
    root = tree.getroot()

    # First pass: index all elements by name for Extends resolution
    elements_by_name: dict[str, etree._Element] = {}
    for elem in root.iter(tag):
        name = elem.get("name")
        if name:
            elements_by_name[name] = elem

    objects = []
    for elem in root.iter(tag):
        name = elem.get("name")
        if not name:
            continue

        # Direct properties
        props = {}
        for prop in elem.findall("property"):
            pname = prop.get("name")
            if pname:
                props[pname] = prop.get("value", "")

        # Resolve icon: CustomIcon > own name
        custom_icon = props.get("CustomIcon")
        custom_icon_tint = props.get("CustomIconTint")
        creative_mode = props.get("CreativeMode", "")
        group = props.get("Group", "")

        # If no CustomIcon, check inheritance via Extends
        if custom_icon is None:
            extends_val = props.get("Extends")
            if extends_val:
                # param1 lists properties EXCLUDED from inheritance
                extends_prop = elem.find("property[@name='Extends']")
                excluded = ""
                if extends_prop is not None:
                    excluded = extends_prop.get("param1", "")
                excluded_set = {e.strip() for e in excluded.split(",") if e.strip()}

                if "CustomIcon" not in excluded_set:
                    # Walk the Extends chain
                    custom_icon = _resolve_inherited_icon(
                        extends_val, elements_by_name
                    )

        # Determine the actual icon filename (without .png)
        icon_name = custom_icon if custom_icon else name

        objects.append({
            "name": name,
            "source": source_label,
            "tag": tag,
            "icon_name": icon_name,
            "custom_icon_tint": custom_icon_tint,
            "creative_mode": creative_mode,
            "group": group,
        })

    return objects


def _resolve_inherited_icon(
    parent_name: str, elements_by_name: dict, depth: int = 0
) -> str | None:
    """Walk Extends chain to find a CustomIcon, up to 10 levels deep."""
    if depth > 10:
        return None
    parent = elements_by_name.get(parent_name)
    if parent is None:
        return None

    for prop in parent.findall("property"):
        if prop.get("name") == "CustomIcon":
            return prop.get("value", "")

    # Check if parent itself extends something
    extends_prop = parent.find("property[@name='Extends']")
    if extends_prop is not None:
        grandparent = extends_prop.get("value", "")
        excluded = extends_prop.get("param1", "")
        excluded_set = {e.strip() for e in excluded.split(",") if e.strip()}
        if grandparent and "CustomIcon" not in excluded_set:
            return _resolve_inherited_icon(grandparent, elements_by_name, depth + 1)

    return None


def parse_localization(txt_path: str) -> dict:
    """Parse Localization.txt into {key: {english, russian}} dict."""
    loc: dict = {}
    with open(txt_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        header_lower = [h.strip().lower() for h in header]
        key_idx = 0
        en_idx = header_lower.index("english") if "english" in header_lower else None
        ru_idx = header_lower.index("russian") if "russian" in header_lower else None
        for row in reader:
            if not row:
                continue
            key = row[key_idx].strip()
            en = row[en_idx].strip() if en_idx is not None and en_idx < len(row) else ""
            ru = row[ru_idx].strip() if ru_idx is not None and ru_idx < len(row) else ""
            loc[key] = {"english": en, "russian": ru}
    return loc


def load_icon_index(icons_dir: str) -> set[str]:
    """Return set of icon names (without extension) available in ItemIcons."""
    icons = set()
    if os.path.isdir(icons_dir):
        for fname in os.listdir(icons_dir):
            if fname.lower().endswith(".png"):
                icons.add(fname[:-4])  # strip .png
    return icons


def icon_relative_path(icon_name: str) -> str:
    """Return relative path from the build/ dir to the icon PNG."""
    return f"../Data/ItemIcons/{icon_name}.png"


# ---------------------------------------------------------------------------
# HTML report
# ---------------------------------------------------------------------------

def _esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


CREATIVE_COLORS = {
    "": "#aaa",
    "Player": "#4CAF50",
    "Dev": "#ff9800",
    "Test": "#9C27B0",
    "None": "#666",
    "Console": "#2196F3",
}


def render_html(
    all_objects: dict[str, list[dict]],
    localization: dict,
    icon_index: set[str],
    output_path: str,
):

    # Count totals
    grand_total = sum(len(objs) for objs in all_objects.values())

    lines: list[str] = []
    lines.append("<!DOCTYPE html>")
    lines.append('<html lang="en"><head><meta charset="UTF-8">')
    lines.append("<title>7D2D Inventory Object Catalog</title>")
    lines.append("<style>")
    lines.append(_CSS)
    lines.append("</style></head><body>")

    lines.append("<h1>7D2D — Inventory Object Catalog</h1>")
    lines.append(f'<div class="summary">')
    lines.append(f"  Total objects: <b>{grand_total}</b>")
    for label, objects in all_objects.items():
        lines.append(f"  &nbsp;|&nbsp; {_esc(label)}: <b>{len(objects)}</b>")
    lines.append("</div>")

    # Global controls
    lines.append('<div class="controls">')
    lines.append('  <input class="search-box" type="text" id="searchBox" '
                 'placeholder="Search by name or ID…" oninput="filterAll()">')
    lines.append('  <select id="creativeModeFilter" onchange="filterAll()">')
    lines.append('    <option value="all">All CreativeModes</option>')
    for cm in ["", "Player", "Dev", "Test", "None", "Console"]:
        label = cm if cm else "(default)"
        lines.append(f'    <option value="{_esc(cm)}">{_esc(label)}</option>')
    lines.append("  </select>")
    lines.append("</div>")

    # One table per source
    for label, objects in all_objects.items():
        anchor = label.replace(" ", "_").lower()
        lines.append(f'<h2 id="{anchor}">{_esc(label)} ({len(objects)})</h2>')
        lines.append(f'<table class="catalog" data-section="{_esc(anchor)}">')
        lines.append("<thead><tr>")
        lines.append("  <th>Icon</th>")
        lines.append('  <th class="sortable" onclick="sortSection(this, 1)">Name (ID)</th>')
        lines.append('  <th class="sortable" onclick="sortSection(this, 2)">English</th>')
        lines.append('  <th class="sortable" onclick="sortSection(this, 3)">Russian</th>')
        lines.append("  <th>Description (RU)</th>")
        lines.append('  <th class="sortable" onclick="sortSection(this, 5)">Creative</th>')
        lines.append("</tr></thead><tbody>")

        for obj in objects:
            name = obj["name"]
            icon_name = obj["icon_name"]
            tint = obj.get("custom_icon_tint")
            creative = obj["creative_mode"]

            loc_name = localization.get(name, {})
            en_name = loc_name.get("english", "")
            ru_name = loc_name.get("russian", "")

            loc_desc = localization.get(name + "Desc", {})
            ru_desc = loc_desc.get("russian", "")

            # Icon HTML
            if icon_name in icon_index:
                src = _esc(icon_relative_path(icon_name))
                tint_style = ""
                if tint:
                    tint_style = f' style="filter: drop-shadow(0 0 0 #{_esc(tint)}); opacity: 0.95;"'
                icon_html = (
                    f'<img src="{src}" width="48" height="48" '
                    f'loading="lazy" alt="{_esc(icon_name)}"{tint_style}>'
                )
            else:
                icon_html = '<span class="no-icon">—</span>'

            # CreativeMode badge
            cm_color = CREATIVE_COLORS.get(creative, "#aaa")
            cm_label = creative if creative else "default"
            cm_html = f'<span class="cm-badge" style="color:{cm_color}">{_esc(cm_label)}</span>'

            search_text = f"{name.lower()} {en_name.lower()} {ru_name.lower()}"
            lines.append(
                f'<tr data-search="{_esc(search_text)}" data-cm="{_esc(creative)}">'
            )
            lines.append(f"  <td class=\"icon-cell\">{icon_html}</td>")
            lines.append(f"  <td class=\"name-cell\"><code>{_esc(name)}</code></td>")
            lines.append(f"  <td>{_esc(en_name)}</td>")
            lines.append(f"  <td>{_esc(ru_name)}</td>")
            lines.append(f"  <td class=\"desc-cell\">{_esc(ru_desc)}</td>")
            lines.append(f"  <td>{cm_html}</td>")
            lines.append("</tr>")

        lines.append("</tbody></table>")

    lines.append(_JS)
    lines.append("</body></html>")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\n  Report saved → {output_path}")


# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
_CSS = """
body {
    background: #1a1a2e; color: #e0e0e0;
    font-family: 'Segoe UI', Consolas, monospace;
    margin: 0; padding: 20px;
}
h1 { color: #fff; margin-bottom: 5px; }
h2 {
    color: #ccc; margin-top: 30px; padding-bottom: 6px;
    border-bottom: 1px solid #333;
}
.summary { color: #aaa; margin-bottom: 15px; font-size: 14px; }
.controls {
    display: flex; gap: 10px; margin-bottom: 15px;
    flex-wrap: wrap; align-items: center;
}
.search-box {
    background: #2a2a4a; color: #e0e0e0; border: 1px solid #444;
    padding: 6px 12px; border-radius: 4px; font-size: 13px; width: 350px;
}
select {
    background: #2a2a4a; color: #e0e0e0; border: 1px solid #444;
    padding: 6px 12px; border-radius: 4px; font-size: 13px;
}
table.catalog { border-collapse: collapse; width: 100%; font-size: 13px; margin-bottom: 20px; }
table.catalog th {
    background: #16213e; padding: 8px 10px; text-align: left;
    border-bottom: 2px solid #444; position: sticky; top: 0; z-index: 1;
}
th.sortable { cursor: pointer; }
th.sortable:hover { background: #1a2a50; }
table.catalog td {
    padding: 4px 10px; border-bottom: 1px solid #2a2a4a;
    vertical-align: middle;
}
table.catalog tr:hover { background: rgba(255,255,255,0.04); }
td.icon-cell { width: 56px; text-align: center; }
td.icon-cell img { display: block; margin: auto; image-rendering: pixelated; }
td.name-cell code {
    background: #2a2a4a; padding: 2px 6px; border-radius: 3px;
    font-size: 12px; word-break: break-all;
}
td.desc-cell {
    max-width: 400px; font-size: 12px; color: #bbb;
    overflow: hidden; text-overflow: ellipsis;
}
.no-icon { color: #555; font-size: 20px; }
.cm-badge { font-size: 11px; font-weight: bold; }
.hidden { display: none; }
"""

# ---------------------------------------------------------------------------
# JavaScript
# ---------------------------------------------------------------------------
_JS = """
<script>
function filterAll() {
    const q = document.getElementById('searchBox').value.toLowerCase();
    const cm = document.getElementById('creativeModeFilter').value;
    document.querySelectorAll('table.catalog tbody tr').forEach(row => {
        const matchSearch = !q || row.dataset.search.includes(q);
        const matchCm = cm === 'all' || row.dataset.cm === cm;
        row.style.display = (matchSearch && matchCm) ? '' : 'none';
    });
}

function sortSection(th, colIdx) {
    const table = th.closest('table');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.rows);
    const asc = th.dataset.asc !== '1';
    th.dataset.asc = asc ? '1' : '0';
    rows.sort((a, b) => {
        const av = a.cells[colIdx].textContent.trim().toLowerCase();
        const bv = b.cells[colIdx].textContent.trim().toLowerCase();
        return asc ? av.localeCompare(bv) : bv.localeCompare(av);
    });
    rows.forEach(r => tbody.appendChild(r));
}
</script>
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("7D2D Inventory Object Catalog")
    print("=" * 60)

    print("\n[1/4] Loading objects …")
    all_objects: dict[str, list[dict]] = {}
    total = 0
    for xml_path, tag, label in SOURCES:
        if not os.path.isfile(xml_path):
            print(f"  SKIP {xml_path} (not found)")
            continue
        objects = parse_objects(xml_path, tag, label)
        print(f"  {os.path.basename(xml_path)} → {len(objects)} objects")
        all_objects[label] = objects
        total += len(objects)
    print(f"  Total: {total}")

    print("\n[2/4] Parsing localization …")
    localization = parse_localization(LOCALIZATION_TXT)
    print(f"  Keys loaded: {len(localization)}")

    print("\n[3/4] Indexing icons …")
    icon_index = load_icon_index(ICONS_DIR)
    print(f"  Icon files found: {len(icon_index)}")

    # Stats: how many objects have matching icons?
    found = 0
    missing = 0
    for objects in all_objects.values():
        for obj in objects:
            if obj["icon_name"] in icon_index:
                found += 1
            else:
                missing += 1
    print(f"  Objects with icon: {found}, without: {missing}")

    print("\n[4/4] Generating HTML report …")
    render_html(all_objects, localization, icon_index, OUTPUT_HTML)

    print(f"\nDone! → {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
