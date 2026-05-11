# Remove Trader XP

## Description

Removes XP gained from selling items to traders, closing a well-known exploit that breaks server balance.

In vanilla 7 Days to Die, selling items to traders awards XP via the `Selling` tag on `PlayerExpGain`. This mechanic is easily abused: cheap or quickly farmed items (plant fibers, stone, salvaged parts) can be mass-sold in buy/sell cycles, pushing a player from level 1 to level 500 in 10–15 minutes — without engaging with actual survival gameplay. This disadvantages players who level legitimately through combat, looting, and crafting.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- Zeroes out all XP from selling items to any trader
- Closes the buy/sell cycle exploit used to reach level 500 in minutes
- Eliminates the unfair advantage over players who level through survival gameplay
- All other XP sources (kills, crafting, quests, looting, harvesting) remain completely unchanged
- Normal trading (buying, selling for Dukes) is unaffected — only the XP reward is removed

## How It Works

Sets `PlayerExpGain` base value to `0` for the `Selling` tag on the player entity. Using `base_set 0` ensures the result is always exactly zero — unaffected by XP bonus buffs (Grandpa's Learning Elixir, Twitch buffs, etc.) and cannot produce negative XP.

## Installation

1. Copy the `EV_RemoveTraderXP` folder into your `7 Days to Die/Mods/` directory.
2. Restart the game or server.

## Compatibility

- 7 Days to Die 1.0 (Alpha 21+)
- Server-side mod — works without client installation
- May conflict with mods that modify `PlayerExpGain` on `playerMale` entity class

### Companion Mod

Works well alongside [**EV_ReducedLootingXP**](https://github.com/alekho77/epic_7d2d_mods), which reduces XP from opening loot containers to 10% of vanilla. Together, the two mods close the two most common non-combat XP exploits and shift the progression curve decisively toward zombie killing, crafting, and questing.

## Changelog

### v1.0.0

- Initial release — selling items to traders no longer grants XP

## Credits

Inspired by [WMMRemoveTraderXP](https://www.nexusmods.com/7daystodie/mods/4167) by **w00kie n00kie**. The original mod uses a Harmony DLL patch that works in single-player but does not apply on dedicated servers. This modlet reimplements the same idea as a pure XML patch, making it server-side compatible.

---

**Author:** Aleksei Khozin  
**Version:** 1.0.0  
**Website:** <https://github.com/alekho77/epic_7d2d_mods>
