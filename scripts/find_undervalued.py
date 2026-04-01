"""
7 Days to Die — Undervalued Object Finder
==========================================

Analyses all crafting recipes and identifies objects whose EconomicValue
is lower than the total EconomicValue of their ingredients.  Also
propagates the "suspect" flag downstream: if an object's price is
already questionable, every item crafted from it is suspect too.

Usage
-----
    .venv/Scripts/python.exe scripts/find_undervalued.py

Output
------
    scripts/undervalued.html  — colour-coded report.
    Console summary is also printed.

Colour coding in the report
----------------------------
    RED    — directly undervalued: product value < sum of ingredient values.
    ORANGE — suspect (downstream): crafted from at least one undervalued
             or suspect ingredient, so its real cost is unknown.
    GREEN  — healthy: product value >= ingredient value.
    GREY   — unverifiable: at least one ingredient has no EconomicValue,
             so the comparison cannot be made.
"""

import os
import csv
from collections import defaultdict
from lxml import etree

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
CONFIG_DIR = os.path.join(ROOT_DIR, "Config")
BUILD_DIR = os.path.join(ROOT_DIR, "build")

RECIPES_XML = os.path.join(CONFIG_DIR, "recipes.xml")
ITEMS_XML = os.path.join(CONFIG_DIR, "items.xml")
BLOCKS_XML = os.path.join(CONFIG_DIR, "blocks.xml")
ITEM_MODIFIERS_XML = os.path.join(CONFIG_DIR, "item_modifiers.xml")
LOCALIZATION_TXT = os.path.join(CONFIG_DIR, "Localization.txt")
OUTPUT_HTML = os.path.join(BUILD_DIR, "undervalued.html")


# ---------------------------------------------------------------------------
# Parsing helpers (same logic as build_graph.py)
# ---------------------------------------------------------------------------

TAG_MAP = {"item": "item", "block": "block", "item_modifier": "item_modifier"}


def parse_objects(xml_path: str, source_label: str) -> dict:
    objects: dict = {}
    tree = etree.parse(xml_path)
    tag = TAG_MAP.get(source_label, source_label)
    for elem in tree.iter(tag):
        name = elem.get("name")
        if not name:
            continue
        eco = None
        bundle_size = 1
        for prop in elem.findall("property"):
            if prop.get("name") == "EconomicValue":
                try:
                    eco = int(prop.get("value", 0))
                except ValueError:
                    eco = None
            if prop.get("name") == "EconomicBundleSize":
                try:
                    bundle_size = int(prop.get("value", 1))
                except ValueError:
                    bundle_size = 1
        objects[name] = {
            "source": source_label,
            "economic_value": eco,
            "bundle_size": bundle_size,
        }
    return objects


def load_all_objects() -> dict:
    objs: dict = {}
    for path, label in [
        (ITEMS_XML, "item"),
        (BLOCKS_XML, "block"),
        (ITEM_MODIFIERS_XML, "item_modifier"),
    ]:
        if os.path.isfile(path):
            parsed = parse_objects(path, label)
            print(f"  {os.path.basename(path)} → {len(parsed)} objects")
            objs.update(parsed)
    print(f"  Total objects: {len(objs)}")
    return objs


def parse_recipes(xml_path: str) -> list[dict]:
    recipes = []
    tree = etree.parse(xml_path)
    for recipe_el in tree.iter("recipe"):
        name = recipe_el.get("name")
        if not name:
            continue
        count = int(recipe_el.get("count", 1))
        material_based = recipe_el.get("material_based", "false").lower() == "true"
        ingredients = []
        for ing in recipe_el.findall("ingredient"):
            ing_name = ing.get("name")
            if not ing_name:
                continue
            ing_count = int(ing.get("count", 1))
            ingredients.append({"name": ing_name, "count": ing_count})
        # Skip scrap-only recipes with no ingredients
        if not ingredients:
            continue
        recipes.append({
            "name": name,
            "count": count,
            "ingredients": ingredients,
            "material_based": material_based,
        })
    print(f"  recipes.xml → {len(recipes)} recipes (with ingredients)")
    return recipes


