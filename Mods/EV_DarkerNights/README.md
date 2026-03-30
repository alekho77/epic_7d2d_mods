# Darker Nights

## Description

Makes nights significantly darker for a more immersive and challenging survival experience. Ambient lighting during nighttime is reduced to approximately half of vanilla values. Also enhances night vision goggles with an additional Bright effect to compensate for the increased darkness.

## Features

- **Darker nights** — ambient light values reduced ~2× across the board
- **Enhanced night vision goggles** — adds a secondary Bright screen effect alongside the standard NightVision filter for better visibility in the darkened world
- **Indoor lighting affected** — interior ambient values also reduced for consistency
- **Moon lighting reduced** — moonlight contribution halved for truly dark nights

## Changes

### Ambient Lighting (Night Values)
| Parameter | Vanilla | Modded |
|---|---|---|
| Ambient Equator Scale | 0.45 | 0.225 |
| Ambient Ground Scale | 0.05 | 0.025 |
| Ambient Sky Scale | 0.70 | 0.35 |
| Ambient Sky Desat | 0.70 | 0.35 |
| Ambient Moon | 0.40 | 0.20 |
| Indoor Equator Scale | 1.50 | 0.75 |
| Indoor Ground Scale | 0.20 | 0.10 |
| Indoor Sky Scale | 0.40 | 0.20 |

### Night Vision Goggles
- Standard NightVision effect (green tint) — **retained**
- Additional **Bright** effect (intensity 0.9) — **added** for enhanced visibility
- Both effects activate/deactivate and unequip properly

## Installation

1. Copy the `EV_DarkerNights` folder into your game's `Mods/` directory
2. Restart the game or server

## Compatibility

- 7 Days to Die 1.0 (Alpha 21+)
- Server and single-player compatible
- May conflict with mods that modify `worldglobal.xml` ambient values or the `modArmorNightVision` item modifier

## Changelog

### v1.1.0
- Added enhanced night vision goggles with Bright effect

### v1.0.0
- Initial release with darker ambient night lighting

---

**Author:** Aleksei Khozin  
**Version:** 1.1.0  
**Website:** https://github.com/alekho77/epic_7d2d_mods
