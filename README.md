# EpicVales — 7 Days to Die Modlets

A collection of modlets for **7 Days to Die** maintained by **Aleksei Khozin** for the [EpicVales](https://steamcommunity.com/groups/epicvales) Steam group.

All mods use the `EV_` prefix and are designed to be lightweight, focused, and compatible with multiplayer servers.

## About This Repository

Each modlet lives in its own subfolder under `Mods/` and targets a single feature or gameplay adjustment. Mods use the standard 7 Days to Die XPath patching system — vanilla files are never modified directly.

Some mods are server-side only; others require installation on both server and client. Each mod's `README.md` specifies its installation requirements.

## Structure

- **`Mods/`** — individual modlet folders, each self-contained with its own `ModInfo.xml` and `README.md`
- **`Data/Config/`** — reference copy of the unmodified vanilla game configuration files (source of truth for authoring patches)
- **`scripts/`** — utility scripts for mod development and analysis
- **`docs/`** — modding documentation:
  - [Modding Guide](docs/modding_guide.md) — overview of all modding phases
  - [Phase 1: XML Modlets](docs/phase1_xml_modlets.md) — XPath patching, mod structure, examples
  - [Phase 2: Harmony Mods](docs/phase2_harmony_mods.md) — C# patches with HarmonyLib
  - [Phase 3: Total Conversion](docs/phase3_total_conversion.md) — deep modding and asset replacement
  - [Game File Inventory](docs/game_files.md) — complete reference of game installation files

## Installation

1. Download the desired mod folder(s)
2. Copy them into your game's `Mods/` directory:
   - **Client:** `<GameDirectory>/Mods/`
   - **Dedicated Server:** `<ServerDirectory>/Mods/`
3. Restart the game or server

## Compatibility

All mods target **7 Days to Die 1.0+**. Each mod's `README.md` lists any known conflicts with other mods.

## License

Free to use and modify for personal and server use. Credit appreciated but not required.

---

**Author:** Aleksei Khozin  
**Website:** <https://www.epicvales.online/>
