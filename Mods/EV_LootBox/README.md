# Loot Box

## Description

Adds a **Loot Box** — a special bundle item that opens a loot selection window with three named **reward categories**. Each box rolls exactly one category: **Simple**, **Good**, or **Valuable**.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- **Category-based probability system** — each box rolls one reward category with 75% Simple, 20% Good, and 5% Valuable odds
- **Matched weapon bonus** — the selected category also has a 30% chance to add one weapon from the same reward category
- **Loot Box** (`evLootBox`) — single reward box with three named reward categories
- **Loot window UI** — uses the vanilla `OpenLootBundle` mechanic; opens a container window just like quest reward bundles
- **No perks or loot abundance influence** — rewards are fixed regardless of player progression
- **Server-friendly** — fully controlled by the server; admins distribute boxes via console commands

## How It Works

When a player right-clicks a **Loot Box**, the reward is built from one selected category plus an optional matching weapon bonus:

Use the table below as the working template for grouped item IDs by reward category:

Simple, Good, and Valuable are reward categories. `Q1` to `Q6` refers to the in-game item quality for weapons and tools.

For weapons and tools, only non-default qualities are annotated in the table. If a weapon or tool entry does not include an explicit quality annotation, it is assumed to be `Q6`.

For food and drink entries, parentheses indicate the stack count range that should drop from the box.

