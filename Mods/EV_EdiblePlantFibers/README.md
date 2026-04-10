# Edible Plant Fibers

## Description

A humorous mod that makes plant fibers (Yucca Fibers) edible, restoring a whopping **1 food** per use. This is more of a joke mod than a serious gameplay feature — but hey, when the apocalypse hits and you're starving on Day 1 with nothing but grass in your pockets, at least now you can chew on it and pretend it helps.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

## Features

- Plant fibers can be eaten directly from your inventory
- Restores 1 food per use — barely noticeable, but technically not zero
- No health gain, no dysentery risk — grass is surprisingly safe
- Uses the hand-held food eating animation
- Fast 0.5-second consume time — at least the suffering is quick

## How It Works

The mod patches `resourceYuccaFibers` to add an `Eat` action. On consumption it adds **1 point** to the food meter via the standard `buffProcessConsumables` pipeline. The hold type is changed to hand-held food (type 31) so your character plays the eating animation instead of the default resource-holding pose.

## Installation

1. Copy the `EV_EdiblePlantFibers` folder into your game's `Mods/` directory.
2. Restart the game or server.

## Compatibility

- 7 Days to Die — 1.0 (b36)
- Server-side mod — works without client installation
- May conflict with mods that modify the `resourceYuccaFibers` item definition

## Changelog

### v1.0.0

- Initial release — plant fibers are now edible (1 food per use)

---

**Author:** Aleksei Khozin
**Version:** 1.0.0
**Website:** <https://github.com/alekho77/epic_7d2d_mods>
