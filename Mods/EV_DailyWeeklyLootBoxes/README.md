# Daily & Weekly Loot Boxes

## Description

Adds **Daily** and **Weekly Loot Boxes** — special bundle items that open a loot selection window with a **tiered reward system**. Each box is randomly assigned one of three reward tiers when opened, keeping every day's reward a surprise.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- **Tiered probability system** — each box draws from one of three tiers using weighted random selection
- **Daily Loot Box** (`evDailyLootBundle`) — lightweight daily reward with three quality tiers
- **Loot window UI** — uses the vanilla `OpenLootBundle` mechanic; opens a container window just like quest reward bundles
- **No perks or loot abundance influence** — rewards are fixed regardless of player progression
- **Server-friendly** — fully controlled by the server; admins distribute boxes via console commands

## How It Works

When a player right-clicks a **Daily Loot Box**, the game rolls a single weighted random draw against the three tiers:

| Tier | Probability | Contents |
| ---- | ----------- | -------- |
| 🟢 Common | 75% | 2–3× Canned Sham, 3–5× Bandage, 50–100× 9mm Ball ammo |
| 🟡 Uncommon | 20% | 1–2× Meat Stew, 1–2× First Aid Kit, 50–100× 9mm HP ammo |
| 🔴 Rare | 5% | 3–5× Repair Kit, 1–2× Steroids, 2–3× Handguns Skill Magazine |

The tier selector is a `count="1"` lootgroup with relative `prob` weights (75 / 20 / 5). Once a tier is selected, **all items** in that tier are given to the player — the result is shown in a loot window identical to vanilla quest reward bundles.

## Installation

1. Copy the `EV_DailyWeeklyLootBoxes` folder into your `7 Days to Die/Mods/` directory.
2. Restart the game or server.
3. Distribute boxes to players via the admin console:

```text
giveself evDailyLootBundle 1
give <player_name> evDailyLootBundle 1
```

## Compatibility

- **Game Version:** 7 Days to Die (latest stable)
- **Type:** XML modlet — no Harmony patches, no DLL, no Unity assets
- **Multiplayer:** Server-side only — clients do not need this mod installed

## Changelog

### v0.1.0

- Initial prototype release
- Added `evDailyLootBundle` (Daily Loot Box) with three reward tiers (75 / 20 / 5%)
- Common tier: Canned Sham, Bandage, 9mm Ball ammo
- Uncommon tier: Meat Stew, First Aid Kit, 9mm HP ammo
- Rare tier: Repair Kit, Steroids, Handguns Skill Magazine

---

**Author:** Aleksei Khozin  
**Version:** 0.1.0  
**Website:** [github.com/alekho77/epic_7d2d_mods](https://github.com/alekho77/epic_7d2d_mods)
