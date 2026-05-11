# Reduced Looting XP

> ⚠️ **Test Build** — exact XP reduction is under active investigation. See [`Refs/ContainerLootXP_Research.md`](../../Refs/ContainerLootXP_Research.md) for details.

## Description

Reduces XP gained from opening untouched loot containers, rebalancing progression toward combat and survival gameplay.

In vanilla 7 Days to Die, opening an untouched loot container awards XP proportional to the player's current game stage. Both world-placed containers (crates, safes, fridges) and zombie drop bags award XP on first open — bags spawn untouched and use the same XP code path as world containers. Players who focus on aggressive POI runs, blood moon looting, and systematic container farming can level disproportionately fast compared to players who progress mainly through combat. This mod reduces container XP while leaving kill XP, loot tables, and bag spawning behavior unchanged.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- Reduces XP from opening untouched containers (world containers and zombie drop bags)
- The looting XP branch stays enabled — it is rebalanced, not removed
- All other XP sources (kills, crafting, quests, selling, harvesting, upgrading) remain completely unchanged
- Loot quality, loot quantity, scavenging speed, and Lucky Looter perk are **not** affected
- Zombie drop bags (`EntityLootContainer*`) spawn untouched and award first-open XP the same as world containers — this mod reduces that XP too
- Player chests, secure storage, and dropped player backpacks are excluded from looting XP by the game engine and are unaffected by this mod

## How It Works

Confirmed from decompiling `Assembly-CSharp.dll` (`XUiC_LootWindowGroup`, `Progression.AddLevelExp`, `EffectManager.GetValue`):

- Looting XP is awarded on first open of an untouched non-player container
- The base XP value passed to the effect system is `gameStage × (XPMultiplier / 100)`
- `EffectManager.GetValue` returns `_base_value × _perc_value`
- `base_set VALUE` replaces `_base_value` with the literal value (absolute replacement)
- `perc_add VALUE` accumulates into `_perc_value` (which starts at `1.0`)
- The final result is cast to `int` (floor-truncated before granting)

This mod applies `base_set 0.8` to `PlayerExpGain` for the `Looting` tag. **The exact XP output of this configuration is under investigation** — in-game testing at known game stages is required to confirm behavior.

> **Note:** The Project Z overhaul mod applies `PlayerExpGain perc_add -1 tags="Looting"` via an always-active buff, which zeroes looting XP on its own. Test results from Project Z sessions may not reflect vanilla behavior. See [`Refs/ContainerLootXP_Research.md`](../../Refs/ContainerLootXP_Research.md) Section 9 for details.

## Installation

1. Copy the `EV_ReducedLootingXP` folder into your `7 Days to Die/Mods/` directory.
2. Restart the game or server.

## Compatibility

- 7 Days to Die 1.0 (Alpha 21+)
- Server-side mod — works without client installation
- May conflict with mods that modify `PlayerExpGain` on the `playerMale` entity class
- **Project Z:** The Z_Game_Balance sub-mod applies its own `PlayerExpGain perc_add -1 tags="Looting"` modifier, which stacks with this mod. Behavior under Project Z differs from vanilla.

### Companion Mod

Works well alongside [**EV_RemoveTraderXP**](https://github.com/alekho77/epic_7d2d_mods), which completely removes XP from selling items to traders. Together, the two mods close the two most common non-combat XP exploits and shift the progression curve decisively toward zombie killing, crafting, and questing.

## Changelog

### v1.0.0

- Initial release — reduces XP from opening untouched loot containers (exact reduction under investigation)

---

**Author:** Aleksei Khozin
**Version:** 1.0.0
**Website:** <https://github.com/alekho77/epic_7d2d_mods>