| Group          | Simple                                      | Good                                        | Valuable                             |
| -------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------ |
| Food           | `foodCanBeef` (3-5)                         | `foodHoney` (1-3)                           | `foodHoneyGlazedSham` (1-3)          |
|                | `foodCanChicken` (4-6)                      | `foodMeatStew` (2-4)                        | `foodHoneyBrisket` (1-3)             |
|                | `foodCanLamb` (3-5)                         | `foodSteakAndPotato` (1-3)                  | `foodGumboStew` (2-4)                |
|                | `foodCanCatfood` (4-6)                      | `foodShamChowder` (1-3)                     | `foodShepardsPie` (1-3)              |
|                | `foodCanDogfood` (1-3)                      | `foodHoboStew` (1-3)                        |                                      |
|                | `foodCanChili` (1-3)                        | `foodFishTacos` (1-3)                       |                                      |
|                | `foodCanTuna` (3-5)                         | `foodChiliDog` (1-3)                        |                                      |
|                | `foodCanSham` (3-5)                         | `foodBlueberryPie` (2-4)                    |                                      |
|                | `foodCanPasta` (3-5)                        | `foodPumpkinPie` (2-4)                      |                                      |
|                | `foodCanSalmon` (3-5)                       | `foodSpaghetti` (1-3)                       |                                      |
|                | `foodCanMiso` (4-6)                         | `foodTunaFishGravyToast` (1-3)              |                                      |
|                | `foodCanPeas` (3-5)                         |                                             |                                      |
|                | `foodCanPears` (4-6)                        |                                             |                                      |
|                | `foodCanSoup` (4-6)                         |                                             |                                      |
|                | `foodCanStock` (3-5)                        |                                             |                                      |
|                | `foodCornOnTheCob` (4-6)                    |                                             |                                      |
|                | `foodCornBread` (4-6)                       |                                             |                                      |
|                | `foodGrilledMeat` (4-6)                     |                                             |                                      |
|                | `foodBoiledMeat` (3-5)                      |                                             |                                      |
|                | `foodBakedPotato` (4-6)                     |                                             |                                      |
|                | `foodPumpkinBread` (3-5)                    |                                             |                                      |
|                | `foodEggBoiled` (4-6)                       |                                             |                                      |
|                | `foodBaconAndEggs` (2-4)                    |                                             |                                      |
|                | `foodVegetableStew` (1-3)                   |                                             |                                      |
| Drinks         | `drinkJarYuccaJuice` (1-3)                  | `drinkJarPureMineralWater` (2-4)            | `drinkJarHoneyTea` (2-4)             |
|                | `drinkJarGoldenRodTea` (2-4)                | `drinkJarRedTea` (2-3)                      | `drinkJarBlackStrapCoffee` (1-3)     |
|                | `drinkJarCoffee` (1-3)                      |                                             |                                      |
|                | `drinkJarBoiledWater` (5-7)                 |                                             |                                      |
| Ranged weapons | `gunHandgunT1Pistol`                        | `gunHandgunT2Magnum44`                      | `gunHandgunT3SMG5`                   |
|                | `gunShotgunT1DoubleBarrel`                  | `gunShotgunT2PumpShotgun`                   | `gunHandgunT3DesertVulture`          |
|                | `gunRifleT1HuntingRifle`                    | `gunRifleT2LeverActionRifle`                | `gunShotgunT3AutoShotgun`            |
|                | `gunMGT1AK47` (Q2)                          | `gunMGT1AK47`                               | `gunRifleT3SniperRifle`              |
|                | `gunBowT1WoodenBow`                         | `gunBowT1IronCrossbow`                      | `gunMGT2TacticalAR`                  |
|                |                                             | `gunMGT2TacticalAR` (Q2)                    | `gunMGT3M60`                         |
|                |                                             |                                             | `gunBowT3CompoundBow`                |
|                |                                             |                                             | `gunBowT3CompoundCrossbow`           |
| Melee weapons  | `meleeWpnSpearT1IronSpear` (Q2)             | `meleeWpnSpearT1IronSpear`                  | `meleeWpnSpearT3SteelSpear`          |
|                | `meleeWpnBladeT1HuntingKnife` (Q2)          | `meleeWpnBladeT3Machete` (Q2)               | `meleeWpnBladeT3Machete`             |
|                | `meleeWpnClubT1BaseballBat` (Q2)            | `meleeWpnClubT1BaseballBat`                 | `meleeWpnClubT3SteelClub`            |
|                | `meleeWpnSledgeT1IronSledgehammer` (Q2)     | `meleeWpnSpearT3SteelSpear` (Q2)            | `meleeWpnBatonT2StunBaton`           |
|                | `meleeWpnBatonT0PipeBaton`                  | `meleeWpnBatonT2StunBaton` (Q2)             | `meleeWpnSledgeT3SteelSledgehammer`  |
|                | `meleeWpnKnucklesT0LeatherKnuckles`         | `meleeWpnBladeT1HuntingKnife`               | `meleeWpnKnucklesT3SteelKnuckles`    |
|                |                                             | `meleeWpnSledgeT1IronSledgehammer`          |                                      |
|                |                                             | `meleeWpnKnucklesT1IronKnuckles`            |                                      |
| Tools          | `meleeToolRepairT0TazasStoneAxe`            | `meleeToolRepairT3Nailgun` (Q2)             | `meleeToolRepairT3Nailgun`           |
|                | `meleeToolRepairT1ClawHammer`               | `meleeToolAxeT2SteelAxe`                    | `meleeToolAxeT3Chainsaw`             |
|                | `meleeToolAxeT1IronFireaxe`                 | `meleeToolPickT2SteelPickaxe`               | `meleeToolPickT3Auger`               |
|                | `meleeToolPickT1IronPickaxe`                | `meleeToolShovelT2SteelShovel`              | `meleeToolSalvageT3ImpactDriver`     |
|                | `meleeToolShovelT1IronShovel`               | `meleeToolSalvageT2Ratchet`                 |                                      |
|                | `meleeToolSalvageT1Wrench`                  |                                             |                                      |

The reward-category selector is a `count="1"` lootgroup with weighted entries. Each use of the box picks exactly one category: `Simple` with weight `75`, `Good` with weight `20`, or `Valuable` with weight `5`. The base consumables in that category are guaranteed, and then the matching weapon group rolls at `30%`. If that bonus roll succeeds, one weapon from the same reward category is added to the same loot window.

## Installation

1. Copy the `EV_LootBox` folder into your `7 Days to Die/Mods/` directory.
2. Restart the game or server.
3. Distribute boxes to players via the admin console:

```text
giveself evLootBox 1
give <player_name> evLootBox 1
```

## Compatibility

- **Game Version:** 7 Days to Die (latest stable)
- **Type:** XML modlet — no Harmony patches, no DLL, no Unity assets
- **Multiplayer:** Server-side only — clients do not need this mod installed

## Changelog

### v0.1.0

- Initial prototype release with mutually exclusive 75% Simple, 20% Good, and 5% Valuable category rolls plus a 30% matching weapon bonus

---

**Author:** Aleksei Khozin  
**Version:** 0.1.0  
**Website:** [github.com/alekho77/epic_7d2d_mods](https://github.com/alekho77/epic_7d2d_mods)