def parse_localization(txt_path: str) -> dict:
    loc: dict = {}
    with open(txt_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        header_lower = [h.strip().lower() for h in header]
        en_idx = header_lower.index("english") if "english" in header_lower else None
        ru_idx = header_lower.index("russian") if "russian" in header_lower else None
        for row in reader:
            if not row:
                continue
            key = row[0].strip()
            if key.endswith("Desc") or key.endswith("Tooltip"):
                continue
            en = row[en_idx].strip() if en_idx is not None and en_idx < len(row) else ""
            ru = row[ru_idx].strip() if ru_idx is not None and ru_idx < len(row) else ""
            loc[key] = {"english": en, "russian": ru}
    return loc


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

# Status constants
HEALTHY = "healthy"
UNDERVALUED = "undervalued"
SUSPECT = "suspect"
UNVERIFIABLE = "unverifiable"


def get_eco(objects: dict, name: str):
    """Return per-unit EconomicValue (EconomicValue / EconomicBundleSize) or None."""
    info = objects.get(name)
    if info is None:
        return None
    eco = info.get("economic_value")
    if eco is None:
        return None
    bundle_size = info.get("bundle_size", 1)
    return eco / bundle_size


def derive_forge_unit_values(objects: dict, recipes: list[dict]):
    """
    Derive EconomicValue for forge unit items (unit_*) that have no price.

    Forge-emptying recipes convert N × unit_X → 1 × resource.
    So 1 unit_X is worth (resource_per_unit_price / N).

    We use material_based forge recipes where the sole ingredient is a
    unit_* item with no EconomicValue, and the product has a known price.
    """
    derived = 0
    for r in recipes:
        if not r.get("material_based"):
            continue
        if len(r["ingredients"]) != 1:
            continue
        ing = r["ingredients"][0]
        ing_name = ing["name"]
        # Only process unit_ items with no EconomicValue
        if not ing_name.startswith("unit_"):
            continue
        ing_info = objects.get(ing_name)
        if ing_info is None or ing_info.get("economic_value") is not None:
            continue
        # Product must have a known price
        product_eco = get_eco(objects, r["name"])
        if product_eco is None:
            continue
        # N × unit_X → count × product
        # 1 unit_X = (product_per_unit_price × product_count) / ing_count
        unit_value = (product_eco * r["count"]) / ing["count"]
        # Store as EconomicValue with bundle_size=1 (already per-unit)
        ing_info["economic_value"] = unit_value
        ing_info["bundle_size"] = 1
        ing_info["derived"] = True
        derived += 1
        print(f"    {ing_name}: {unit_value:.4g} dukes/unit "
              f"(from {r['name']} ×{r['count']}, needs {ing['count']} units)")
    print(f"  Derived values for {derived} forge unit(s)")
    return objects


def analyse_recipes(objects: dict, recipes: list[dict]):
    """
    For each recipe compute ingredient cost vs product value.

    Returns:
        results — list of dicts with analysis for each recipe
        statuses — dict[name] → worst status across all recipes
    """
    results = []
    # Track per-object worst status
    statuses: dict[str, str] = {}

    for r in recipes:
        product = r["name"]
        product_count = r["count"]
        product_eco = get_eco(objects, product)

        ingredients_detail = []
        total_ingredient_cost = 0
        has_missing = False

        for ing in r["ingredients"]:
            ing_eco = get_eco(objects, ing["name"])
            if ing_eco is None:
                has_missing = True
                ingredients_detail.append({
                    "name": ing["name"],
                    "count": ing["count"],
                    "unit_value": None,
                    "total_value": None,
                })
            else:
                total = ing_eco * ing["count"]
                total_ingredient_cost += total
                ingredients_detail.append({
                    "name": ing["name"],
                    "count": ing["count"],
                    "unit_value": ing_eco,
                    "total_value": total,
                })

        # Determine status for this recipe
        if product_eco is None or has_missing:
            status = UNVERIFIABLE
        else:
            product_total = product_eco * product_count
            if product_total < total_ingredient_cost:
                status = UNDERVALUED
            else:
                status = HEALTHY

        entry = {
            "product": product,
            "product_count": product_count,
            "product_eco": product_eco,
            "product_total": round(product_eco * product_count, 2) if product_eco is not None else None,
            "ingredients": ingredients_detail,
            "ingredient_cost": round(total_ingredient_cost, 2) if not has_missing else None,
            "status": status,
        }
        results.append(entry)

        # Update worst status for this product
        prev = statuses.get(product, HEALTHY)
        statuses[product] = _worst(prev, status)

    return results, statuses


def _worst(a: str, b: str) -> str:
    """Return the more severe status."""
    order = {UNDERVALUED: 0, SUSPECT: 1, UNVERIFIABLE: 2, HEALTHY: 3}
    return a if order.get(a, 99) <= order.get(b, 99) else b


def propagate_suspect(recipes: list[dict], statuses: dict):
    """
    BFS propagation: if an ingredient is UNDERVALUED or SUSPECT,
    mark its downstream products as SUSPECT (unless already UNDERVALUED).
    """
    # Build adjacency: ingredient → set of products
    downstream: dict[str, set] = defaultdict(set)
    for r in recipes:
        for ing in r["ingredients"]:
            downstream[ing["name"]].add(r["name"])

    # Seeds: all undervalued objects
    queue = [name for name, st in statuses.items() if st == UNDERVALUED]
    visited: set = set(queue)

    while queue:
        current = queue.pop(0)
        for child in downstream.get(current, set()):
            if child in visited:
                continue
            prev = statuses.get(child, HEALTHY)
            if prev == UNDERVALUED:
                # Already worse — don't downgrade, but still propagate
                visited.add(child)
                queue.append(child)
                continue
            statuses[child] = SUSPECT
            visited.add(child)
            queue.append(child)

    return statuses


# ---------------------------------------------------------------------------
# HTML report
# ---------------------------------------------------------------------------

STATUS_COLORS = {
    UNDERVALUED: "#ff4444",
    SUSPECT: "#ff9800",
    HEALTHY: "#4CAF50",
    UNVERIFIABLE: "#9E9E9E",
}

STATUS_LABELS = {
    UNDERVALUED: "UNDERVALUED",
    SUSPECT: "SUSPECT (downstream)",
    HEALTHY: "OK",
    UNVERIFIABLE: "UNVERIFIABLE",
}


def _esc(text: str) -> str:
    """Escape HTML special characters."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def display_name(name: str, localization: dict) -> str:
    loc = localization.get(name, {})
    en = loc.get("english", "")
    return en if en else name


def render_html(results: list[dict], statuses: dict, localization: dict, output_path: str):
    # Sort: undervalued first, then suspect, then unverifiable, then healthy
    order = {UNDERVALUED: 0, SUSPECT: 1, UNVERIFIABLE: 2, HEALTHY: 3}
    sorted_results = sorted(results, key=lambda r: (order.get(statuses.get(r["product"], HEALTHY), 99),
                                                     order.get(r["status"], 99),
                                                     r["product"]))

    # Count stats
    unique_undervalued = sum(1 for s in statuses.values() if s == UNDERVALUED)
    unique_suspect = sum(1 for s in statuses.values() if s == SUSPECT)

    lines = []
    lines.append("<!DOCTYPE html>")
    lines.append('<html lang="en"><head><meta charset="UTF-8">')
    lines.append("<title>7D2D Undervalued Objects Report</title>")
    lines.append("<style>")
    lines.append("""
        body {
            background: #1a1a2e; color: #e0e0e0; font-family: 'Segoe UI', Consolas, monospace;
            margin: 0; padding: 20px;
        }
        h1 { color: #ffffff; margin-bottom: 5px; }
        .summary { color: #aaa; margin-bottom: 20px; font-size: 14px; }
        .summary span.red { color: #ff4444; font-weight: bold; }
        .summary span.orange { color: #ff9800; font-weight: bold; }
        .filters { margin-bottom: 15px; }
        .filters button {
            background: #2a2a4a; color: #e0e0e0; border: 1px solid #444;
            padding: 6px 14px; margin-right: 6px; cursor: pointer; border-radius: 4px;
            font-size: 13px;
        }
        .filters button:hover { background: #3a3a5a; }
        .filters button.active { border-color: #fff; background: #3a3a6a; }
        table { border-collapse: collapse; width: 100%; font-size: 13px; }
        th {
            background: #16213e; padding: 8px 10px; text-align: left;
            border-bottom: 2px solid #444; position: sticky; top: 0; cursor: pointer;
        }
        th:hover { background: #1a2a50; }
        td { padding: 6px 10px; border-bottom: 1px solid #2a2a4a; vertical-align: top; }
        tr.undervalued { background: rgba(255, 68, 68, 0.10); }
        tr.suspect { background: rgba(255, 152, 0, 0.10); }
        tr.unverifiable { background: rgba(158, 158, 158, 0.08); }
        tr.healthy { }
        .badge {
            display: inline-block; padding: 2px 8px; border-radius: 3px;
            font-size: 11px; font-weight: bold; color: #fff;
        }
        .ingredient-list { margin: 0; padding-left: 18px; }
        .ingredient-list li { margin-bottom: 2px; }
        .missing { color: #ff9800; font-style: italic; }
        .diff-positive { color: #4CAF50; }
        .diff-negative { color: #ff4444; font-weight: bold; }
        .search-box {
            background: #2a2a4a; color: #e0e0e0; border: 1px solid #444;
            padding: 6px 12px; border-radius: 4px; font-size: 13px; width: 300px;
            margin-bottom: 15px;
        }
    """)
    lines.append("</style></head><body>")
    lines.append("<h1>7D2D — Undervalued Objects Report</h1>")
    lines.append(f'<div class="summary">')
    lines.append(f'  Recipes analysed: <b>{len(results)}</b> &nbsp;|&nbsp; ')
    lines.append(f'  <span class="red">Undervalued objects: {unique_undervalued}</span> &nbsp;|&nbsp; ')
    lines.append(f'  <span class="orange">Suspect (downstream): {unique_suspect}</span>')
    lines.append(f'</div>')

    # Search
    lines.append('<input class="search-box" type="text" id="searchBox" placeholder="Search by name..." oninput="filterTable()">')

    # Filter buttons
    lines.append('<div class="filters">')
    lines.append('  <button class="active" onclick="setFilter(\'all\', this)" title="Show all recipes regardless of status">All</button>')
    lines.append('  <button onclick="setFilter(\'undervalued\', this)" title="Product EconomicValue is LOWER than the total cost of its ingredients. The object is directly underpriced — selling ingredients separately would be more profitable than crafting.">Undervalued</button>')
    lines.append('  <button onclick="setFilter(\'suspect\', this)" title="This object is crafted from at least one undervalued or suspect ingredient. Its real crafting cost is higher than what the ingredient values suggest, so its own EconomicValue is also questionable.">Suspect</button>')
    lines.append('  <button onclick="setFilter(\'unverifiable\', this)" title="At least one ingredient (or the product itself) has no EconomicValue defined, so the cost comparison cannot be performed.">Unverifiable</button>')
    lines.append('  <button onclick="setFilter(\'healthy\', this)" title="Product EconomicValue is greater than or equal to the total ingredient cost. The pricing is consistent.">Healthy</button>')
    lines.append('</div>')

    # Table
    lines.append('<table id="mainTable">')
    lines.append("<thead><tr>")
    lines.append('  <th onclick="sortTable(0)">Status</th>')
    lines.append('  <th onclick="sortTable(1)">Product</th>')
    lines.append('  <th onclick="sortTable(2)">Count</th>')
    lines.append('  <th onclick="sortTable(3)">Product Value</th>')
    lines.append('  <th onclick="sortTable(4)">Ingredient Cost</th>')
    lines.append('  <th onclick="sortTable(5)">Difference</th>')
    lines.append('  <th>Ingredients</th>')
    lines.append("</tr></thead><tbody>")

    for entry in sorted_results:
        product = entry["product"]
        # Use the propagated status for downstream suspect detection
        propagated = statuses.get(product, HEALTHY)
        # Row status: recipe's own assessment takes priority,
        # but healthy recipes inherit SUSPECT if product is flagged downstream
        if entry["status"] == UNDERVALUED:
            row_status = UNDERVALUED
        elif entry["status"] == UNVERIFIABLE:
            row_status = UNVERIFIABLE
        elif propagated == SUSPECT:
            row_status = SUSPECT
        else:
            row_status = HEALTHY
        color = STATUS_COLORS[row_status]
        label = STATUS_LABELS[row_status]
        dn = _esc(display_name(product, localization))
        product_id = _esc(product)

        product_total = entry["product_total"]
        ing_cost = entry["ingredient_cost"]

        pt_str = f"{product_total:.2f}" if product_total is not None else "N/A"
        ic_str = f"{ing_cost:.2f}" if ing_cost is not None else "N/A"

        if product_total is not None and ing_cost is not None:
            diff = product_total - ing_cost
            diff_class = "diff-positive" if diff >= 0 else "diff-negative"
            diff_str = f'<span class="{diff_class}">{diff:+.2f}</span>'
        else:
            diff_str = "—"

        # Ingredients list
        ing_html_parts = []
        for ing in entry["ingredients"]:
            ing_dn = _esc(display_name(ing["name"], localization))
            ing_id = _esc(ing["name"])
            if ing["total_value"] is not None:
                ing_html_parts.append(
                    f"<li>{ing_dn} <small>({ing_id})</small> "
                    f"×{ing['count']} = {ing['total_value']:.2f} "
                    f"<small>(unit: {ing['unit_value']:.4g})</small></li>"
                )
            else:
                ing_html_parts.append(
                    f'<li class="missing">{ing_dn} <small>({ing_id})</small> '
                    f"×{ing['count']} — <em>no EconomicValue</em></li>"
                )
        ing_html = '<ul class="ingredient-list">' + "".join(ing_html_parts) + "</ul>"

        lines.append(f'<tr class="{row_status}" data-status="{row_status}" data-name="{product_id.lower()} {dn.lower()}">')
        lines.append(f'  <td><span class="badge" style="background:{color}">{label}</span></td>')
        lines.append(f"  <td><b>{dn}</b><br><small>{product_id}</small></td>")
        lines.append(f"  <td>{entry['product_count']}</td>")
        lines.append(f"  <td>{pt_str}</td>")
        lines.append(f"  <td>{ic_str}</td>")
        lines.append(f"  <td>{diff_str}</td>")
        lines.append(f"  <td>{ing_html}</td>")
        lines.append("</tr>")

    lines.append("</tbody></table>")

    # JavaScript for filtering and sorting
    lines.append("""
<script>
let currentFilter = 'all';

function setFilter(status, btn) {
    currentFilter = status;
    document.querySelectorAll('.filters button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    filterTable();
}

function filterTable() {
    const search = document.getElementById('searchBox').value.toLowerCase();
    const rows = document.querySelectorAll('#mainTable tbody tr');
    rows.forEach(row => {
        const st = row.dataset.status;
        const name = row.dataset.name;
        const matchFilter = (currentFilter === 'all' || st === currentFilter);
        const matchSearch = !search || name.includes(search);
        row.style.display = (matchFilter && matchSearch) ? '' : 'none';
    });
}

let sortCol = -1, sortAsc = true;
function sortTable(col) {
    if (sortCol === col) { sortAsc = !sortAsc; } else { sortCol = col; sortAsc = true; }
    const tbody = document.querySelector('#mainTable tbody');
    const rows = Array.from(tbody.rows);
    rows.sort((a, b) => {
        let av = a.cells[col].textContent.trim();
        let bv = b.cells[col].textContent.trim();
        // Try numeric
        const an = parseFloat(av.replace(/[^\\d.-]/g, ''));
        const bn = parseFloat(bv.replace(/[^\\d.-]/g, ''));
        if (!isNaN(an) && !isNaN(bn)) {
            return sortAsc ? an - bn : bn - an;
        }
        return sortAsc ? av.localeCompare(bv) : bv.localeCompare(av);
    });
    rows.forEach(r => tbody.appendChild(r));
}
</script>
""")

    lines.append("</body></html>")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\n  Report saved → {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("7D2D Undervalued Object Finder")
    print("=" * 60)

    print("\n[1/6] Loading objects …")
    objects = load_all_objects()

    print("\n[2/6] Parsing recipes …")
    recipes = parse_recipes(RECIPES_XML)

    print("\n[3/6] Deriving forge unit values …")
    objects = derive_forge_unit_values(objects, recipes)

    print("\n[4/6] Analysing recipe economics …")
    results, statuses = analyse_recipes(objects, recipes)

    undervalued_count = sum(1 for s in statuses.values() if s == UNDERVALUED)
    print(f"  Directly undervalued: {undervalued_count}")

    print("\n[5/6] Propagating suspect status downstream …")
    statuses = propagate_suspect(recipes, statuses)
    suspect_count = sum(1 for s in statuses.values() if s == SUSPECT)
    print(f"  Suspect (downstream): {suspect_count}")

    print("\n[6/6] Generating HTML report …")
    localization = parse_localization(LOCALIZATION_TXT)
    render_html(results, statuses, localization, OUTPUT_HTML)

    # Console summary of undervalued objects
    print("\n" + "=" * 60)
    print("UNDERVALUED OBJECTS (product value < ingredient cost):")
    print("=" * 60)
    for entry in sorted(results, key=lambda e: e["product"]):
        if entry["status"] != UNDERVALUED:
            continue
        p = entry["product"]
        loc = localization.get(p, {})
        en = loc.get("english", p)
        pt = entry["product_total"]
        ic = entry["ingredient_cost"]
        diff = pt - ic if pt is not None and ic is not None else 0
        print(f"  {en:40s}  value={pt:>10.2f}  cost={ic:>10.2f}  diff={diff:>+10.2f}")

    print(f"\nTotal: {undervalued_count} undervalued + {suspect_count} suspect downstream")
    print("Done!")


if __name__ == "__main__":
    main()
