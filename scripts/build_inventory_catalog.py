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
    build/inventory_catalog.html  — searchable, filterable catalog.
    build/inventory_catalog/      — processed icons (resized, tinted).
"""

import os
import csv
import shutil
from PIL import Image
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

# ---------------------------------------------------------------------------
# Item sub-categories (matches Major Item Categories from modding_guide.md)
# ---------------------------------------------------------------------------

# Order matters — first match wins.
_ITEM_CATEGORY_RULES: list[tuple[str, callable]] = [
    ("Ranged Weapons",      lambda o: _grp(o, "Ranged Weapons") or
                            (o["name"].startswith("gun") and not o["name"].startswith("gunBot"))),
    ("Melee Weapons",       lambda o: _grp(o, "Melee Weapons") or
                            o["name"].startswith("meleeWpn") or
                            o["name"].startswith("meleeHand")),
    ("Tools",               lambda o: _grp(o, "Tools/Traps") or
                            o["name"].startswith("meleeTool")),
    ("Robotic Companions",  lambda o: _grp(o, "Robotics") or
                            o["name"].startswith("gunBot")),
    ("Ammunition",          lambda o: _grp(o, "Ammo") or
                            o["name"].startswith("ammo")),
    ("Food & Drinks",       lambda o: _grp(o, "Food/Cooking") or
                            _grp(o, "Drink") or
                            o["name"].startswith("food") or
                            o["name"].startswith("drink")),
    ("Medicine & Science",  lambda o: _grp(o, "Medical") or
                            _grp(o, "Science") or
                            o["name"].startswith("medical") or
                            o["name"].startswith("drug")),
    ("Clothing & Armor",    lambda o: _grp(o, "Armor") or
                            _grp(o, "Clothing") or
                            o["name"].startswith("armor") or
                            o["name"].startswith("clothing") or
                            o["name"].startswith("apparel")),
    ("Resources & Materials", lambda o: _grp(o, "Resources") or
                            _grp(o, "Chemicals") or
                            o["name"].startswith("resource") or
                            o["name"].startswith("unit_")),
    ("Books & Schematics",  lambda o: _grp(o, "Books") or
                            o["name"].startswith("book") or
                            o["name"].startswith("schematic")),
    ("Vehicles",            lambda o: o["name"].startswith("vehicle")),
    ("Decorations",         lambda o: _grp(o, "Decor")),
    ("Special / Quest Items", lambda o: _grp(o, "Special Items") or
                            o["name"].startswith("quest")),
]


def _grp(obj: dict, keyword: str) -> bool:
    """Check if any of the object's comma-separated Group values contain *keyword*."""
    return keyword in obj.get("group", "")


def categorize_items(items: list[dict]) -> list[tuple[str, list[dict]]]:
    """
    Split items into sub-categories.  Returns a list of (category_name, items)
    tuples preserving insertion order, plus a final catch-all bucket.
    Hidden/internal items (CreativeMode='None') are separated first.
    """
    buckets: dict[str, list[dict]] = {}
    for cat, _ in _ITEM_CATEGORY_RULES:
        buckets[cat] = []
    buckets["Other"] = []
    hidden: list[dict] = []

    for obj in items:
        if obj.get("creative_mode") == "None":
            hidden.append(obj)
            continue
        matched = False
        for cat, rule in _ITEM_CATEGORY_RULES:
            if rule(obj):
                buckets[cat].append(obj)
                matched = True
                break
        if not matched:
            buckets["Other"].append(obj)

    # Build result: non-empty categories in definition order, then Other, then Hidden
    result = []
    for cat, _ in _ITEM_CATEGORY_RULES:
        if buckets[cat]:
            result.append((cat, buckets[cat]))
    if buckets["Other"]:
        result.append(("Other", buckets["Other"]))
    if hidden:
        result.append(("Hidden / Internal", hidden))
    return result


# ---------------------------------------------------------------------------
# Block sub-categories (by Class property from blocks.xml)
# ---------------------------------------------------------------------------

