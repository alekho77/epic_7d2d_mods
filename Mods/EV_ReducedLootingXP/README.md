# Reduced Looting XP

## Description

Reduces XP gained from opening untouched loot containers to **approximately 20% of vanilla**, rebalancing progression toward combat and survival gameplay.

In vanilla 7 Days to Die, opening an untouched loot container awards XP equal to the player's current game stage. World-placed containers (crates, safes, fridges) grant this XP on first open. Players who focus on aggressive POI runs, blood moon looting, and systematic container farming can level disproportionately fast compared to players who progress mainly through combat. This mod reduces container XP while leaving kill XP, loot tables, and bag spawning behavior unchanged.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- Reduces XP from opening untouched world containers to approximately 20% of vanilla
- The looting XP branch stays enabled — it is rebalanced, not removed
- All other XP sources (kills, crafting, quests, selling, harvesting, upgrading) remain completely unchanged
- Loot quality, loot quantity, scavenging speed, and Lucky Looter perk are **not** affected
- Player chests, secure storage, and dropped player backpacks are excluded from looting XP by the game engine and are unaffected by this mod

## How It Works

The game calculates looting XP for untouched non-player containers as follows:

- Looting XP is awarded on first open of an untouched non-player container
- Looting XP normally scales with your current game stage and the server XP setting
- This mod reduces that reward to roughly one-fifth of the normal value
- The exact XP you see is still rounded down by the game, so some game stages land just below the next whole number

> **Why `-0.799` and not `-0.8`?** A slightly adjusted value is used so the in-game thresholds line up with the intended results more reliably after the game applies its own rounding.

At the default XPMultiplier of 100:

| Game Stage | Vanilla XP | With this mod |
|:----------:|:----------:|:-------------:|
| 5          | 5          | 1             |
| 10         | 10         | 2             |
| 27         | 27         | 5             |
| 50         | 50         | 10            |
| 100        | 100        | 20            |

## Installation

1. Copy the `EV_ReducedLootingXP` folder into your `7 Days to Die/Mods/` directory.
2. Restart the game or server.

## Compatibility

- 7 Days to Die 1.0 (b313) and later
- Server-side mod — works without client installation
- May conflict with mods that modify `PlayerExpGain` on the `playerMale` entity class

### Large Modpacks and Overhauls

Some large overhaul modpacks and total-conversion mods already tune the looting XP branch independently. When they are installed together with this mod the `perc_add` values stack and the final XP will differ from the table above — it could be higher or lower depending on what the other mod adds.

Before combining this mod with a large modpack, search the other mod's `Config/` files for the following patterns:

- `PlayerExpGain` with `tags="Looting"` — directly modifies the same branch as this mod
- Untagged `PlayerExpGain` effects — apply to all XP branches including looting
- `buffStatusCheck02` — a vanilla always-active player status buff that overhauls commonly append their XP modifiers to

If any of these are present, the two mods need a compatibility patch to produce a predictable looting XP value.

### Companion Mod

Works well alongside [**EV_RemoveTraderXP**](https://github.com/alekho77/epic_7d2d_mods), which completely removes XP from selling items to traders. Together, the two mods close the two most common non-combat XP exploits and shift the progression curve decisively toward zombie killing, crafting, and questing.

## Changelog

### v1.0.0

- Initial release — reduces XP from opening untouched loot containers to approximately 20% of vanilla via `perc_add -0.799`

---

**Author:** Aleksei Khozin
**Version:** 1.0.0
**Website:** <https://github.com/alekho77/epic_7d2d_mods>
