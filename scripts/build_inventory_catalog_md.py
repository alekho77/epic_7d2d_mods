"""
7 Days to Die — Inventory Object Catalog (Markdown)
====================================================

Parses items.xml, blocks.xml, and item_modifiers.xml to build
a complete Markdown catalog of all inventory-compatible game objects,
with internal names, English and Russian display names,
Russian descriptions, and CreativeMode values.

Usage
-----
    .venv/Scripts/python.exe scripts/build_inventory_catalog_md.py

Output
------
    docs/inventory_catalog.md
"""

import os
import csv
import re
from lxml import etree

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
CONFIG_DIR = os.path.join(ROOT_DIR, "Data", "Config")
DOCS_DIR = os.path.join(ROOT_DIR, "docs")

ITEMS_XML = os.path.join(CONFIG_DIR, "items.xml")
BLOCKS_XML = os.path.join(CONFIG_DIR, "blocks.xml")
ITEM_MODIFIERS_XML = os.path.join(CONFIG_DIR, "item_modifiers.xml")
LOCALIZATION_TXT = os.path.join(CONFIG_DIR, "Localization.txt")
OUTPUT_MD = os.path.join(DOCS_DIR, "inventory_catalog.md")


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
    """Split items into sub-categories."""
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
# Item Modifier sub-categories (matches Mod Categories from modding_guide.md)
# ---------------------------------------------------------------------------

_MOD_CATEGORY_RULES: list[tuple[str, callable]] = [
    ("Gun Mods",            lambda o: o["name"].startswith("modGun") or
                            o["name"].startswith("modShotgun")),
    ("Melee Mods",          lambda o: o["name"].startswith("modMelee")),
    ("Armor Mods",          lambda o: o["name"].startswith("modArmor")),
    ("Dye Mods",            lambda o: o["name"].startswith("modDye")),
    ("Vehicle Mods",        lambda o: o["name"].startswith("modVehicle")),
    ("Robotic Drone Mods",  lambda o: o["name"].startswith("modRoboticDrone")),
    ("Fuel Tank Mods",      lambda o: o["name"].startswith("modFuelTank")),
]


def categorize_modifiers(modifiers: list[dict]) -> list[tuple[str, list[dict]]]:
    """Split item modifiers into sub-categories by name prefix."""
    buckets: dict[str, list[dict]] = {}
    for cat, _ in _MOD_CATEGORY_RULES:
        buckets[cat] = []
    buckets["Other"] = []
    hidden: list[dict] = []

    for obj in modifiers:
        cm = obj.get("creative_mode", "")
        if cm in ("Dev", "Test", "None"):
            hidden.append(obj)
            continue
        matched = False
        for cat, rule in _MOD_CATEGORY_RULES:
            if rule(obj):
                buckets[cat].append(obj)
                matched = True
                break
        if not matched:
            buckets["Other"].append(obj)

    result = []
    for cat, _ in _MOD_CATEGORY_RULES:
        if buckets[cat]:
            result.append((cat, buckets[cat]))
    if buckets["Other"]:
        result.append(("Other", buckets["Other"]))
    if hidden:
        result.append(("Hidden / Dev / Test", hidden))
    return result


# ---------------------------------------------------------------------------
# Block sub-categories (by Class property from blocks.xml)
# ---------------------------------------------------------------------------

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

_BLOCK_CLASS_TO_CATEGORY: dict[str, str] = {}
for _cat, _classes in _BLOCK_CLASS_GROUPS:
    for _cls in _classes:
        _BLOCK_CLASS_TO_CATEGORY[_cls] = _cat


def categorize_blocks(blocks: list[dict]) -> list[tuple[str, list[dict]]]:
    """Split blocks into sub-categories by their Class property."""
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

    result = []
    if buckets["Standard Blocks"]:
        result.append(("Standard Blocks", buckets["Standard Blocks"]))
    for cat, _ in _BLOCK_CLASS_GROUPS:
        if buckets[cat]:
            result.append((cat, buckets[cat]))
    if buckets["Other"]:
        result.append(("Other", buckets["Other"]))
    return result


# ---------------------------------------------------------------------------
# XML Parsing
# ---------------------------------------------------------------------------

