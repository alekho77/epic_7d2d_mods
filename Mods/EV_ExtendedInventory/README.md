# Extended Inventory

## Description

Expands the player's inventory from the vanilla 45 slots (5x9) to **60 slots (6x10)** using the native v3 item stack template with smaller cells that fit standard screen ratios.

> ### Client + Server Mod
>
> **This mod must be installed on both the dedicated server and each player's game client.** The server handles the extra inventory slots, but the UI changes require a local client installation to display correctly.

## Features

- **15 extra inventory slots** - from 45 to 60 total
- **Compact cell size** - 60x60px cells, down from 67x67px vanilla
- **Native v3 item stack UI** - durability bars, labels, overlays, lock mode, favorites, and quickswap stay on the vanilla template
- **Proper encumbrance support** - full compatibility with overweight item highlighting
- **Optimized layout** - fits without overlapping the toolbelt on 16:9 and 5:3 displays

## Installation

1. Copy the `EV_ExtendedInventory` folder into your game's `Mods/` directory
2. Restart the game or server

> This is a **client + server** mod - install it on both the client and server for full functionality.

## Compatibility

- 7 Days to Die v3.0
- Works with standard inventory mechanics, including Pack Mule and encumbrance
- Uses the native v3 `item_stack` template with a smaller `cell_size`

**Potential conflicts** with mods that:

- Modify inventory cell sizing
- Change the inventory window layout significantly
- Replace or remove the inventory grid `item_stack` element
- Alter inventory grid dimensions

## Mod Files

| File | Purpose |
| --- | --- |
| `Config/XUi_InGame/windows.xml` | Inventory window configuration (6x10 grid, cell sizing) |
| `Config/entityclasses.xml` | Player entity bag size adjustment |
| `Config/item_modifiers.xml` | Pocket mod slot adjustments |

## Changelog

### v1.1.0

- Initial public release with 6x10 inventory grid (60 slots)
- Native v3 item stack template with 60x60px cells
- Preserves vanilla v3 stack UI behavior
- Optimized for multiple screen ratios

---

**Author:** Aleksei Khozin  
**Version:** 1.1.0  
**Website:** <https://github.com/alekho77/epic_7d2d_mods>
