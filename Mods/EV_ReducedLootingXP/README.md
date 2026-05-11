# Reduced Looting XP

## Description

Reduces XP gained from opening untouched loot containers to **10% of vanilla**, rebalancing progression toward combat and survival gameplay.

In vanilla 7 Days to Die, opening a loot container awards XP equal to the player's current game stage. This adds up quickly: a blood moon night produces large numbers of loot bags and air drops, and systematically opening them can yield more XP than the fighting itself. Players who focus on looting routes rather than engaging enemies level disproportionately fast compared to players who actually fight their way through the game. This mod reduces that imbalance by keeping the looting XP channel active but much less dominant.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- Reduces container-open XP to 10% of vanilla (game stage × 0.1 instead of game stage × 1)
- XP is still rewarded for looting — the channel is not removed, just rebalanced
- All other XP sources (kills, crafting, quests, selling, harvesting, upgrading) remain completely unchanged
- Loot quality, loot quantity, scavenging speed, and Lucky Looter perk are **not** affected
- Player chests, secure storage, and dropped backpacks are excluded from looting XP by the game engine and are unaffected by this mod

## How It Works

Sets `PlayerExpGain` base multiplier to `0.1` for the `Looting` tag on the player entity. Using `base_set 0.1` scales the base before any additive percentage buffs apply — so a player with Grandpa's Learning Elixir (+20%) gains `gameStage × 0.1 × 1.2` rather than `gameStage × 1.2`, keeping XP boost items proportional without restoring the full vanilla looting XP.

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

- Initial release — opening loot containers grants 10% of vanilla XP

---

**Author:** Aleksei Khozin
**Version:** 1.0.0
**Website:** <https://github.com/alekho77/epic_7d2d_mods>
