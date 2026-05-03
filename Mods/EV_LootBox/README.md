# Loot Box

## Description

Adds a **Loot Box** — a special bundle item that opens a loot selection window with a **tiered reward system**. Each box always grants a **Simple** reward tier and can independently add **Good** and **Quality** bonus rewards on top.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- **Tiered probability system** — each box always grants a Simple reward and can independently add Good and Quality bonus tiers
- **Loot Box** (`evLootBox`) — single reward box with three named tiers
- **Loot window UI** — uses the vanilla `OpenLootBundle` mechanic; opens a container window just like quest reward bundles
- **No perks or loot abundance influence** — rewards are fixed regardless of player progression
- **Server-friendly** — fully controlled by the server; admins distribute boxes via console commands

## How It Works

When a player right-clicks a **Loot Box**, the reward is built in layers:

Use the table below as the working list of item IDs for each tier:

| Simple Items               | Good Items              | Quality Items              |
| -------------------------- | ----------------------- | -------------------------- |
| `foodCanPeas`              | `foodMeatStew`          | `resourceRepairKit`        |
| `foodCanSoup`              | `medicalFirstAidKit`    | `drugSteroids`             |
| `foodCanSham`              | `ammo9mmBulletHP`       | `handgunsSkillMagazine`    |
| `foodCanChicken`           |                         |                            |
| `foodCanChili`             |                         |                            |
| `foodCanBeef`              |                         |                            |
| `foodCanTuna`              |                         |                            |
| `foodCanPasta`             |                         |                            |
| `foodCornBread`            |                         |                            |
| `foodGrilledMeat`          |                         |                            |
| `foodEggBoiled`            |                         |                            |
| `foodBakedPotato`          |                         |                            |
| `drinkJarBoiledWater`      |                         |                            |
| `drinkJarYuccaJuice`       |                         |                            |
| `drinkJarGoldenRodTea`     |                         |                            |
| `drinkJarBeer`             |                         |                            |
| `medicalBandage`           |                         |                            |
| `medicalAloeCream`         |                         |                            |
| `medicalFirstAidBandage`   |                         |                            |
| `drugVitamins`             |                         |                            |
| `drugPainkillers`          |                         |                            |
| `ammo9mmBulletBall`        |                         |                            |
|                            |                         |                            |
|                            |                         |                            |

The tier selector is a `count="all"` lootgroup. The Simple pool is always included, while the Good and Quality pools use independent `force_prob="true"` rolls with `prob="0.20"` and `prob="0.05"`. If a bonus roll succeeds, **all items** in that tier are added to the same loot window.

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

- Initial prototype release
- Added `evLootBox` (Loot Box) with guaranteed Simple rewards plus 20% Good and 5% Quality bonus rolls
- Simple tier: Canned Sham, Bandage, 9mm Ball ammo
- Good tier: Meat Stew, First Aid Kit, 9mm HP ammo
- Quality tier: Repair Kit, Steroids, Handguns Skill Magazine

---

**Author:** Aleksei Khozin  
**Version:** 0.1.0  
**Website:** [github.com/alekho77/epic_7d2d_mods](https://github.com/alekho77/epic_7d2d_mods)