def parse_objects(xml_path: str, tag: str, source_label: str) -> list[dict]:
    """Parse all objects from an XML file, resolving CustomIcon via Extends."""
    tree = etree.parse(xml_path)
    root = tree.getroot()

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

        props = {}
        for prop in elem.findall("property"):
            pname = prop.get("name")
            if pname:
                props[pname] = prop.get("value", "")

        creative_mode = props.get("CreativeMode", "")
        group = props.get("Group", "")
        block_class = props.get("Class", "")

        objects.append({
            "name": name,
            "source": source_label,
            "creative_mode": creative_mode,
            "group": group,
            "block_class": block_class,
        })

    return objects


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
# Markdown rendering
# ---------------------------------------------------------------------------

def _md_escape(text: str) -> str:
    """Escape pipe characters and collapse newlines for Markdown table cells."""
    return text.replace("\\n", " ").replace("|", "\\|").replace("\n", " ")


def _gfm_anchor(heading: str) -> str:
    """Compute the GFM-compatible anchor from a heading string.

    GitHub's algorithm: lowercase → keep only [a-z0-9 -] → spaces to hyphens.
    """
    h = heading.lower()
    h = re.sub(r"[^a-z0-9 \-]", "", h)
    h = h.replace(" ", "-")
    return h


def _render_table(lines: list[str], objects: list[dict], localization: dict):
    """Render a Markdown table for a list of objects."""
    lines.append("| Name (ID) | English | Russian | Description (RU) | Creative |")
    lines.append("| --- | --- | --- | --- | --- |")

    for obj in objects:
        name = obj["name"]
        creative = obj["creative_mode"] or "default"

        loc_name = localization.get(name, {})
        en_name = _md_escape(loc_name.get("english", ""))
        ru_name = _md_escape(loc_name.get("russian", ""))

        loc_desc = localization.get(name + "Desc", {})
        ru_desc = _md_escape(loc_desc.get("russian", ""))

        lines.append(
            f"| `{name}` | {en_name} | {ru_name} | {ru_desc} | {creative} |"
        )

    lines.append("")


def render_markdown(
    all_objects: dict[str, list[dict]],
    localization: dict,
    output_path: str,
):
    grand_total = sum(len(objs) for objs in all_objects.values())

    lines: list[str] = []
    lines.append("# 7D2D Inventory Object Catalog")
    lines.append("")
    parts = [f"**Total objects: {grand_total}**"]
    for label, objects in all_objects.items():
        parts.append(f"{label}: {len(objects)}")
    lines.append(" | ".join(parts))
    lines.append("")

    # Build section structure: list of (heading_level, heading_text, objects)
    sections: list[tuple[int, str, list[dict] | None]] = []

    if "Items" in all_objects:
        items = all_objects["Items"]
        categories = categorize_items(items)
        sections.append((2, f"Items ({len(items)})", None))
        for cat, cat_items in categories:
            sections.append((3, f"Items - {cat} ({len(cat_items)})", cat_items))

    if "Blocks" in all_objects:
        blocks = all_objects["Blocks"]
        block_categories = categorize_blocks(blocks)
        sections.append((2, f"Blocks ({len(blocks)})", None))
        for cat, cat_blocks in block_categories:
            sections.append((3, f"Blocks - {cat} ({len(cat_blocks)})", cat_blocks))

    if "Item Modifiers" in all_objects:
        modifiers = all_objects["Item Modifiers"]
        mod_categories = categorize_modifiers(modifiers)
        sections.append((2, f"Item Modifiers ({len(modifiers)})", None))
        for cat, cat_mods in mod_categories:
            sections.append((3, f"Item Modifiers - {cat} ({len(cat_mods)})", cat_mods))

    # Table of contents
    lines.append("## Table of Contents")
    lines.append("")
    for level, heading, _ in sections:
        anchor = _gfm_anchor(heading)
        indent = "  " if level == 3 else ""
        lines.append(f"{indent}- [{heading}](#{anchor})")
    lines.append("")

    # Render sections
    for level, heading, objects in sections:
        hashes = "#" * level
        lines.append(f"{hashes} {heading}")
        lines.append("")
        if objects is not None:
            _render_table(lines, objects, localization)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\n  Catalog saved → {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("7D2D Inventory Object Catalog (Markdown)")
    print("=" * 60)

    print("\n[1/3] Loading objects …")
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

    print("\n[2/3] Parsing localization …")
    localization = parse_localization(LOCALIZATION_TXT)
    print(f"  Keys loaded: {len(localization)}")

    print("\n[3/3] Generating Markdown catalog …")
    render_markdown(all_objects, localization, OUTPUT_MD)

    print(f"\nDone! → {OUTPUT_MD}")


if __name__ == "__main__":
    main()
