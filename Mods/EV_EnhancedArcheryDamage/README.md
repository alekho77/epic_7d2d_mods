# Enhanced Archery Damage

## Description

A comprehensive archery overhaul that increases damage for bows, crossbows, arrows, and bolts, and adds crafting recipes to convert arrows into crossbow bolts and vice versa at a 1:1 ratio with no material loss.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- Boosted damage for all arrow and bolt types
- Increased base damage bonus for bows and crossbows
- Balanced scaling — higher tier ammo gets proportionally larger boosts
- **10 new recipes** — 5 arrow-to-bolt conversions + 5 bolt-to-arrow conversions
- **1:1 conversion** — no material loss
- **No XP gain** — prevents exploit crafting for experience
- **Tiered craft times** — higher tier ammo takes slightly longer to convert
- Stone tier can be converted anywhere; Iron+ requires a Workbench
- **10 disassembled ammo bundles** — open to receive raw crafting ingredients for arrows and bolts
- Bundle icons match vanilla ammo bundles with a light red tint for easy identification

## Damage Changes

### Arrows

| Ammo Type | Vanilla | Modded | Change |
| --- | --- | --- | --- |
| Stone Arrow | 35 | 49 | +40% |
| Iron Arrow | 38 | 68 | +79% |
| Steel AP Arrow | 42 | 92 | +119% |
| Flaming Arrow | 25 | 38 | +52% |
| Exploding Arrow | 180 | 220 | +22% |

### Crossbow Bolts

| Ammo Type | Vanilla | Modded | Change |
| --- | --- | --- | --- |
| Stone Bolt | 50 | 58 | +16% |
| Iron Bolt | 59 | 100 | +69% |
| Steel AP Bolt | 63 | 142 | +125% |
| Flaming Bolt | 38 | 68 | +79% |
| Exploding Bolt | 250 | 270 | +8% |

### Weapons (base_add bonus)

| Weapon | Vanilla | Modded | Change |
| --- | --- | --- | --- |
| Wooden Bow | +9 | +19 | +111% |
| Compound Bow | +29 | +51 | +76% |
| Compound Crossbow | +25 | +50 | +100% |

## Conversion Recipes

| From | To | Craft Time | Station |
| --- | --- | --- | --- |
| Stone Arrow | Stone Bolt | 1s | Anywhere |
| Iron Arrow | Iron Bolt | 1s | Workbench |
| Steel AP Arrow | Steel AP Bolt | 2s | Workbench |
| Flaming Arrow | Flaming Bolt | 3s | Workbench |
| Exploding Arrow | Exploding Bolt | 4s | Workbench |
| Stone Bolt | Stone Arrow | 1s | Anywhere |
| Iron Bolt | Iron Arrow | 1s | Workbench |
| Steel AP Bolt | Steel AP Arrow | 2s | Workbench |
| Flaming Bolt | Flaming Arrow | 3s | Workbench |
| Exploding Bolt | Exploding Arrow | 4s | Workbench |

## Disassembled Ammo Bundles

The mod adds 10 disassembled ammo bundles — one for each arrow and crossbow bolt type. Opening a bundle gives you the raw crafting ingredients instead of finished ammo. Standard bundles yield materials for 100 ammo; exploding variants yield materials for 75.

### Arrow Kits

| Bundle | Contents |
| --- | --- |
| Disassembled Stone Arrow Kit | 100 Small Stones, 100 Wood, 100 Feathers |
| Disassembled Iron Arrow Kit | 100 Iron Arrowheads, 100 Wood, 100 Feathers |
| Disassembled Steel AP Arrow Kit | 100 Steel AP Arrowheads, 200 Scrap Polymers |
| Disassembled Flaming Arrow Kit | 100 Steel AP Arrowheads, 200 Scrap Polymers, 200 Gun Powder, 500 Cloth, 100 Animal Fat |
| Disassembled Exploding Arrow Kit | 75 Steel AP Arrowheads, 150 Scrap Polymers, 450 Gun Powder, 75 Paper, 75 Yucca Fibers |

### Crossbow Bolt Kits

| Bundle | Contents |
| --- | --- |
| Disassembled Stone Bolt Kit | 100 Small Stones, 100 Wood, 100 Feathers |
| Disassembled Iron Bolt Kit | 100 Iron Arrowheads, 100 Wood, 100 Feathers |
| Disassembled Steel AP Bolt Kit | 100 Steel AP Arrowheads, 200 Scrap Polymers |
| Disassembled Flaming Bolt Kit | 100 Steel AP Arrowheads, 200 Scrap Polymers, 200 Gun Powder, 500 Cloth, 100 Animal Fat |
| Disassembled Exploding Bolt Kit | 75 Steel AP Arrowheads, 150 Scrap Polymers, 600 Gun Powder, 75 Paper, 75 Yucca Fibers |

## Installation

1. Copy the `EV_EnhancedArcheryDamage` folder into your game's `Mods/` directory
2. Restart the game or server

## Compatibility

- 7 Days to Die 1.0 (Alpha 21+)
- Server-side mod — works without client installation
- May conflict with mods that modify arrow/bolt EntityDamage values or bow/crossbow base_add damage

## Changelog

### v1.2.0

- Added 10 disassembled ammo bundles (5 arrow kits + 5 crossbow bolt kits) containing raw crafting ingredients
- Added Localization.txt with English and Russian translations for all bundle items

### v1.1.0

- Merged TransmuteArrowsAndBolts mod — added 10 recipes to convert arrows to bolts and vice versa (1:1 ratio, no material loss)

### v1.0.0

- Initial release with enhanced damage for all arrow/bolt types and archery weapons

---

**Author:** Aleksei Khozin  
**Version:** 1.2.0  
**Website:** <https://github.com/alekho77/epic_7d2d_mods>
