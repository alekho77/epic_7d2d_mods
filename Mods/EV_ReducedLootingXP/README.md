# Reduced Looting XP

## Description

Reduces XP gained from opening untouched loot containers to **20% of vanilla**, rebalancing progression toward combat and survival gameplay.

In vanilla 7 Days to Die, opening an untouched loot container awards XP proportional to the player's current game stage. Both world-placed containers (crates, safes, fridges) and zombie drop bags award XP on first open — bags spawn untouched and use the same XP code path as world containers. Players who focus on aggressive POI runs, blood moon looting, and systematic container farming can level disproportionately fast compared to players who progress mainly through combat. This mod reduces container XP while leaving kill XP, loot tables, and bag spawning behavior unchanged.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- Reduces untouched container XP (world containers and zombie drop bags) to 20% of vanilla — effective rate changes from `gameStage × 0.2` to `gameStage × 0.04`
- The looting XP branch stays enabled — it is rebalanced, not removed
- All other XP sources (kills, crafting, quests, selling, harvesting, upgrading) remain completely unchanged
- Loot quality, loot quantity, scavenging speed, and Lucky Looter perk are **not** affected
- Zombie drop bags (`EntityLootContainer*`) spawn untouched and award first-open XP the same as world containers — this mod reduces that XP too
- Player chests, secure storage, and dropped player backpacks are excluded from looting XP by the game engine and are unaffected by this mod

## How It Works

The vanilla XP formula for opening an untouched container is:

> `xp = floor(gameStage × 0.2 × PlayerExpGain)`

The inner `0.2` is a hardcoded engine constant. `PlayerExpGain` for the `Looting` tag defaults to `1.0`, so vanilla awards approximately `gameStage / 5` XP per container. Both world-placed containers and zombie drop bags use this same code path.

This mod sets `PlayerExpGain` to `0.2` for the `Looting` tag, making the effective formula:

> `xp = floor(gameStage × 0.2 × 0.2) = floor(gameStage × 0.04)`

The result is approximately **20% of vanilla XP** at any given game stage (when both round to a non-zero integer). XP bonus buffs such as Grandpa's Learning Elixir apply multiplicatively on top of the reduced `0.2` base, keeping boosts proportional without restoring the full vanilla rate.

### Important to Keep in Mind

Looting XP is an integer — it is `floor`-truncated. At low game stage the result rounds down to `0 XP` per container.

With no XP buffs or perks active, the first game stage that produces at least `1 XP` per untouched container is `ceil(5 / PlayerExpGain)`:

| `PlayerExpGain` | First game stage with non-zero loot XP |
| --- | --- |
| `0.10` | `50` |
| **`0.20` (this mod)** | **`25`** |
| `0.25` | `20` |
| `0.50` | `10` |
| `1.00` (vanilla) | `5` |

With this mod set to `0.2`, looting XP from containers is zero until game stage 25. This is intentional — the mod targets players who use large-scale looting as a primary XP source, not casual early-game looting.

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