# Maps category name → set of Class values that belong to it.
_BLOCK_CLASS_GROUPS: list[tuple[str, set[str]]] = [
    ("Loot Containers", {
        "Loot", "SecureLoot", "QuestLoot", "CarExplodeLoot", "VendingMachine",
    }),
    ("Doors", {
        "DoorSecure", "TrapDoor", "PoweredDoor", "DrawBridge",
    }),
    ("Lighting", {
        "Light", "Spotlight", "PoweredLight", "TorchHeatMap",
    }),
    ("Electrical / Powered", {
        "Generator", "SolarPanel", "BatteryBank", "Powered", "Switch",
        "MotionSensor", "TimerRelay", "Speaker", "SpeakerTrader",
        "ElectricWire", "ActivateSwitch", "Activate", "ActivateSingle",
        "Collector",
    }),
    ("Traps & Hazards", {
        "Hazard", "BladeTrap", "Mine", "Damage", "TripWire",
        "PressurePlate", "Launcher", "Ranged",
    }),
    ("Vehicles", {
        "CarExplode",
    }),
    ("Vegetation", {
        "Tallgrass", "Deadgrass", "PlantGrowing", "ModelTree",
        "TrunkTip", "Trunk", "Cactus", "Hay",
    }),
    ("Functional Blocks", {
        "Campfire", "Workstation", "Forge", "SleepingBag",
        "LandClaim", "PlayerSign", "CompositeTileEntity",
    }),
    ("Events & Triggers", {
        "GameEvent", "QuestActivate", "RallyMarker",
        "TriggerDowngrade", "SpawnEntity", "Sleeper",
    }),
    ("Terrain & Structure", {
        "Liquidv2", "Ladder", "Stairs",
    }),
]

# Build a reverse lookup: Class value → category name
_BLOCK_CLASS_TO_CATEGORY: dict[str, str] = {}
for _cat, _classes in _BLOCK_CLASS_GROUPS:
    for _cls in _classes:
        _BLOCK_CLASS_TO_CATEGORY[_cls] = _cat


