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

- **59 Project Z Recipes** — 12 rare weapons, 2 rare tools, 10 legendary unique weapons, 9 Improved armor sets, 5 Legendary named armor sets, 11 Improved weapons, 4 Improved power tools, 2 Improved robotics drones, and 4 Depleted Uranium ammo crates
- **Always Unlocked** — no schematic or perk level required
- **Inventory Crafting** — no workstation needed
- **Tiered Pricing** — Depleted Uranium ammo crates at 6 EB each, rare gear in the 45–75 EB range, Improved weapons/tools in the 75–180 EB range, Improved armor sets in the 150–200 EB range, Legendary weapons and armor sets priced very high (200–380 EB) to prevent instant end-game

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

### Improved Armor Sets (from `Z_Armor_Improved`)

Full 4-piece Quality 6 "Improved" armor sets. Each `Improved` piece is significantly stronger than its vanilla Quality 6 counterpart (higher physical/elemental resist, extra mod slots, class-specific passive bonuses) and normally requires the `MasterArmor` perk and the Improved Workbench to craft, so bundles are priced between Rare weapons and Legendary weapons.

| Bundle | Class | Armor Type | Price |
| --- | --- | --- | ---: |
| Rogue Improved Armor Set | Rogue | Light | 150 EB |
| Gatherer Improved Armor Set | Gatherer | Heavy (Project Z exclusive) | 150 EB |
| Nomad Improved Armor Set | Nomad | Medium | 150 EB |
| Nerd Improved Armor Set | Nerd | Light | 150 EB |
| Ranger Improved Armor Set | Ranger | Medium | 170 EB |
| Assassin Improved Armor Set | Assassin | Medium | 170 EB |
| Commando Improved Armor Set | Commando | Medium | 180 EB |
| Enforcer Improved Armor Set | Enforcer | Heavy | 200 EB |
| Raider Improved Armor Set | Raider | Heavy | 200 EB |

### Legendary Named Armor Sets (from `Z_Master_Skills`)

End-game named armor sets with a gold `#FFB800` tint. Each set grants a unique **full-set bonus buff** (e.g. `buffPredatorSetBonus`, `buffSonnySetBonus`) when all 4 pieces of the same class are equipped simultaneously. Normally crafted only at the Improved Workbench with the `MasterArmor` perk. Each bundle yields the full 4-piece set at Quality 6.

| Bundle | Class | Armor Type | Price |
| --- | --- | --- | ---: |
| Rescuer Legendary Armor Set | Rescuer | Light | 300 EB |
| Predator Legendary Armor Set | Predator | Medium | 320 EB |
| Plunderer Legendary Armor Set | Plunderer | Medium | 320 EB |
| Sonny Legendary Armor Set | Sonny | Heavy (premium) | 380 EB |
| Maus Legendary Armor Set | Maus | Heavy (premium) | 380 EB |

### Improved Weapons & Tools (from `Z_Master_Skills`)

Deterministic Quality 6 "Improved" weapons, tools, and drones (tint `#8692FF`). Normally gated behind the `MasterWeapons` / `MasterTools` perks and the Improved Workbench.

#### 🎯 Improved Ranged Weapons

| Bundle | Price |
| --- | ---: |
| Improved M60 Machine Gun | 140 EB |
| Improved Auto Shotgun | 120 EB |
| Improved Sniper Rifle | 120 EB |
| Improved SMG-5 | 120 EB |
| Improved Compound Bow | 90 EB |
| Improved Compound Crossbow | 90 EB |

#### ⚔️ Improved Melee Weapons

| Bundle | Price |
| --- | ---: |
| Improved Steel Spear | 90 EB |
| Improved Steel Club | 90 EB |
| Improved Steel Sledgehammer | 90 EB |
| Improved Steel Knuckles | 90 EB |
| Improved Machete | 90 EB |

#### 🔧 Improved Power Tools

| Bundle | Price |
| --- | ---: |
| Improved Chainsaw | 75 EB |
| Improved Auger | 90 EB |
| Improved Impact Driver | 90 EB |
| Improved Nailgun | 140 EB |

#### 🤖 Improved Robotics

| Bundle | Price |
| --- | ---: |
| Improved Junk Sledge Drone | 180 EB |
| Improved Junk Turret Drone | 180 EB |

### Depleted Uranium Ammo (from `Z_Master_Skills`)

Experimental [5AFF75]Depleted Uranium[-] rounds — armor-ignoring, multi-target penetrating ammunition that normally cannot be crafted and is obtainable only from boss loot or the in-game support radio system. These bundles provide a paid alternative via Epic Bucks and appear under **Ammo/Weapons → Ammo** in the inventory crafting tabs.

