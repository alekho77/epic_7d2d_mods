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

Simple, Good, and Valuable are reward categories. `Q1` to `Q6` refers to the in-game item quality.

Only non-default qualities are annotated in the table. If a table entry does not include an explicit quality annotation, it is assumed to be `Q6`.

| Group          | Simple                                      | Good                                        | Valuable                             |
| -------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------ |
| Ranged weapons | `gunHandgunT1Pistol`                        | `gunHandgunT2Magnum44`                      | `gunHandgunT3SMG5`                   |
|                | `gunShotgunT1DoubleBarrel`                  | `gunShotgunT2PumpShotgun`                   | `gunHandgunT3DesertVulture`          |
|                | `gunRifleT1HuntingRifle`                    | `gunRifleT2LeverActionRifle`                | `gunShotgunT3AutoShotgun`            |
|                | `gunMGT1AK47` (Q3)                          | `gunMGT1AK47`                               | `gunRifleT3SniperRifle`              |
|                | `gunBowT1WoodenBow`                         | `gunBowT1IronCrossbow`                      | `gunMGT2TacticalAR`                  |
|                |                                             | `gunMGT2TacticalAR` (Q3)                    | `gunMGT3M60`                         |
|                |                                             |                                             | `gunBowT3CompoundBow`                |
|                |                                             |                                             | `gunBowT3CompoundCrossbow`           |
| Melee weapons  | `meleeWpnSpearT1IronSpear` (Q3)             | `meleeWpnSpearT1IronSpear`                  | `meleeWpnSpearT3SteelSpear`          |
|                | `meleeWpnBladeT1HuntingKnife` (Q3)          | `meleeWpnBladeT3Machete` (Q3)               | `meleeWpnBladeT3Machete`             |
|                | `meleeWpnClubT1BaseballBat` (Q3)            | `meleeWpnClubT1BaseballBat`                 | `meleeWpnClubT3SteelClub`            |
|                | `meleeWpnSledgeT1IronSledgehammer` (Q3)     | `meleeWpnSpearT3SteelSpear` (Q3)            | `meleeWpnBatonT2StunBaton`           |
|                | `meleeWpnBatonT0PipeBaton`                  | `meleeWpnBatonT2StunBaton` (Q3)             | `meleeWpnSledgeT3SteelSledgehammer`  |
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