def categorize_blocks(blocks: list[dict]) -> list[tuple[str, list[dict]]]:
    """
    Split blocks into sub-categories by their Class property.
    Blocks without a Class go into 'Standard Blocks'.
    Any unknown Class values go into 'Other'.
    """
    buckets: dict[str, list[dict]] = {"Standard Blocks": []}
    for cat, _ in _BLOCK_CLASS_GROUPS:
        buckets[cat] = []
    buckets["Other"] = []

    for obj in blocks:
        cls = obj.get("block_class", "")
        if not cls:
            buckets["Standard Blocks"].append(obj)
        elif cls in _BLOCK_CLASS_TO_CATEGORY:
            buckets[_BLOCK_CLASS_TO_CATEGORY[cls]].append(obj)
        else:
            buckets["Other"].append(obj)

    # Build result: Standard Blocks first, then classified groups, then Other
    result = []
    if buckets["Standard Blocks"]:
        result.append(("Standard Blocks", buckets["Standard Blocks"]))
    for cat, _ in _BLOCK_CLASS_GROUPS:
        if buckets[cat]:
            result.append((cat, buckets[cat]))
    if buckets["Other"]:
        result.append(("Other", buckets["Other"]))
    return result


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
        block_class = props.get("Class", "")

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

        # Collect Extends chain names as fallback icon candidates
        # (used when neither CustomIcon nor own-name icon file exists)
        extends_chain: list[str] = []
        if custom_icon is None:
            _walk = props.get("Extends")
            _depth = 0
            while _walk and _depth < 10:
                extends_chain.append(_walk)
                _par = elements_by_name.get(_walk)
                if _par is None:
                    break
                _ext = _par.find("property[@name='Extends']")
                _walk = _ext.get("value", "") if _ext is not None else ""
                _depth += 1

        objects.append({
            "name": name,
            "source": source_label,
            "tag": tag,
            "icon_name": icon_name,
            "custom_icon_tint": custom_icon_tint,
            "creative_mode": creative_mode,
            "group": group,
            "block_class": block_class,
            "extends_chain": extends_chain,
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


# ---------------------------------------------------------------------------
# Icon processing
# ---------------------------------------------------------------------------

ICON_SIZE = 80  # 80×80 px (displayed at 40×40 CSS, 2× for retina)


def load_icon_index(icons_dir: str) -> dict[str, str]:
    """Return a case-insensitive mapping {lowercase_name: actual_name} for ItemIcons."""
    icons: dict[str, str] = {}
    if os.path.isdir(icons_dir):
        for fname in os.listdir(icons_dir):
            if fname.lower().endswith(".png"):
                base = fname[:-4]  # strip .png
                icons[base.lower()] = base
    return icons


def _parse_tint(tint: str) -> tuple[int, int, int] | None:
    """
    Parse a CustomIconTint value into (r, g, b).

    Supports two game formats:
      - Hex:    "FF8800" or "ff8800" (6 hex chars, optional alpha ignored)
      - Comma:  "255,136,0" (three decimal 0-255 values)
    """
    tint = tint.strip()
    if "," in tint:
        parts = [p.strip() for p in tint.split(",")]
        if len(parts) >= 3:
            try:
                return int(parts[0]), int(parts[1]), int(parts[2])
            except ValueError:
                return None
    else:
        # Hex format — strip optional alpha prefix for 8-char strings
        h = tint.lstrip("#")
        if len(h) == 8:
            h = h[2:]  # AARRGGBB → RRGGBB
        if len(h) >= 6:
            try:
                return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
            except ValueError:
                return None
    return None


def _apply_tint(img: Image.Image, tr: int, tg: int, tb: int) -> Image.Image:
    """
    Multiply-blend an RGB tint onto an RGBA image.

    For each pixel: out.r = pixel.r * tint.r / 255  (same for g, b).
    Alpha is preserved.  This matches how the game applies CustomIconTint.
    """
    img = img.convert("RGBA")
    r, g, b, a = img.split()

    r = r.point(lambda v: v * tr // 255)
    g = g.point(lambda v: v * tg // 255)
    b = b.point(lambda v: v * tb // 255)

    return Image.merge("RGBA", (r, g, b, a))


def process_icons(
    all_objects: dict[str, list[dict]],
    icon_index: dict[str, str],
    icons_src_dir: str,
    icons_dst_dir: str,
) -> dict[str, str]:
    """
    Copy, resize, and optionally tint every needed icon into *icons_dst_dir*.

    Returns a mapping  {output_filename: relative_path}  for use in HTML.
    Each unique (icon_name, tint) pair produces one output file.
    """
    os.makedirs(icons_dst_dir, exist_ok=True)

    # Collect all unique (icon_name, tint) combinations
    # needed maps (icon_name, tint) → (out_filename, actual_icon_on_disk)
    needed: dict[tuple[str, str | None], tuple[str, str]] = {}
    for objects in all_objects.values():
        for obj in objects:
            icon_name = obj["icon_name"]
            tint = obj.get("custom_icon_tint")
            key = (icon_name, tint)
            if key in needed:
                continue
            actual = icon_index.get(icon_name.lower())
            if actual is None:
                continue
            if tint:
                # Normalize tint for filename (replace commas)
                tint_slug = tint.replace(",", "_").replace(" ", "")
                out_name = f"{icon_name}__{tint_slug}.png"
            else:
                out_name = f"{icon_name}.png"
            needed[key] = (out_name, actual)

    # Process each icon
    icon_map: dict[tuple[str, str | None], str] = {}  # key → relative path
    dst_folder_name = os.path.basename(icons_dst_dir)
    total = len(needed)
    done = 0
    for (icon_name, tint), (out_name, actual) in needed.items():
        src_path = os.path.join(icons_src_dir, actual + ".png")
        dst_path = os.path.join(icons_dst_dir, out_name)

        img = Image.open(src_path).convert("RGBA")

        # Resize
        if img.size != (ICON_SIZE, ICON_SIZE):
            img = img.resize((ICON_SIZE, ICON_SIZE), Image.LANCZOS)

        # Tint
        if tint:
            rgb = _parse_tint(tint)
            if rgb:
                img = _apply_tint(img, *rgb)

        img.save(dst_path, "PNG", optimize=True)

        icon_map[(icon_name, tint)] = f"{dst_folder_name}/{out_name}"

        done += 1
        if done % 500 == 0 or done == total:
            print(f"    {done}/{total} icons processed")

    return icon_map


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
    icon_map: dict[tuple[str, str | None], str],
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

    # --- Items: split into sub-categories ---
    if "Items" in all_objects:
        items = all_objects["Items"]
        categories = categorize_items(items)

        lines.append(f'<h2 id="items">Items ({len(items)})</h2>')

        # Table of contents for categories
        lines.append('<div class="category-nav">')
        for cat, cat_items in categories:
            anchor = "items_" + cat.lower().replace(" ", "_").replace("/", "_")
            lines.append(
                f'  <a href="#{_esc(anchor)}">{_esc(cat)}</a>'
                f' <small>({len(cat_items)})</small>'
            )
        lines.append("</div>")

        for cat, cat_items in categories:
            anchor = "items_" + cat.lower().replace(" ", "_").replace("/", "_")
            lines.append(
                f'<h3 id="{_esc(anchor)}">{_esc(cat)} ({len(cat_items)})</h3>'
            )
            _render_table(lines, cat_items, anchor, localization, icon_map)

    # --- Blocks: split into sub-categories by Class ---
    if "Blocks" in all_objects:
        blocks = all_objects["Blocks"]
        block_categories = categorize_blocks(blocks)

        lines.append(f'<h2 id="blocks">Blocks ({len(blocks)})</h2>')

        # Table of contents for block categories
        lines.append('<div class="category-nav">')
        for cat, cat_blocks in block_categories:
            anchor = "blocks_" + cat.lower().replace(" ", "_").replace("/", "_").replace("&", "")
            lines.append(
                f'  <a href="#{_esc(anchor)}">{_esc(cat)}</a>'
                f' <small>({len(cat_blocks)})</small>'
            )
        lines.append("</div>")

        for cat, cat_blocks in block_categories:
            anchor = "blocks_" + cat.lower().replace(" ", "_").replace("/", "_").replace("&", "")
            lines.append(
                f'<h3 id="{_esc(anchor)}">{_esc(cat)} ({len(cat_blocks)})</h3>'
            )
            _render_table(lines, cat_blocks, anchor, localization, icon_map)

    # --- Item Modifiers: single table ---
    for source_label in ["Item Modifiers"]:
        if source_label not in all_objects:
            continue
        objects = all_objects[source_label]
        anchor = source_label.replace(" ", "_").lower()
        lines.append(f'<h2 id="{anchor}">{_esc(source_label)} ({len(objects)})</h2>')
        _render_table(lines, objects, anchor, localization, icon_map)

    lines.append(_JS)
    lines.append("</body></html>")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\n  Report saved → {output_path}")


def _render_table(
    lines: list[str],
    objects: list[dict],
    anchor: str,
    localization: dict,
    icon_map: dict,
):
    """Render a single catalog table into *lines*."""
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
        icon_key = (icon_name, tint)
        icon_path = icon_map.get(icon_key)
        if icon_path:
            icon_html = (
                f'<img src="{_esc(icon_path)}" width="40" height="40" '
                f'loading="lazy" alt="{_esc(icon_name)}">'
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
h3 {
    color: #aab; margin-top: 22px; margin-bottom: 6px; font-size: 16px;
    padding-left: 10px; border-left: 3px solid #4a5a8a;
}
.category-nav {
    display: flex; flex-wrap: wrap; gap: 6px 16px;
    margin: 10px 0 14px 0; font-size: 13px;
}
.category-nav a {
    color: #6a9fd8; text-decoration: none;
}
.category-nav a:hover { text-decoration: underline; }
.category-nav small { color: #777; }
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
td.icon-cell { width: 48px; text-align: center; }
td.icon-cell img { display: block; margin: auto; }
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

    print("\n[1/5] Loading objects …")
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

    print("\n[2/5] Parsing localization …")
    localization = parse_localization(LOCALIZATION_TXT)
    print(f"  Keys loaded: {len(localization)}")

    print("\n[3/5] Indexing icons …")
    icon_index = load_icon_index(ICONS_DIR)
    print(f"  Icon files found: {len(icon_index)}")

    # Stats: how many objects have matching icons?
    # Also resolve fallback icon names via Extends chain.
    found = 0
    missing = 0
    fallback_resolved = 0
    for objects in all_objects.values():
        for obj in objects:
            if obj["icon_name"].lower() in icon_index:
                found += 1
            else:
                # Try parent names from Extends chain as icon fallback
                resolved = False
                for parent_name in obj.get("extends_chain", []):
                    if parent_name.lower() in icon_index:
                        obj["icon_name"] = parent_name
                        found += 1
                        fallback_resolved += 1
                        resolved = True
                        break
                if not resolved:
                    missing += 1
    print(f"  Objects with icon: {found}, without: {missing}")
    if fallback_resolved:
        print(f"  Resolved via Extends fallback: {fallback_resolved}")

    print("\n[4/5] Processing icons (resize + tint) …")
    icons_dst_dir = OUTPUT_HTML.rsplit(".", 1)[0]  # build/inventory_catalog
    if os.path.isdir(icons_dst_dir):
        shutil.rmtree(icons_dst_dir)
    icon_map = process_icons(all_objects, icon_index, ICONS_DIR, icons_dst_dir)
    print(f"  Output icons: {len(icon_map)}")

    print("\n[5/5] Generating HTML report …")
    render_html(all_objects, localization, icon_map, OUTPUT_HTML)

    print(f"\nDone! → {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
