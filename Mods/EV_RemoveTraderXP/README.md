# Remove Trader XP

## Description

Completely removes XP gained from selling items to traders, preventing abuse of trader XP for rapid leveling.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- Zeroes out all experience points from selling items to any trader
- Prevents speedrun-style power leveling through buy/sell exploits
- All other XP sources (kills, crafting, quests, harvesting, etc.) remain unchanged

## How It Works

Sets `PlayerExpGain` base value to `0` for the `Selling` tag on the player entity. Using `base_set 0` ensures the result is always exactly zero — unaffected by XP bonus buffs (Grandpa's Learning Elixir, Twitch buffs, etc.) and cannot produce negative XP.

## Installation

1. Copy the `EV_RemoveTraderXP` folder into your `7 Days to Die/Mods/` directory.
2. Restart the game or server.

## Compatibility

- 7 Days to Die 1.0 (Alpha 21+)
- Server-side mod — works without client installation
- May conflict with mods that modify `PlayerExpGain` on `playerMale` entity class

## Changelog

### v1.0.0

- Initial release — selling items to traders no longer grants XP

---

**Author:** Aleksei Khozin  
**Version:** 1.0.0  
**Website:** <https://github.com/alekho77/epic_7d2d_mods>
