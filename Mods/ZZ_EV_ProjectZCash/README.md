# ZZ_EV_ProjectZCash — EpicCash Recipes for Project Z

## Description

Adds **Epic Bucks** crafting recipes for content from the **[Project Z](https://7dtdprojectz.com/)** modpack. Players can spend Epic Bucks (`evCash`) to craft item bundles added by Project Z submods, turning the EpicCash economy into a gateway to Project Z's extended content. New bundle categories are added over time.

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
> 2. **[Project Z](https://7dtdprojectz.com/)** — provides the items referenced by each recipe. Only the Project Z submods relevant to the currently added recipes are strictly required (see the *Included Recipes* section below).
>
> The `ZZ_` folder prefix ensures the mod is loaded **after** `EV_*` and `Z_*` mods (7D2D loads mods alphabetically by folder name), so all referenced items already exist when recipes are registered.

## Features

- **24 Project Z Recipes** — 12 rare weapons, 2 rare tools, and 10 legendary unique weapons
- **Always Unlocked** — no schematic or perk level required
- **Inventory Crafting** — no workstation needed
- **Tiered Pricing** — rare gear in the 45–75 EB range, legendary gear priced very high (200–350 EB) to prevent instant end-game

## Included Recipes

### Rare Weapons (from `Z_RareItems`)

Each bundle yields **one random rare variant** (Quality 6) of the weapon with a unique passive bonus (headshot multiplier, knockdown, vampirism, fast reload, etc.) rolled from the Project Z rare pool.

#### 🎯 Ranged Weapons

| Bundle | Variants | Price |
| --- | --- | ---: |
| Rare Sniper Rifle | Crusher / Unkillable / Knockdown / Stable | 55 EB |
| Rare Auto Shotgun | Crusher / Unkillable / Snowstorm / Universal | 55 EB |
| Rare M60 Machine Gun | Snowstorm / Universal / Unkillable / Stable | 75 EB |
| Rare SMG-5 | Snowstorm / Unkillable / Stable / Universal | 65 EB |
| Rare Desert Vulture | Experienced / Universal / Knockdown / Vampire | 55 EB |
| Rare Archery | Compound Bow / Crossbow × Robinhood / Ninja / Vampire | 50 EB |

#### ⚔️ Melee Weapons

| Bundle | Variants | Price |
| --- | --- | ---: |
| Rare Steel Spear (T3) | Awl / Convenient / Universal | 45 EB |
| Rare Steel Club (T3) | Experienced / Universal / Unkillable | 45 EB |
| Rare Steel Sledgehammer (T3) | Champion / Convenient / Vampire | 45 EB |
| Rare Steel Knuckles (T3) | Awl / Convenient / Experienced / Butcher | 45 EB |
| Rare Machete (T3) | Convenient / Unkillable / Universal | 45 EB |
| Rare Stun Baton (T3) | Convenient / Unkillable / Experienced | 50 EB |

#### 🔧 Tools

| Bundle | Variants | Price |
| --- | --- | ---: |
| Rare Auger | Metalist / Mason / Digger / Unkillable | 55 EB |
| Rare Chainsaw | Lumberjack / Unkillable | 50 EB |

### Legendary Unique Weapons (from `Z_Master_Skills`)

End-game named weapons above the Rare tier (unique model, bronze `#C27E53` tint, powerful legendary passives). Each bundle yields **one random legendary variant** at Quality 6. Prices are intentionally set very high so that a single purchase does not act as a shortcut to full end-game gear.

#### 🎯 Ranged Weapons (Legendary)

| Bundle | Class | Variants | Price |
| --- | --- | --- | ---: |
| Unique Buldog | M60-class (7.62 mm) | Arsonist / URANUS / Breeze / Unkillable / Avenger / Berserk | 350 EB |
| Unique Eraser | Auto Shotgun | Arsonist / URANUS / Unkillable / Avenger / Berserk | 300 EB |
| Unique Gaus | Sniper Rifle | Arsonist / Tesla / URANUS / Unkillable | 300 EB |
| Unique Zinger | SMG-5 | Arsonist / URANUS / Breeze / Unkillable / Avenger / Berserk | 300 EB |

#### ⚔️ Melee Weapons (Legendary)

| Bundle | Class | Variants | Price |
| --- | --- | --- | ---: |
| Unique Combistick | Spear | Crisis / Crusher / Masterpiece / Guardian / Surgeon | 200 EB |
| Unique Barbarian | Axe | Crisis / Crusher / Masterpiece / Guardian | 200 EB |
| Unique Destructor | Sledgehammer | Crisis / Crusher / Masterpiece / Guardian | 200 EB |
| Unique Maus Claws | Knuckles | Crisis / Crusher / Masterpiece / Guardian / Surgeon | 200 EB |
| Unique Indiana | Machete | Crisis / Crusher / Masterpiece / Guardian / Surgeon | 200 EB |
| Unique Flugen | Stun Baton | Crisis / Crusher / Masterpiece / Guardian | 200 EB |

## Installation

1. Install **EV_EpicCash** — copy `EV_EpicCash` into your `7 Days to Die/Mods/` directory.
2. Install **Project Z** — at minimum every submod referenced by the recipes listed above must be present in `Mods/`.
3. Copy the **ZZ_EV_ProjectZCash** folder into the same `Mods/` directory.
4. Restart the game or server.

## Compatibility

- **Game Version:** 7 Days to Die (latest stable)
- **Type:** XML modlet (recipes only — no items, no buffs, no Harmony)
- **Multiplayer:** Server-side only — clients do not need this mod installed.
- **Load Order:** The `ZZ_` prefix forces this mod to load after both `EV_*` and `Z_*` mods, which is required because recipes reference items defined in both.

## Changelog

### v0.2.0

- Added 2 rare tool bundle recipes from `Z_RareItems`: Auger (55 EB), Chainsaw (50 EB)
- Added 10 legendary unique weapon bundle recipes from `Z_Master_Skills`: 4 ranged (300–350 EB) + 6 melee (200 EB each)

### v0.1.0

- Initial release with 12 Project Z rare weapon bundle recipes (6 ranged + 6 melee)

## Credits

- **Base currency mod:** [EV_EpicCash](https://github.com/alekho77/epic_7d2d_mods) by Aleksei Khozin
- **Base content mod:** [Project Z](https://7dtdprojectz.com/) by BlackRabbit
- **Author:** Aleksei Khozin
- **Community:** [EpicVales Steam Group](https://steamcommunity.com/groups/EpicVales)

---

**Author:** Aleksei Khozin\
**Version:** 0.2.0\
**Website:** [https://github.com/alekho77/epic_7d2d_mods](https://github.com/alekho77/epic_7d2d_mods)
