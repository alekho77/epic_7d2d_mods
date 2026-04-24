# EV_EpicCash — Custom Server Currency

## Description

Adds **Epic Bucks** (`evCash`) — a custom in-game currency designed for **dedicated server administrators** who want to provide a fair and enjoyable experience for all players. Admins can reward active community members, compensate for lost progress, run in-game events, or help newcomers and casual players catch up with veterans — letting everyone enjoy the server equally, regardless of how much time they spend in the game.

> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.

<!-- -->

> ### ⚠️ Disclaimer
>
> The author **does not endorse pay-to-win mechanics**. This mod was created solely to help dedicated server owners sustain their communities and provide a fair, enjoyable gameplay experience for all players. If you choose to tie Epic Bucks to real-money donations, please **avoid aggressive, intrusive, or no-alternative monetization policies**. The best servers are those where supporting the server is voluntary and never gives a decisive competitive advantage.

## How It Works

Epic Bucks is a neon yellow in-game currency that server administrators distribute to players at their discretion. Typical use cases include rewards for community participation, compensation after server wipes or rollbacks, event prizes, or as part of a server support program. The flow is simple:

1. An admin decides how and when to distribute Epic Bucks (console commands, automated systems, or any other method).
2. Players receive Epic Bucks in their inventory.
3. Players open their crafting menu and exchange Epic Bucks for the item bundles they want — no further admin involvement needed.

This mod ships **92 ready-made bundles** covering vehicles, weapons, ammo, armor, tools, skill magazines, skill books, workstations, food, and drinks. The included guide also explains how to add your own custom bundles for any combination of items.

## Features

- **Custom Currency Item** — `evCash` (Epic Bucks) based on the Old Cash model
- **Neon Yellow Icon** — instantly recognizable bright #FFF200 tint
- **Large Stack Size** — stacks up to 50,000 for convenient storage
- **Cannot Be Sold** — not sellable to traders, keeping it as a server-only economy
- **Cannot Be Used as Fuel** — prevents accidental burning
- **Creative Menu Access** — available in creative mode for easy admin distribution
- **92 Ready-Made Bundles** — vehicles, weapons, ammo, armor, tools, magazines, books, workstations, food, and drinks
- **Color-Coded Categories** — each bundle type has a unique neon icon tint for instant recognition
- **Extensible** — add unlimited custom bundles with any items and prices

## Admin Commands

Give Epic Bucks to a player:

