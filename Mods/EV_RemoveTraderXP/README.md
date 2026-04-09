# EV_RemoveTraderXP

🟢 **Server-Side Friendly**

Completely removes XP gained from selling items to traders, preventing abuse of trader XP for rapid leveling.

## Features

- Zeroes out all experience points from selling items to any trader
- Prevents speedrun-style power leveling through buy/sell exploits
- All other XP sources (kills, crafting, quests, harvesting, etc.) remain unchanged

## How It Works

Applies a `-100%` modifier to `PlayerExpGain` with the `Selling` tag on the player entity, effectively nullifying any XP that would be awarded from trader sell transactions.

## Installation

1. Copy the `EV_RemoveTraderXP` folder into your `7 Days to Die/Mods/` directory.
2. Restart the game or server.

## Compatibility

- **Game Version:** 1.2 (V1.2 b27+)
- **Mod Type:** XML-only (no DLL required)
- Works on dedicated servers — no client-side installation needed.
