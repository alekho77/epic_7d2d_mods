"""
7 Days to Die — Recipe Graph Builder

Parses Config/recipes.xml, Config/items.xml, Config/blocks.xml
and builds an interactive graph (pyvis) of crafting dependencies.

Nodes  = items / blocks  (weight = EconomicValue, label = name)
Edges  = ingredient → product  (weight = ingredient count)
"""

import os
import sys
import csv
from collections import defaultdict
from lxml import etree
from pyvis.network import Network

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
CONFIG_DIR = os.path.join(ROOT_DIR, "Config")

RECIPES_XML = os.path.join(CONFIG_DIR, "recipes.xml")
ITEMS_XML = os.path.join(CONFIG_DIR, "items.xml")
BLOCKS_XML = os.path.join(CONFIG_DIR, "blocks.xml")
ITEM_MODIFIERS_XML = os.path.join(CONFIG_DIR, "item_modifiers.xml")
LOCALIZATION_TXT = os.path.join(CONFIG_DIR, "Localization.txt")
OUTPUT_HTML = os.path.join(SCRIPT_DIR, "graph.html")

# ---------------------------------------------------------------------------
# 1b. Parse Localization.txt  →  dict[key] → {english, russian}
# ---------------------------------------------------------------------------

def parse_localization(txt_path: str) -> dict:
    """Return {key: {'english': str, 'russian': str}}"""
    loc: dict = {}
    with open(txt_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        # Find column indices
        header_lower = [h.strip().lower() for h in header]
        try:
            en_idx = header_lower.index("english")
        except ValueError:
            en_idx = None
        try:
            ru_idx = header_lower.index("russian")
        except ValueError:
            ru_idx = None

        for row in reader:
            if not row:
                continue
            key = row[0].strip()
            # Skip description keys (end with Desc) and tooltip keys
            if key.endswith("Desc") or key.endswith("Tooltip"):
                continue
            en = row[en_idx].strip() if en_idx is not None and en_idx < len(row) else ""
            ru = row[ru_idx].strip() if ru_idx is not None and ru_idx < len(row) else ""
            loc[key] = {"english": en, "russian": ru}

    print(f"  Localization.txt → {len(loc)} keys")
    return loc



# ---------------------------------------------------------------------------
# 1a. Parse items.xml & blocks.xml  →  dict[name] → {source, economic_value}
# ---------------------------------------------------------------------------

TAG_MAP = {
    "item": "item",
    "block": "block",
    "item_modifier": "item_modifier",
}


def parse_objects(xml_path: str, source_label: str) -> dict:
    """Return {name: {'source': str, 'economic_value': int|None, 'sellable': bool}}"""
    objects: dict = {}
    tree = etree.parse(xml_path)

    tag = TAG_MAP.get(source_label, source_label)
    for elem in tree.iter(tag):
        name = elem.get("name")
        if not name:
            continue
        eco = None
        sellable = True  # default: sellable unless explicitly set to false
        creative = True  # default: available in creative mode
        for prop in elem.findall("property"):
            if prop.get("name") == "EconomicValue":
                try:
                    eco = int(prop.get("value", 0))
                except ValueError:
                    eco = None
            if prop.get("name") == "SellableToTrader":
                sellable = prop.get("value", "true").lower() != "false"
            if prop.get("name") == "CreativeMode":
                creative = prop.get("value", "").lower() != "none"
        objects[name] = {"source": source_label, "economic_value": eco, "sellable": sellable, "creative": creative}
    return objects


def load_all_objects() -> dict:
    """Merge items + blocks into one dict."""
    objs: dict = {}
    if os.path.isfile(ITEMS_XML):
        objs.update(parse_objects(ITEMS_XML, "item"))
        print(f"  items.xml  → {len(objs)} objects")
    if os.path.isfile(BLOCKS_XML):
        before = len(objs)
        objs.update(parse_objects(BLOCKS_XML, "block"))
        print(f"  blocks.xml → {len(objs) - before} objects")
    if os.path.isfile(ITEM_MODIFIERS_XML):
        before = len(objs)
        objs.update(parse_objects(ITEM_MODIFIERS_XML, "item_modifier"))
        print(f"  item_modifiers.xml → {len(objs) - before} objects")
    print(f"  Total objects: {len(objs)}")
    return objs


# ---------------------------------------------------------------------------
# 2. Parse recipes.xml  →  list of recipes
# ---------------------------------------------------------------------------

def parse_recipes(xml_path: str) -> list[dict]:
    """
    Return list of:
      {
        'name': str,          # product name
        'count': int,         # product count
        'craft_area': str,
        'tags': str,
        'ingredients': [ {'name': str, 'count': int}, ... ]
      }
    """
    recipes = []
    tree = etree.parse(xml_path)

    for recipe_el in tree.iter("recipe"):
        name = recipe_el.get("name")
        if not name:
            continue

        count = int(recipe_el.get("count", 1))
        craft_area = recipe_el.get("craft_area", "hand")
        tags = recipe_el.get("tags", "")

        ingredients = []
        for ing in recipe_el.findall("ingredient"):
            ing_name = ing.get("name")
            if not ing_name:
                continue
            ing_count = int(ing.get("count", 1))
            ingredients.append({"name": ing_name, "count": ing_count})

        recipes.append({
            "name": name,
            "count": count,
            "craft_area": craft_area,
            "tags": tags,
            "ingredients": ingredients,
        })

    print(f"  recipes.xml → {len(recipes)} recipes")
    return recipes


# ---------------------------------------------------------------------------
# 3. Build graph data
# ---------------------------------------------------------------------------

def build_graph_data(objects: dict, recipes: list[dict]):
    """
    Returns:
      nodes  – dict[name] → {source, economic_value, is_base}
      edges  – list of (ingredient_name, product_name, count)
    """
    # Start with known objects
    nodes: dict = {}
    for name, info in objects.items():
        nodes[name] = {**info, "is_base": True}
        if "sellable" not in nodes[name]:
            nodes[name]["sellable"] = True
        if "creative" not in nodes[name]:
            nodes[name]["creative"] = True

    # Track which names appear as recipe outputs
    recipe_outputs: set = set()

    edges: list = []
    for r in recipes:
        product = r["name"]
        recipe_outputs.add(product)

        # Ensure product node exists
        if product not in nodes:
            nodes[product] = {
                "source": "unknown",
                "economic_value": None,
                "is_base": False,
                "sellable": True,
                "creative": True,
            }
        else:
            nodes[product]["is_base"] = False

        for ing in r["ingredients"]:
            ing_name = ing["name"]
            # Ensure ingredient node exists
            if ing_name not in nodes:
                nodes[ing_name] = {
                    "source": "unknown",
                    "economic_value": None,
                    "is_base": True,
                    "sellable": True,
                    "creative": True,
                }
            edges.append((ing_name, product, ing["count"]))

    # Mark nodes that are never a recipe output as base resources
    for name in nodes:
        if name not in recipe_outputs:
            nodes[name]["is_base"] = True

    base_count = sum(1 for n in nodes.values() if n["is_base"])
    print(f"  Graph: {len(nodes)} nodes ({base_count} base), {len(edges)} edges")
    return nodes, edges


def filter_unsellable_leaves(nodes: dict, edges: list):
    """
    Remove nodes that are NOT used as an ingredient in any recipe
    AND meet at least one of these conditions:
      - SellableToTrader="false"
      - EconomicValue is not defined (N/A)
    Nodes that ARE used as ingredients are always kept.
    """
    # Collect names used as ingredients (edge sources)
    used_as_ingredient: set = set()
    for src, dst, _ in edges:
        used_as_ingredient.add(src)

    to_remove: set = set()
    for name, info in nodes.items():
        if name in used_as_ingredient:
            continue
        # Remove if unsellable OR has no EconomicValue (and not an ingredient)
        if not info.get("sellable", True):
            to_remove.add(name)
        elif info.get("economic_value") is None:
            to_remove.add(name)

    for name in to_remove:
        del nodes[name]

    edges = [(s, d, c) for s, d, c in edges if d not in to_remove and s not in to_remove]

    print(f"  Filtered out {len(to_remove)} unsellable/no-value leaf nodes")
    print(f"  After filter: {len(nodes)} nodes, {len(edges)} edges")
    return nodes, edges


# ---------------------------------------------------------------------------
# 4. Colour helpers
# ---------------------------------------------------------------------------

def node_color(info: dict) -> str:
    """Return colour string for a node."""
    if not info.get("creative", True):
        return "#9137FF"   # purple — not in creative (template/base class)
    if info["is_base"]:
        return "#4CAF50"   # green — base resource (no recipe)
    if info["source"] == "item":
        return "#229CFF"   # light blue — item
    if info["source"] == "block":
        return "#EEFF00"   # yellow — block
    if info["source"] == "item_modifier":
        return "#FD7B10"   # orange — mod
    return "#9E9E9E"       # grey — unknown / unit


def node_size(info: dict) -> int:
    eco = info.get("economic_value")
    if eco is None or eco <= 0:
        return 8
    if eco < 10:
        return 10
    if eco < 50:
        return 14
    if eco < 200:
        return 20
    if eco < 1000:
        return 28
    return 36


# ---------------------------------------------------------------------------
# 5. Render with pyvis
# ---------------------------------------------------------------------------

def render_graph(nodes: dict, edges: list, output_path: str):
    net = Network(
        height="100vh",
        width="100%",
        directed=True,
        bgcolor="#1a1a2e",
        font_color="#ffffff",
        select_menu=True,
        filter_menu=True,
        cdn_resources="remote",        # use CDN instead of local lib/
    )

    # Physics settings for large graphs
    net.barnes_hut(
        gravity=-3000,
        central_gravity=0.3,
        spring_length=150,
        spring_strength=0.01,
        damping=0.09,
        overlap=0,
    )

    # Add nodes
    for name, info in nodes.items():
        eco = info.get("economic_value")
        eco_str = f"EconomicValue: {eco}" if eco is not None else "EconomicValue: N/A"
        source_str = info["source"]
        base_str = "BASE (no recipe)" if info["is_base"] else "craftable"

        en_name = info.get("name_en", "")
        ru_name = info.get("name_ru", "")
        is_creative = info.get("creative", True)
        display_name = en_name or name
        title_lines = [name]
        if en_name:
            title_lines.append(f"EN: {en_name}")
        if ru_name:
            title_lines.append(f"RU: {ru_name}")
        title_lines.append(f"{source_str} | {base_str}")
        title_lines.append(eco_str)
        if not is_creative:
            title_lines.append("⚠ CreativeMode=None (template/base class)")
        title = "\n".join(title_lines)
        label = display_name

        # pyvis strips `color` when `group` is present, so we only
        # set group for nodes where we rely on group auto-coloring.
        # For creative=None nodes we omit group so the explicit dark-red
        # colour takes effect.
        node_opts = dict(
            label=label,
            title=title,
            color=node_color(info),
            size=node_size(info),
            value=eco if eco else 1,
        )
        if is_creative:
            node_opts["group"] = source_str

        net.add_node(name, **node_opts)

    # Aggregate duplicate edges (same ingredient→product may appear in
    # multiple recipes; we sum counts).
    edge_map: dict = defaultdict(int)
    for src, dst, count in edges:
        edge_map[(src, dst)] += count

    for (src, dst), total_count in edge_map.items():
        net.add_edge(
            src,
            dst,
            value=total_count,
            title=f"{src} → {dst}  ×{total_count}",
            label=str(total_count),
            color="#555555",
            font={"size": 8, "color": "#aaaaaa"},
        )

    net.write_html(output_path)
    print(f"\n  Graph saved → {output_path}")
    print(f"  Nodes: {len(nodes)},  Edges: {len(edge_map)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("7D2D Recipe Graph Builder")
    print("=" * 60)

    print("\n[1/5] Loading objects from items.xml & blocks.xml …")
    objects = load_all_objects()

    print("\n[2/5] Parsing recipes & localization …")
    recipes = parse_recipes(RECIPES_XML)
    localization = parse_localization(LOCALIZATION_TXT)

    print("\n[3/5] Building graph …")
    nodes, edges = build_graph_data(objects, recipes)

    print("\n[4/5] Filtering unsellable leaf nodes …")
    nodes, edges = filter_unsellable_leaves(nodes, edges)

    # Enrich nodes with localization
    for name, info in nodes.items():
        loc = localization.get(name, {})
        info["name_en"] = loc.get("english", "")
        info["name_ru"] = loc.get("russian", "")

    print("\n[5/5] Rendering with pyvis …")
    render_graph(nodes, edges, OUTPUT_HTML)

    print("\nDone! Open graph.html in a browser.")


if __name__ == "__main__":
    main()