```text
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

## Included Bundles

The mod ships with **92 ready-made bundles** across 10 categories, all craftable from the player inventory using Epic Bucks (EB).

### 🟠 Vehicle Bundles

| Name | Contents | Description | Price |
| --- | --- | --- | ---: |
| Bicycle Kit | Bicycle, 2× Vehicle Storage mod | Fully assembled bicycle and 2 Vehicle Storage mods | 5 EB |
| Minibike Starter Kit | Minibike, 3,000× Gas Can, Super Charger mod | Fully assembled minibike with 3,000 gasoline cans and a Super Charger mod | 15 EB |
| Motorcycle Starter Kit | Motorcycle, 5,000× Gas Can, Fuel Saver mod | Fully assembled motorcycle with 5,000 gasoline cans and a Fuel Saver mod | 20 EB |
| 4x4 Truck Starter Kit | 4x4 Truck, 12,000× Gas Can, Fuel Saver / Super Charger / Reserve Fuel Tank mods | Fully assembled 4x4 truck with 12,000 gasoline cans and 3 vehicle mods | 50 EB |
| Gyrocopter Starter Kit | Gyrocopter, 12,000× Gas Can | Fully assembled gyrocopter and 12,000 gasoline cans | 50 EB |

### 🔴 Weapon Bundles

| Name | Contents | Description | Price |
| --- | --- | --- | ---: |
| Pistol Kit | T6 Pistol, 600× AP 9mm | Tier 6 Pistol and 600 AP 9mm rounds | 20 EB |
| Pump Shotgun Kit | T6 Pump Shotgun, 600× AP Slugs | Tier 6 Pump Shotgun and 600 AP slugs | 20 EB |
| Sniper Rifle Kit | T6 Sniper Rifle, 1,000× AP 7.62mm | Tier 6 Sniper Rifle and 1,000 AP 7.62mm rounds | 40 EB |
| SMG-5 Kit | T6 SMG-5, 1,500× AP 9mm | Tier 6 SMG-5 and 1,500 AP 9mm rounds | 50 EB |
| Desert Vulture Kit | T6 Desert Vulture, 1,000× AP .44 Magnum | Tier 6 Desert Vulture and 1,000 AP .44 Magnum rounds | 40 EB |
| Auto Shotgun Kit | T6 Auto Shotgun, 1,000× AP Slugs | Tier 6 Auto Shotgun and 1,000 AP slugs | 40 EB |
| Robotic Turret Kit | T6 Robotic Turret, 1,000× AP Turret Ammo | Tier 6 Robotic Turret and 1,000 AP turret rounds | 30 EB |
| M60 Machine Gun Kit | T6 M60, 3,000× AP 7.62mm | Tier 6 M60 Machine Gun and 3,000 AP 7.62mm rounds | 60 EB |

### 🟡 Ammo Bundles

| Name | Contents | Description | Price |
| --- | --- | --- | ---: |
| 9mm Ammo Pack | 1,000× 9mm rounds | 1,000 standard 9mm rounds | 1 EB |
| .44 Magnum Ammo Pack | 1,000× .44 Magnum rounds | 1,000 standard .44 Magnum rounds | 1 EB |
| 7.62mm Ammo Pack | 1,000× 7.62mm rounds | 1,000 standard 7.62mm rounds | 1 EB |
| Shotgun Shell Pack | 1,000× Shotgun Shells | 1,000 standard shotgun shells | 1 EB |
| Robotic Turret Ammo Pack | 1,000× Turret Ammo | 1,000 standard Robotic Turret rounds | 1 EB |
| AP 9mm Ammo Pack | 1,000× AP 9mm rounds | 1,000 AP 9mm rounds | 3 EB |
| AP .44 Magnum Ammo Pack | 1,000× AP .44 Magnum rounds | 1,000 AP .44 Magnum rounds | 3 EB |
| AP 7.62mm Ammo Pack | 1,000× AP 7.62mm rounds | 1,000 AP 7.62mm rounds | 3 EB |
| AP Shotgun Slug Pack | 1,000× AP Shotgun Slugs | 1,000 AP shotgun slugs | 3 EB |
| AP Robotic Turret Ammo Pack | 1,000× AP Turret Ammo | 1,000 AP Robotic Turret rounds | 3 EB |

### 🔵 Armor Bundles

All armor bundles include a full Tier 6 set — helmet, outfit, gloves, and boots. Prices are tiered by the combat/crafting impact of each armor class's set bonuses.

| Name | Contents | Description | Price |
| --- | --- | --- | ---: |
| Lumberjack Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Lumberjack armor set | 40 EB |
| Preacher Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Preacher armor set | 40 EB |
| Farmer Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Farmer armor set | 40 EB |
| Miner Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Miner armor set | 40 EB |
| Nomad Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Nomad armor set | 40 EB |
| Rogue Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Rogue armor set | 40 EB |
| Athletic Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Athletic armor set | 40 EB |
| Biker Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Biker armor set | 40 EB |
| Scavenger Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Scavenger armor set | 40 EB |
| Ranger Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Ranger armor set | 40 EB |
| Enforcer Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Enforcer armor set | 40 EB |
| Commando Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Commando armor set | 40 EB |
| Assassin Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Assassin armor set | 40 EB |
| Nerd Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Nerd armor set | 40 EB |
| Raider Armor Set | T6 helmet, outfit, gloves, boots | Full Tier 6 Raider armor set | 40 EB |

### 🟢 Tool Bundles

Most tool bundles contain a single Tier 6 tool. Nailgun Kit also includes a stack of Concrete Mix for immediate building and repairs.

| Name | Contents | Description | Price |
| --- | --- | --- | ---: |
| Nailgun Kit | T6 Nailgun, 500× Concrete Mix | Tier 6 Nailgun plus 500 Concrete Mix | 30 EB |
| Impact Driver Kit | T6 Impact Driver | Tier 6 Impact Driver | 30 EB |
| Chainsaw Kit | T6 Chainsaw | Tier 6 Chainsaw | 20 EB |
| Auger Kit | T6 Auger | Tier 6 Auger | 30 EB |

### 🟣 Skill Magazine Bundles

All magazine bundles contain 10 copies of the respective magazine. Skill magazines feed both vanilla crafting skills and skill trees added by other modpacks, so the price sits slightly above the standard 10 EB tier.

| Name | Contents | Description | Price |
| --- | --- | --- | ---: |
| Home Cooking Weekly Pack (10) | 10× Home Cooking Weekly | 10 Home Cooking Weekly magazines | 12 EB |
| Medical Journal Pack (10) | 10× Medical Journal | 10 Medical Journal magazines | 12 EB |
| Armored Up Pack (10) | 10× Armored Up | 10 Armored Up magazines | 12 EB |
| Vehicle Adventures Pack (10) | 10× Vehicle Adventures | 10 Vehicle Adventures magazines | 12 EB |
| Tools Digest Pack (10) | 10× Tools Digest | 10 Tools Digest magazines | 12 EB |
| Handy Land Pack (10) | 10× Handy Land | 10 Handy Land magazines | 12 EB |
| Scrapping 4 Fun Pack (10) | 10× Scrapping 4 Fun | 10 Scrapping 4 Fun magazines | 12 EB |
| Furious Fists Pack (10) | 10× Furious Fists | 10 Furious Fists magazines | 12 EB |
| Knife Guy Pack (10) | 10× Knife Guy | 10 Knife Guy magazines | 12 EB |
| Big Hitters Pack (10) | 10× Big Hitters | 10 Big Hitters magazines | 12 EB |
| Get Hammered Pack (10) | 10× Get Hammered | 10 Get Hammered magazines | 12 EB |
| Sharp Sticks Pack (10) | 10× Sharp Sticks | 10 Sharp Sticks magazines | 12 EB |
| Bow Hunters Pack (10) | 10× Bow Hunters | 10 Bow Hunters magazines | 12 EB |
| Handgun Magazine Pack (10) | 10× Handgun Magazine | 10 Handgun Magazine magazines | 12 EB |
| Shotgun Weekly Pack (10) | 10× Shotgun Weekly | 10 Shotgun Weekly magazines | 12 EB |
| Rifle World Pack (10) | 10× Rifle World | 10 Rifle World magazines | 12 EB |
| Tactical Warfare Pack (10) | 10× Tactical Warfare | 10 Tactical Warfare magazines | 12 EB |
| Explosive Magazine Pack (10) | 10× Explosive Magazine | 10 Explosive Magazine magazines | 12 EB |
| Tech Planet Pack (10) | 10× Tech Planet | 10 Tech Planet magazines | 12 EB |
| Southern Farming Pack (10) | 10× Southern Farming | 10 Southern Farming magazines | 12 EB |
| Wiring 101 Pack (10) | 10× Wiring 101 | 10 Wiring 101 magazines | 12 EB |
| Electrical Traps Pack (10) | 10× Electrical Traps | 10 Electrical Traps magazines | 12 EB |
| Forge Ahead Pack (10) | 10× Forge Ahead | 10 Forge Ahead magazines | 12 EB |

### 🟪 Skill Book Bundles

All book bundles contain the complete set of 7 volumes. Every Skill Book Bundle now costs 25 EB.

| Name | Contents | Description | Price |
| --- | --- | --- | ---: |
| The Fireman's Almanac Complete Set | 7 volumes | All 7 volumes of The Fireman's Almanac | 25 EB |
| The Great Heist Complete Set | 7 volumes | All 7 volumes of The Great Heist | 25 EB |
| Wasteland Treasures Complete Set | 7 volumes | All 7 volumes of Wasteland Treasures | 25 EB |
| The Hunter's Journal Complete Set | 7 volumes | All 7 volumes of The Hunter's Journal | 25 EB |
| Art of Mining Complete Set | 7 volumes | All 7 volumes of Art of Mining | 25 EB |
| Night Stalker Complete Set | 7 volumes | All 7 volumes of Night Stalker | 25 EB |
| Batter Up Complete Set | 7 volumes | All 7 volumes of Batter Up | 25 EB |
| Sledge Saga Complete Set | 7 volumes | All 7 volumes of Sledge Saga | 25 EB |
| Ranger's Guide to Archery Complete Set | 7 volumes | All 7 volumes of Ranger's Guide to Archery | 25 EB |
| Sniper Complete Set | 7 volumes | All 7 volumes of Sniper | 25 EB |
| Tech Junkie Complete Set | 7 volumes | All 7 volumes of Tech Junkie | 25 EB |
| Bar Brawling Complete Set | 7 volumes | All 7 volumes of Bar Brawling | 25 EB |
| Spear Hunter Complete Set | 7 volumes | All 7 volumes of Spear Hunter | 25 EB |
| Lucky Looter Complete Set | 7 volumes | All 7 volumes of Lucky Looter | 25 EB |
| Magnum Enforcer Complete Set | 7 volumes | All 7 volumes of Magnum Enforcer | 25 EB |
| Pistol Pete Complete Set | 7 volumes | All 7 volumes of Pistol Pete | 25 EB |
| Shotgun Messiah Complete Set | 7 volumes | All 7 volumes of Shotgun Messiah | 25 EB |
| Automatic Weapons Handbook Complete Set | 7 volumes | All 7 volumes of Automatic Weapons Handbook | 25 EB |
| Urban Combat Complete Set | 7 volumes | All 7 volumes of Urban Combat | 25 EB |

### 💜 Workstation Bundle

| Name | Contents | Description | Price |
| --- | --- | --- | ---: |
| Basic Workstations Kit | Forge, Workbench, Cement Mixer, Chemistry Station, 2× Dew Collector | All essential crafting workstations and 2 dew collectors | 25 EB |

### 🍀 Food Bundles

| Name | Contents | Description | Price |
| --- | --- | --- | ---: |
| Small Food Kit | One random stack: 8-12× basic meals | One random stack of Bacon and Eggs, Vegetable Stew, Grilled Meat, Blueberry Pie, Pumpkin Bread, or Boiled Egg | 1 EB |
| Medium Food Kit | One random stack: 10× hearty meals | One random stack of Meat Stew, Steak and Potato Meal, Hobo Stew, Fish Tacos, Chili Dog, Pumpkin Pie, or Tuna Fish Gravy Toast | 2 EB |
| Large Food Kit | One random stack: 10× gourmet meals | One random stack of Honey Glazed Sham, Honey Brisket, Sham Chowder, Gumbo Stew, Shepherd's Pie, or Spaghetti | 3 EB |

### 💧 Drink Bundles

| Name | Contents | Description | Price |
| --- | --- | --- | ---: |
| Small Drink Kit | One random stack: 12-20× basic drinks | One random stack of Goldenrod Tea, Red Tea, Coffee, or Water | 1 EB |
| Medium Drink Kit | One random stack: 15× quality drinks | One random stack of Pure Mineral Water or Yucca Juice | 2 EB |
| Large Drink Kit | One random stack: 15× premium drinks | One random stack of Honey Tea, Yucca Juice Smoothie, Mega Crush, or Pure Mineral Water | 3 EB |

> **Extending with non-vanilla items:** If your server runs mods that add custom items to the game, you can easily extend EpicCash to support them. See the [Adding a Custom Bundle](#adding-a-custom-bundle) section below for a step-by-step guide on creating bundles with any items at any price.

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
| --- | --- |
| `name` | Unique internal ID — must be unique across all mods. Use `ev` prefix to avoid conflicts. |
| `CustomIcon` | Icon sprite name. Reuse any vanilla bundle icon, e.g. `bundleVehicleMotorCycle`, `bundleRevolver`, `bundleShotgun`, `bundleRifle`. |
| `CustomIconTint` | RGB hex color of the icon tint (e.g. `00FFCC` for acid turquoise, `FF6600` for orange). |
| `Create_item` | Comma-separated list of item internal names to give when the bundle is opened. |
| `Create_item_count` | Corresponding counts for each item in `Create_item`, in the same order. |

> **Tip:** Item internal names can be found in `/Config/items.xml` and `/Config/item_modifiers.xml` in this repository.

### Step 2 — Add localization

Add two rows to `Config/Localization.txt` — one for the display name and one for the description. At minimum fill in the `english` column; copy the pattern from existing entries for other languages.

```text
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
| --- | --- |
| `name` | Must match the item `name` exactly. |
| `count` | How many bundles are produced per craft (normally `1`). |
| `craft_time` | Crafting time in seconds. |
| `always_unlocked` | Keep `true` so no schematic is required. |
| `count` on `<ingredient>` | The Epic Bucks price — how many `evCash` the player must spend. |

