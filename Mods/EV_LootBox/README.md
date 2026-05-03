# Loot Box

## Description

Adds a **Loot Box** — a special bundle item that opens a loot selection window with a **tiered reward system**. Each box always grants a base reward tier and can independently add higher-tier bonus rewards on top.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- **Tiered probability system** — each box always grants a common reward and can independently add uncommon and rare bonus tiers
- **Loot Box** (`evLootBox`) — single reward box with three quality tiers
- **Loot window UI** — uses the vanilla `OpenLootBundle` mechanic; opens a container window just like quest reward bundles
- **No perks or loot abundance influence** — rewards are fixed regardless of player progression
- **Server-friendly** — fully controlled by the server; admins distribute boxes via console commands

## How It Works

When a player right-clicks a **Loot Box**, the reward is built in layers:

| Tier | Probability | Contents |
| ---- | ----------- | -------- |
| 🟢 Common | Always | 2–3× Canned Sham, 3–5× Bandage, 50–100× 9mm Ball ammo |
| 🟡 Uncommon | 20% extra roll | 1–2× Meat Stew, 1–2× First Aid Kit, 50–100× 9mm HP ammo |
| 🔴 Rare | 5% extra roll | 3–5× Repair Kit, 1–2× Steroids, 2–3× Handguns Skill Magazine |

The tier selector is a `count="all"` lootgroup. The common pool is always included, while the uncommon and rare pools use independent `force_prob="true"` rolls with `prob="0.20"` and `prob="0.05"`. If a bonus roll succeeds, **all items** in that tier are added to the same loot window.

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
- Added `evLootBox` (Loot Box) with guaranteed common rewards plus 20% uncommon and 5% rare bonus rolls
- Common tier: Canned Sham, Bandage, 9mm Ball ammo
- Uncommon tier: Meat Stew, First Aid Kit, 9mm HP ammo
- Rare tier: Repair Kit, Steroids, Handguns Skill Magazine

---

**Author:** Aleksei Khozin  
**Version:** 0.1.0  
**Website:** [github.com/alekho77/epic_7d2d_mods](https://github.com/alekho77/epic_7d2d_mods)
