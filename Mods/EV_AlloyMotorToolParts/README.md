# Alloy Motor Tool Parts

## Description

Adds **Alloy Motor Tool Parts (Tier A)** — an upgraded tier of motor tool parts crafted from regular chainsaw parts, a silver nugget, and forged steel. Part of a planned multi-tier tool upgrade system for the EpicVales server community.

## Features

- New craftable item: Alloy Motor Tool Parts (Tier A)
- Server-side mod — no mandatory client installation for basic functionality
- Reuses existing game icon with a custom steel-blue color tint (`7A8C9E`)
- Balanced economic value calculated as 2× ingredient cost (EconomicValue: 1400)

## Crafting Recipe

| Ingredient | Quantity |
|---|---|
| Motor Tool Parts (regular) | 1 |
| Silver Nugget | 1 |
| Forged Steel | 5 |

**Crafting Station:** Workbench  
**Craft Time:** 60 seconds

## Unlock Requirements

The recipe is locked behind the **Salvage Tools** progression line (Scrapping 4 Fun magazines):

- Unlocks at **level 76** of the Salvage Tools skill
- The mod raises the vanilla Salvage Tools cap from **75 → 100** to make the unlock achievable
- A dedicated "Industrial Parts: Tier A" entry appears in the Salvage Tools progression tab
- The UI shows a lock icon and requirements until level 76 is reached

## Installation

1. Copy the `EV_AlloyMotorToolParts` folder into your game's `Mods/` directory
2. Restart the game or server

> **Note on Progression UI:** The `progression.xml` file is NOT synced to clients automatically. For players to see the correct lock icons and unlock requirements in the progression menu, they need to install the mod locally as well. Without it, the recipe will appear as "available" in the UI but will still be locked server-side until 76 magazines are read.

## Compatibility

- 7 Days to Die 1.0 (Alpha 21+)
- Server and single-player compatible
- May conflict with mods that modify the Salvage Tools progression cap or the `craftingSalvageTools` skill tree

## Planned Development

This mod is the first part of an advanced tool parts system:

- **Tier A** (Alloy Steel) — this mod ✅
- **Tier AAA** (Composite) — planned
- **Tier S** (Diamond) — planned

## Technical Details

- **Unlock tag:** `mtPartsA_Alloy_unlock`
- **Progression:** Linked to `craftingSalvageTools` (level 76+)
- **Cap change:** Raises `max_level` of Salvage Tools from 75 to 100

### Mod Files

| File | Purpose |
|---|---|
| `items.xml` | Item definition with recolored icon |
| `recipes.xml` | Crafting recipe with unlock tag |
| `progression.xml` | Progression system, cap increase, and UI display entry |
| `Localization.txt` | English and Russian localization |

## Changelog

### v1.0.0
- Initial release with Tier A Alloy Motor Tool Parts
- Salvage Tools cap raised to 100
- Full progression UI integration

---

**Author:** Aleksei Khozin  
**Version:** 1.0.0  
**Website:** https://alekho77.github.io/epic_7d2d_mods/
