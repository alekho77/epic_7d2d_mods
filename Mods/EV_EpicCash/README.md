# EV_EpicCash — Custom Server Currency

🟢 **Server-Side Friendly**

Adds **Epic Bucks** (`evCash`) — a custom in-game currency that lets server admins build an in-game item shop backed by a real-money or points-based online store.

## Overview

Epic Bucks is a neon yellow in-game currency designed as a bridge between a server's external donation/points shop and the in-game economy. The flow is simple:

1. A player purchases points or donates on the server's website.
2. An admin (or automated system) issues Epic Bucks to the player via a console command.
3. The player opens their crafting inventory in-game and exchanges Epic Bucks for the item bundles they want — no admin involvement needed at that point.

This mod also ships a ready-made example bundle — a **Motorcycle Starter Kit** — to demonstrate the pattern. The included guide explains how to add your own bundles for any combination of items.

## Features

- **Custom Currency Item** — `evCash` (Epic Bucks) based on the Old Cash model
- **Neon Yellow Icon** — instantly recognizable bright #FFF200 tint
- **Large Stack Size** — stacks up to 50,000 for convenient storage
- **Cannot Be Sold** — not sellable to traders, keeping it as a server-only economy
- **Cannot Be Used as Fuel** — prevents accidental burning
- **Creative Menu Access** — available in creative mode for easy admin distribution
- **Example Bundle Included** — Motorcycle Starter Kit (motorcycle + 5000 gas + Fuel Saver mod) craftable for 10 Epic Bucks
- **Extensible** — add unlimited custom bundles with any items and prices

## Admin Commands

Give Epic Bucks to a player:

```
giveself evCash 100
give <player_name> evCash 100
```

## Installation

1. Copy the `EV_EpicCash` folder into your `7 Days to Die/Mods/` directory.
2. Restart the game or server.

## Compatibility

- **Game Version:** 7 Days to Die (latest stable)
- **Type:** XML modlet (no Harmony patches required)
- **Multiplayer:** Server-side only — clients do not need this mod installed.

## Adding a Custom Bundle

You can extend this mod by adding your own bundles that players craft using Epic Bucks. Every bundle requires three steps: defining the item, adding localization, and creating a recipe.

### Step 1 — Define the bundle item

Add a new `<item>` block inside the `<append xpath="/items">` section in `Config/items.xml`.

```xml
<item name="evMyCustomBundle">
  <property name="Extends" value="questRewardBundleMaster"/>
  <property name="CreativeMode" value="Player"/>
  <property name="CustomIcon" value="bundleVehicleMotorCycle"/>
  <property name="CustomIconTint" value="FF6600"/>
  <property name="ItemTypeIcon" value="bundle"/>
  <property name="DescriptionKey" value="evMyCustomBundleDesc"/>
  <property class="Action0">
    <property name="Create_item" value="item1,item2,item3"/>
    <property name="Create_item_count" value="1,500,1"/>
  </property>
</item>
```

**Customizable parts:**

| Property | What it controls |
|---|---|
| `name` | Unique internal ID — must be unique across all mods. Use `ev` prefix to avoid conflicts. |
| `CustomIcon` | Icon sprite name. Reuse any vanilla bundle icon, e.g. `bundleVehicleMotorCycle`, `bundleRevolver`, `bundleShotgun`, `bundleRifle`. |
| `CustomIconTint` | RGB hex color of the icon tint (e.g. `00FFCC` for acid turquoise, `FF6600` for orange). |
| `Create_item` | Comma-separated list of item internal names to give when the bundle is opened. |
| `Create_item_count` | Corresponding counts for each item in `Create_item`, in the same order. |

> **Tip:** Item internal names can be found in `/Config/items.xml` and `/Config/item_modifiers.xml` in this repository.

### Step 2 — Add localization

Add two rows to `Config/Localization.txt` — one for the display name and one for the description. At minimum fill in the `english` column; copy the pattern from existing entries for other languages.

```
evMyCustomBundle,items,Item,,,My Custom Bundle,Bundle display name,...
evMyCustomBundleDesc,items,Item,,,"Open to receive item1, 500× item2 and item3.",Bundle description,...
```

The key in the first column must exactly match the `name` attribute of the item and the `DescriptionKey` value.

### Step 3 — Add a recipe

Add a `<recipe>` block inside the `<append xpath="/recipes">` section in `Config/recipes.xml`.

```xml
<recipe name="evMyCustomBundle" count="1" craft_time="1" always_unlocked="true" tags="perkCrafting">
  <ingredient name="evCash" count="25"/>
</recipe>
```

**Customizable parts:**

| Attribute | What it controls |
|---|---|
| `name` | Must match the item `name` exactly. |
| `count` | How many bundles are produced per craft (normally `1`). |
| `craft_time` | Crafting time in seconds. |
| `always_unlocked` | Keep `true` so no schematic is required. |
| `count` on `<ingredient>` | The Epic Bucks price — how many `evCash` the player must spend. |

No `craft_area` attribute means the recipe is craftable directly from the player inventory with no workstation required.

---

## Credits

- **Author:** Aleksei Khozin
- **Community:** [EpicVales Steam Group](https://steamcommunity.com/groups/EpicVales)
- **Source:** [GitHub Repository](https://github.com/alekho77/epic_7d2d_mods)
