# ZZ_EV_ProjectZCash — EpicCash Recipes for Project Z

## Description

Adds **Epic Bucks** crafting recipes for content from the **[Project Z](https://7dtdprojectz.com/)** modpack. Players can spend Epic Bucks (`evCash`) to craft rare weapon bundles added by `Z_RareItems`, turning the EpicCash economy into a gateway to Project Z's rare gear.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

<!-- -->

> ### ⚠️ Requires Two Base Mods
>
> This modlet is an **add-on** and does nothing on its own. It requires both base mods to be installed and loaded before it:
>
> 1. **[EV_EpicCash](https://github.com/alekho77/epic_7d2d_mods)** — provides the `evCash` currency used as the ingredient for all recipes.
> 2. **[Project Z](https://7dtdprojectz.com/)** — specifically the `Z_RareItems` submod, which defines the rare weapon bundles this mod unlocks for crafting.
>
> The `ZZ_` folder prefix ensures the mod is loaded **after** `EV_*` and `Z_*` mods (7D2D loads mods alphabetically by folder name), so all referenced items already exist when recipes are registered.

## Features

- **12 Rare Weapon Recipes** — craft random Tier 6 rare variants of Project Z weapons for Epic Bucks
- **Always Unlocked** — no schematic or perk level required
- **Inventory Crafting** — no workstation needed
- **Impact-Based Pricing** — aligned with the EpicCash v1.2.2 pricing model

## Included Recipes

Each bundle yields **one random rare variant** (Quality 6) of the weapon with a unique passive bonus (headshot multiplier, knockdown, vampirism, fast reload, etc.) rolled from the Project Z rare pool.

### 🎯 Ranged Weapons

| Bundle | Variants | Price |
| --- | --- | ---: |
| Rare Sniper Rifle | Crusher / Unkillable / Knockdown / Stable | 55 EB |
| Rare Auto Shotgun | Crusher / Unkillable / Snowstorm / Universal | 55 EB |
| Rare M60 Machine Gun | Snowstorm / Universal / Unkillable / Stable | 75 EB |
| Rare SMG-5 | Snowstorm / Unkillable / Stable / Universal | 65 EB |
| Rare Desert Vulture | Experienced / Universal / Knockdown / Vampire | 55 EB |
| Rare Archery | Compound Bow / Crossbow × Robinhood / Ninja / Vampire | 50 EB |

### ⚔️ Melee Weapons

| Bundle | Variants | Price |
| --- | --- | ---: |
| Rare Steel Spear (T3) | Awl / Convenient / Universal | 45 EB |
| Rare Steel Club (T3) | Experienced / Universal / Unkillable | 45 EB |
| Rare Steel Sledgehammer (T3) | Champion / Convenient / Vampire | 45 EB |
| Rare Steel Knuckles (T3) | Awl / Convenient / Experienced / Butcher | 45 EB |
| Rare Machete (T3) | Convenient / Unkillable / Universal | 45 EB |
| Rare Stun Baton (T3) | Convenient / Unkillable / Experienced | 50 EB |

## Installation

1. Install **EV_EpicCash** — copy `EV_EpicCash` into your `7 Days to Die/Mods/` directory.
2. Install **Project Z** — at minimum the `Z_RareItems` submod must be present in `Mods/`.
3. Copy the **ZZ_EV_ProjectZCash** folder into the same `Mods/` directory.
4. Restart the game or server.

## Compatibility

- **Game Version:** 7 Days to Die (latest stable)
- **Type:** XML modlet (recipes only — no items, no buffs, no Harmony)
- **Multiplayer:** Server-side only — clients do not need this mod installed.
- **Load Order:** The `ZZ_` prefix forces this mod to load after both `EV_*` and `Z_*` mods, which is required because recipes reference items defined in both.

## Changelog

### v0.1.0

- Initial release with 12 Project Z rare weapon bundle recipes (6 ranged + 6 melee)

## Credits

- **Base currency mod:** [EV_EpicCash](https://github.com/alekho77/epic_7d2d_mods) by Aleksei Khozin
- **Base content mod:** [Project Z](https://7dtdprojectz.com/) by BlackRabbit — specifically the `Z_RareItems` submod
- **Author:** Aleksei Khozin
- **Community:** [EpicVales Steam Group](https://steamcommunity.com/groups/EpicVales)

---

**Author:** Aleksei Khozin\
**Version:** 0.1.0\
**Website:** [https://github.com/alekho77/epic_7d2d_mods](https://github.com/alekho77/epic_7d2d_mods)