No `craft_area` attribute means the recipe is craftable directly from the player inventory with no workstation required.

## Changelog

### v1.2.1

- Fine-tuned magazine and book bundle prices to better fit servers that run this mod alongside other modpacks (which often hand out books and magazines much faster than vanilla) while still making sense on pure vanilla servers
- **Skill Magazines** (all 23 bundles): 10 → **12 EB**
- **Skill Books S-tier** (Lucky Looter, Magnum Enforcer, Pistol Pete, Shotgun Messiah, Automatic Weapons, Urban Combat): 30 → **25 EB**
- **Skill Books A-tier** (Night Stalker, Batter Up, Sledge Saga, Ranger's Guide, Sniper, Tech Junkie, Bar Brawling, Spear Hunter): 25 → **20 EB**
- **Skill Books B-tier** (Fireman's Almanac, Great Heist, Wasteland Treasures, Hunter's Journal, Art of Mining): 20 → **15 EB**
- All other bundle prices are unchanged

### v1.2.0

- Rebalanced bundle prices to follow a consistent "impact-based" pricing model — bundles that massively accelerate progression or grant permanent passive bonuses now cost more, while low-impact or early-game bundles remain cheap
- **Vehicles**: 4x4 Truck Starter Kit 20 → 30 EB, Gyrocopter Starter Kit 20 → 30 EB
- **Weapons**: Sniper Rifle Kit 15 → 20 EB, Desert Vulture / Auto Shotgun / Robotic Turret kits 20 → 25 EB, M60 Machine Gun Kit 25 → 40 EB
- **Ammo**: all AP ammo packs 2 → 3 EB (standard ammo unchanged at 1 EB)
- **Armor**: tiered pricing — low-impact sets (Lumberjack, Preacher, Farmer, Miner, Nomad) stay at 10 EB; mid-impact sets (Rogue, Athletic, Biker, Scavenger, Ranger) raised to 15 EB; high-impact sets (Enforcer, Commando, Assassin, Nerd, Raider) raised to 20 EB
- **Tools**: Chainsaw Kit 5 → 12 EB, Auger Kit 5 → 20 EB (Nailgun / Impact Driver unchanged at 5 EB)
- **Skill Books**: tiered pricing — situational sets (Fireman's Almanac, Great Heist, Wasteland Treasures, Hunter's Journal, Art of Mining) raised to 20 EB; strong sets (Night Stalker, Batter Up, Sledge Saga, Ranger's Guide, Sniper, Tech Junkie, Bar Brawling, Spear Hunter) raised to 25 EB; top-tier must-have sets (Lucky Looter, Magnum Enforcer, Pistol Pete, Shotgun Messiah, Automatic Weapons, Urban Combat) raised to 30 EB
- **Workstations**: Basic Workstations Kit 50 → 25 EB (early-game content; previous price was too steep)
- Skill magazine bundles, food bundles, drink bundles, and standard ammo packs are unchanged

### v1.1.0

- Added 92 ready-made item bundles across 10 categories: vehicles, weapons, ammo, armor, tools, skill magazines, skill books, workstations, food, and drinks
- Each bundle category has a unique neon icon color for easy visual identification
- Full localization support (English + Russian descriptions, display names in all 14 languages)

### v1.0.0

- Initial release with evCash currency and Motorcycle Starter Kit example bundle

## Credits

- **Author:** Aleksei Khozin
- **Community:** [EpicVales Steam Group](https://steamcommunity.com/groups/EpicVales)
- **Source:** [GitHub Repository](https://github.com/alekho77/epic_7d2d_mods)

---

**Author:** Aleksei Khozin\
**Version:** 1.2.1\
**Website:** [https://github.com/alekho77/epic_7d2d_mods](https://github.com/alekho77/epic_7d2d_mods)
