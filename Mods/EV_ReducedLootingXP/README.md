# Reduced Looting XP

## Description

Reduces XP gained from opening untouched loot containers to **20% of vanilla**, rebalancing progression toward combat and survival gameplay.

In vanilla 7 Days to Die, the active first-open looting XP branch awards XP equal to the player's current game stage when an untouched world container is opened. Players who focus on aggressive POI routes, airdrops, and other untouched containers can level disproportionately fast compared to players who mainly progress through direct combat. Zombie drop bags use a separate entity-loot path, but vanilla spawns them prefilled and already touched, so that bag-side first-open XP branch is effectively disabled by default. This mod reduces the active container XP branch while leaving kill XP, loot tables, and bag spawning behavior unchanged.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- Reduces untouched world-container XP to 20% of vanilla (game stage × 0.2 instead of game stage × 1)
- The active looting XP branch stays enabled — it is rebalanced, not removed
- All other XP sources (kills, crafting, quests, selling, harvesting, upgrading) remain completely unchanged
- Loot quality, loot quantity, scavenging speed, and Lucky Looter perk are **not** affected
- Zombie drop bags keep vanilla behavior: they are separate `EntityLootContainer*` drops and their bag-side first-open XP branch remains effectively disabled because they spawn already touched
- Player chests, secure storage, and dropped player backpacks are excluded from looting XP by the game engine and are unaffected by this mod

## How It Works

Vanilla has two separate loot-related XP paths:

1. Untouched world containers use the active looting XP branch. On first open, the game grants XP equal to the player's current `gameStage`, then applies `PlayerExpGain` with the `Looting` tag.
2. Zombie drop bags are separate `EntityLootContainer*` entities. The game spawns them with copied inventory content, which marks their backing loot container as already touched before the player opens it. Because the first-open looting XP award only fires for untouched containers, this bag-side branch is effectively disabled in vanilla.

This mod changes only the active container branch by setting `PlayerExpGain` base multiplier to `0.2` for the `Looting` tag on the player entity. Using `base_set 0.2` scales the base before any additive percentage buffs apply — so a player with Grandpa's Learning Elixir (+20%) gains `gameStage × 0.2 × 1.2` rather than `gameStage × 1.2`, keeping XP boost items proportional without restoring the full vanilla looting XP.

### Important to Keep in Mind

Looting XP from the active untouched-container branch is granted as whole numbers. At low game stage, strong reductions can round down to `0 XP` per container.

With no XP buffs or perks active, players start receiving at least `1 XP` from untouched world containers at these game stages:

| Coefficient | First game stage with non-zero loot XP |
| --- | --- |
| `0.10` | `10` |
| `0.20` | `5` |
| `0.25` | `4` |
| `0.50` | `2` |
| `1.00` | `1` |

That is why this mod uses `0.2` instead of `0.1`: it still heavily nerfs looting XP but avoids making early-game container XP disappear entirely.

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
