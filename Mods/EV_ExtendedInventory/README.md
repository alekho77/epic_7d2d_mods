# Extended Inventory

## Description

Expands the player's inventory from the vanilla 45 slots (5×9) to **60 slots (6×10)** with a custom compact cell design. Features scaled-down item icons and UI elements for a clean, professional look that fits standard screen ratios.

> ### 🟡 Client + Server Mod
>
> **This mod must be installed on both the dedicated server and each player's game client.** The server handles the extra inventory slots, but the UI changes (compact grid layout) require a local client installation to display correctly.

## Features

- **15 extra inventory slots** — from 45 to 60 total
- **Compact cell design** — 60×60px cells (down from 67×67px vanilla) with 57×57px icons
- **Proportionally scaled UI** — durability bars, labels, overlays, and borders all adjusted
- **Proper encumbrance support** — full compatibility with overweight item highlighting
- **Optimized layout** — fits without overlapping the toolbelt on 16:9 and 5:3 displays

## Installation

1. Copy the `EV_ExtendedInventory` folder into your game's `Mods/` directory
2. Restart the game or server

> This is a **client-side** mod — install it on both the client and server for full functionality.

## Compatibility

- 7 Days to Die 1.0 (Alpha 21+)
- Works with all standard game mechanics (Pack Mule, encumbrance, etc.)
- Uses a separate `backpack_item_stack_compact` template, reducing conflicts with most inventory mods

**Potential conflicts** with mods that:

- Modify inventory cell templates or sizing
- Change the inventory window layout significantly
- Override the `backpack_item_stack` control template
- Alter inventory grid dimensions

## Mod Files

| File | Purpose |
| --- | --- |
| `Config/XUi/controls.xml` | Custom compact item stack template definition |
| `Config/XUi/windows.xml` | Inventory window configuration (6×10 grid, cell sizing) |
| `Config/entityclasses.xml` | Player entity bag size adjustment |
| `Config/item_modifiers.xml` | Pocket mod slot adjustments |
| `Config/Localization.xml` | Localization strings |

## Changelog

### v1.1.0

- Initial public release with 6×10 inventory grid (60 slots)
- Custom compact cell design (60×60px)
- Proportionally scaled UI elements
- Optimized for multiple screen ratios

---

**Author:** Aleksei Khozin  
**Version:** 1.1.0  
**Website:** <https://github.com/alekho77/epic_7d2d_mods>
