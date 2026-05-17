# Enhanced Archery Damage

## Description

A comprehensive archery overhaul that increases damage for bows, crossbows, arrows, and bolts, adds crafting recipes to convert arrows into crossbow bolts and vice versa at a 1:1 ratio with no material loss, and adds a perk-based ammo refund chance for archery projectiles.

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
- **10 disassembled ammo bundles** — craft from 30 arrows or bolts to recover 75% of raw materials
- Disassembly recipes require a **Workbench** and reading all 7 volumes of **Ranger's Guide to Archery**
- Bundle icons use vanilla ammo icons with a light red tint for easy identification
- **Perk-based ammo refund** - vanilla arrows and bolts have a chance to be returned after projectile impact based on Archery perk level

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

## Archery Ammo Refund

Starting in v1.3.0, vanilla arrows and crossbow bolts can be refunded after projectile impact. This is a pure XML implementation: the ammo is spent normally when fired, then the mod has a chance to add one matching arrow or bolt back to the player's inventory when the projectile impact event fires.

| Archery Perk Level | Refund Chance |
| --- | --- |
| 0 | 0% |
| 1 | 10% |
| 2 | 20% |
| 3 | 30% |
| 4 | 40% |
| 5 | 50% |

This refund is added for vanilla arrows and bolts only:

- Stone, Iron, Steel AP, Flaming, and Exploding Arrows
- Stone, Iron, Steel AP, Flaming, and Exploding Crossbow Bolts

If another mod adds custom arrows or bolts, those custom ammo items will not automatically receive this refund effect. Their item XML needs matching `onProjectileImpact` refund triggers and matching `gameevents.xml` AddItems events, following the same pattern used for the vanilla arrows and bolts.

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

The mod adds 10 disassembly recipes — one for each arrow and crossbow bolt type. Craft a bundle from 30 arrows or bolts on a **Workbench** to recover **75% of the original materials**. Recipes are unlocked after reading all 7 volumes of **Ranger's Guide to Archery**.

### Arrow Kits

| Bundle | Input | Output (75%) |
| --- | --- | --- |
| Disassembled Stone Arrow Kit | 30 Stone Arrows | 22 Small Stones, 22 Wood, 22 Feathers |
| Disassembled Iron Arrow Kit | 30 Iron Arrows | 22 Iron Arrowheads, 22 Wood, 22 Feathers |
| Disassembled Steel AP Arrow Kit | 30 Steel AP Arrows | 22 Steel AP Arrowheads, 45 Scrap Polymers |
| Disassembled Flaming Arrow Kit | 30 Flaming Arrows | 22 Steel AP Arrowheads, 45 Scrap Polymers, 45 Gun Powder, 112 Cloth, 22 Animal Fat |
| Disassembled Exploding Arrow Kit | 30 Exploding Arrows | 22 Steel AP Arrowheads, 45 Scrap Polymers, 135 Gun Powder, 22 Paper, 22 Yucca Fibers |

### Crossbow Bolt Kits

| Bundle | Input | Output (75%) |
| --- | --- | --- |
| Disassembled Stone Bolt Kit | 30 Stone Bolts | 22 Small Stones, 22 Wood, 22 Feathers |
| Disassembled Iron Bolt Kit | 30 Iron Bolts | 22 Iron Arrowheads, 22 Wood, 22 Feathers |
| Disassembled Steel AP Bolt Kit | 30 Steel AP Bolts | 22 Steel AP Arrowheads, 45 Scrap Polymers |
| Disassembled Flaming Bolt Kit | 30 Flaming Bolts | 22 Steel AP Arrowheads, 45 Scrap Polymers, 45 Gun Powder, 112 Cloth, 22 Animal Fat |
| Disassembled Exploding Bolt Kit | 30 Exploding Bolts | 22 Steel AP Arrowheads, 45 Scrap Polymers, 180 Gun Powder, 22 Paper, 22 Yucca Fibers |

## Installation

1. Copy the `EV_EnhancedArcheryDamage` folder into your game's `Mods/` directory
2. Restart the game or server

## Compatibility

- 7 Days to Die 1.0 (Alpha 21+)
- Server-side mod — works without client installation
- May conflict with mods that modify arrow/bolt EntityDamage values or bow/crossbow base_add damage
- Ammo refund effects are added only to vanilla arrow and bolt item names. Custom ammo from other mods needs equivalent refund XML added separately.

## Changelog

### v1.3.0

- Added XML-only ammo refund chance for vanilla arrows and crossbow bolts after projectile impact
- Refund chance scales with Archery perk level: 0/10/20/30/40/50% for levels 0-5
- Added refund support for Stone, Iron, Steel AP, Flaming, and Exploding arrows and bolts
- Added compatibility note for custom arrow/bolt ammo from other mods

### v1.2.0

- Added 10 disassembly recipes to break down 30 arrows/bolts into raw materials at 75% return
- Disassembly requires a Workbench and all 7 volumes of Ranger's Guide to Archery
- Added Localization.txt with English and Russian translations for all bundle items

### v1.1.0

- Merged TransmuteArrowsAndBolts mod — added 10 recipes to convert arrows to bolts and vice versa (1:1 ratio, no material loss)

### v1.0.0

- Initial release with enhanced damage for all arrow/bolt types and archery weapons

---

**Author:** Aleksei Khozin  
**Version:** 1.3.0  
**Website:** <https://github.com/alekho77/epic_7d2d_mods>
