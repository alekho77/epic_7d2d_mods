# ZZ_EV_ProjectZRadiostationQuestFix

## Description

Fixes the first **Project Z Radio Station** support quest used by **Rare Samples Chapter 2**.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

<!-- -->

> ### ⚠️ Requires Project Z
>
> This modlet is an **add-on** for **Project Z** and requires the `Z_Radiostation` module to be installed.
> The `ZZ_` prefix ensures this patch loads **after** Project Z so the target quest and game event already exist.

## Features

- Changes `SmallCase03` zone tracking from the default POI-style objective to the buried-supplies style `StayWithin` objective
- Changes the rally marker from `questRallyMarkerFetchClear` to `questRallyMarkerBuriedSupplies`
- Reduces the experimental-alloy reward crate spawn distance from `15-20` blocks to exactly `3` blocks from the player
- Touches only the first small experimental-alloys request used by `Rare Samples` Chapter 2

## How It Works

`SmallCase03` is the first Radio Station support quest that delivers the `10` experimental alloys needed by `RareSamples2`.

This patch changes two parts of that flow:

1. The phase-3 area tracking now uses the same `StayWithin` style used by vanilla buried-supplies quests.
2. The phase-4 reward spawn now drops the alloy crate almost directly next to the player instead of `15-20` blocks away.

The goal is to make the quest transition into its reward phase more reliable and make the spawned crate much harder to lose.

## Installation

1. Copy the `ZZ_EV_ProjectZRadiostationQuestFix` folder into your game's `Mods/` directory.
2. Make sure `Project Z` with `Z_Radiostation` is already installed.
3. Restart the game or server.

## Compatibility

- 7 Days to Die latest stable
- Server-side XML patch
- Requires `Project Z`, specifically `Z_Radiostation`
- May conflict with other mods that patch `SmallCase03` or `action_spawn_reward_SmallCase_ExperimentalAlloys`

## Changelog

### v1.0.0

- Switched `SmallCase03` to buried-supplies style zone tracking
- Changed the rally marker to the buried-supplies marker type
- Reduced the experimental-alloy crate spawn distance to `3` blocks

---

**Author:** Aleksei Khozin  
**Version:** 1.0.0  
**Website:** <https://github.com/alekho77/epic_7d2d_mods>