| Bundle | Rounds | Price |
| --- | ---: | ---: |
| 9mm DU Ammo Crate | 1500 | 6 EB |
| 7.62mm DU Ammo Crate | 1000 | 6 EB |
| .44 Magnum DU Ammo Crate | 1250 | 6 EB |
| Shotgun DU Ammo Crate | 1000 | 6 EB |

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

### v1.1.0

- Added **4 Depleted Uranium ammo bundle recipes** from the `Z_Master_Skills` submod: 9mm (1500 rounds), 7.62mm (1000 rounds), .44 Magnum (1250 rounds), and shotgun shells (1000 rounds) — all priced at a flat **6 EB** each
- DU rounds cannot normally be crafted and only drop from bosses or via the radio support system; these bundles make them reliably purchasable with Epic Bucks
- Bundles are grouped under **Ammo/Weapons → Ammo** and use the Depleted Uranium tint (`#5AFF75`) to match the Project Z convention
- Added English and Russian localization strings for the new bundles

### v1.0.0

- **First stable release.** Promoted the modlet from pre-release (0.x) to its first release version with no content changes relative to 0.6.0 — the full 55-recipe Project Z catalogue is now considered feature-complete and API-stable for EpicCash integration.

### v0.6.0

- Added **17 Improved Weapon/Tool/Drone bundle recipes** from the `Z_Master_Skills` submod: 6 ranged weapons (M60, Auto Shotgun, Sniper Rifle, SMG-5, Compound Bow, Compound Crossbow), 5 melee weapons (Steel Spear / Club / Sledgehammer / Knuckles / Machete), 4 power tools (Chainsaw, Auger, Impact Driver, Nailgun), and 2 robotics drones (Junk Sledge, Junk Turret)
- Each bundle yields a deterministic Quality 6 `Improved` piece — priced **75–180 EB** depending on role (bows cheapest, drones and Nailgun most expensive)
- New bundles are grouped under their appropriate inventory tabs (**Ammo/Weapons → Ranged/Melee/Robotics**, **Tools/Traps**) and use the Improved-tint (`#8692FF`) convention
- Added English and Russian localization strings for the new bundles

### v0.5.0

- Added **5 Legendary Named Armor bundle recipes** from the `Z_Master_Skills` submod: Rescuer (Light, 300 EB), Predator (Medium, 320 EB), Plunderer (Medium, 320 EB), Sonny (Heavy, 380 EB), Maus (Heavy, 380 EB)
- Each bundle yields a full 4-piece Quality 6 set (helmet, outfit, gloves, boots) and triggers the corresponding class-specific **full-set bonus buff** when all four pieces are equipped
- Bundles use the gold tint (`#FFB800`) matching Project Z's convention for legendary named gear
- Added English and Russian localization strings for the new bundles

### v0.4.0

- Added **9 Improved Armor bundle recipes** from the `Z_Armor_Improved` submod, each yielding a full 4-piece Quality 6 set (helmet, outfit, gloves, boots) for one of the nine armor classes: Rogue, Gatherer, Nomad, Nerd, Ranger, Assassin, Commando, Enforcer, Raider
- Tiered pricing for the new armor sets: **150 EB** (Rogue / Gatherer / Nomad / Nerd), **170 EB** (Ranger / Assassin), **180 EB** (Commando), **200 EB** (Enforcer / Raider) — positioned between Rare weapons and Legendary weapons
- Added `Localization.txt` with English and Russian strings for the new bundle display names and descriptions
- Bundles are grouped under **Clothing/Armor** and use the Improved-tint (`#8692FF`) visual convention from Project Z

### v0.3.0

- Project Z bundle recipes now appear in the inventory crafting tabs alongside vanilla recipes — ranged weapon bundles show up under **Ammo/Weapons → Ranged Weapons**, melee bundles under **Ammo/Weapons → Melee Weapons**, and rare tool bundles under **Tools/Traps** (previously hidden because the source Project Z items used the custom `DonateWeapons` / `DonateMelee` / `DonateTools` groups that are not bound to any inventory tab)
- All recipes now use the standard vanilla `packMuleCrafting` tag, so they are properly scoped by the Pack Mule crafting-time perk like every other inventory recipe
- Crafting time raised from 1 → **2 seconds** for every recipe — still quick, but noticeable enough to prevent accidental mass-crafting

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
**Version:** 1.1.0\
**Website:** [https://github.com/alekho77/epic_7d2d_mods](https://github.com/alekho77/epic_7d2d_mods)
