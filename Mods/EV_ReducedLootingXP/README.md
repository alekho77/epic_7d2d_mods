# Reduced Looting XP

## Description

Reduces XP gained from opening untouched loot containers to **20% of vanilla**, rebalancing progression toward combat and survival gameplay.

In vanilla 7 Days to Die, opening an untouched loot container awards XP proportional to the player's current game stage. Both world-placed containers (crates, safes, fridges) and zombie drop bags award XP on first open — bags spawn untouched and use the same XP code path as world containers. Players who focus on aggressive POI runs, blood moon looting, and systematic container farming can level disproportionately fast compared to players who progress mainly through combat. This mod reduces container XP while leaving kill XP, loot tables, and bag spawning behavior unchanged.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- Reduces untouched container XP (world containers and zombie drop bags) to 20% of vanilla — effective rate changes from `gameStage × (XPMultiplier/100)` to `gameStage × (XPMultiplier/100) × 0.2`
- The looting XP branch stays enabled — it is rebalanced, not removed
- All other XP sources (kills, crafting, quests, selling, harvesting, upgrading) remain completely unchanged
- Loot quality, loot quantity, scavenging speed, and Lucky Looter perk are **not** affected
- Zombie drop bags (`EntityLootContainer*`) spawn untouched and award first-open XP the same as world containers — this mod reduces that XP too
- Player chests, secure storage, and dropped player backpacks are excluded from looting XP by the game engine and are unaffected by this mod

## How It Works

The vanilla XP formula for opening an untouched container, derived from decompiling `Progression.AddLevelExp`:

> `xp = floor(gameStage × (XPMultiplier / 100))`

`XPMultiplier` is the server's XP Multiplier game setting (default **100** — meaning 100%). With default settings, vanilla awards `gameStage` XP per untouched container — e.g., game stage 50 gives 50 XP. Both world-placed containers and zombie drop bags use this same code path.

This mod applies `perc_add -0.8` to `PlayerExpGain` for the `Looting` tag. This reduces the XP multiplier by 80%, leaving 20% of vanilla:

> `xp = floor(gameStage × (XPMultiplier / 100) × (1 + (−0.8)))`
> `= floor(gameStage × (XPMultiplier / 100) × 0.2)`

With default server settings (`XPMultiplier = 100`):

> `xp = floor(gameStage × 0.2)`

The result is **20% of vanilla XP** at any given game stage. XP bonus buffs such as Grandpa's Learning Elixir (`perc_add 0.2`) stack additively with this mod's `-0.8`, raising the effective multiplier from `0.2` to `0.4`. This keeps XP boosts proportional and does not restore the full vanilla rate.

### Important to Keep in Mind

Looting XP is an integer — it is `floor`-truncated. At very low game stage the result rounds down to `0 XP` per container.

The first game stage that produces at least `1 XP` per untouched container is `ceil(1 / (XPMultiplier/100 × effectiveMultiplier))`. With default server settings (`XPMultiplier = 100`):

| `perc_add` value | Remaining XP | First non-zero GS (default server) |
| --- | --- | --- |
| `−0.90` | 10% of vanilla | `10` |
| **`−0.80` (this mod)** | **20% of vanilla** | **`5`** |
| `−0.75` | 25% of vanilla | `4` |
| `−0.50` | 50% of vanilla | `2` |
| `0` (vanilla) | 100% | `1` |

With default server settings, this mod produces non-zero looting XP from game stage 5 onward, consistently at 20% of the vanilla rate throughout the game.

> **Note:** If the server's `XPMultiplier` is set below 100 (e.g., 20 for a 20% global XP rate), the threshold shifts higher and the absolute XP values scale down proportionally. For example, with `XPMultiplier = 20` the first non-zero GS with this mod is 25.

## Installation

1. Copy the `EV_ReducedLootingXP` folder into your `7 Days to Die/Mods/` directory.
2. Restart the game or server.

## Compatibility

- 7 Days to Die 1.0 (Alpha 21+)
- Server-side mod — works without client installation
- May conflict with mods that modify `PlayerExpGain` on the `playerMale` entity class

### Companion Mod

Works well alongside [**EV_RemoveTraderXP**](https://github.com/alekho77/epic_7d2d_mods), which completely removes XP from selling items to traders. Together, the two mods close the two most common non-combat XP exploits and shift the progression curve decisively toward zombie killing, crafting, and questing.

## Changelog

### v1.0.0

- Initial release — opening loot containers grants 20% of vanilla XP

---

**Author:** Aleksei Khozin
**Version:** 1.0.0
**Website:** <https://github.com/alekho77/epic_7d2d_mods>
