# 7 Days to Die — Modding Guide

This guide covers three progressive phases of modding 7 Days to Die, from simple XML-only modlets to full total conversion overhauls. Each phase builds on the previous one.

- **[Phase 1: XML Modlets](phase1_xml_modlets.md)** — Data-only mods using XPath patches on game XML configs. No code, no compilation, no Unity project needed.
- **[Phase 2: Harmony Mods](phase2_harmony_mods.md)** — C# code mods using the HarmonyX patching framework to alter game behavior at runtime.
- **[Phase 3: Total Conversion / Deep Modding](phase3_total_conversion.md)** — Full overhauls involving custom assets (models, textures, sounds, animations), complete UI replacement, world generation, and everything from Phases 1–2 combined.

---

## Game Overview

| Property | Value |
| --- | --- |
| **Game** | 7 Days to Die |
| **Developer** | The Fun Pimps (TFP) |
| **Engine** | Unity (Mono backend) |
| **Platform** | Steam (Windows 64-bit), also Microsoft Store / Xbox |
| **Steam App ID** | 251570 |
| **Anti-Cheat** | EasyAntiCheat (EAC) — disabled when launching without EAC for modding |
| **UI System** | NGUI (not standard Unity UI) + custom XUi XML layer |
| **Scripting Runtime** | Mono/.NET (MonoBleedingEdge), C# assemblies in `7DaysToDie_Data\Managed\` |
| **Mod Framework** | HarmonyX (bundled as `0Harmony.dll`) |
| **Config System** | XML files with XPath-based patching |
| **Asset System** | Unity Addressables + legacy AssetBundles |

---

## Game Installation Structure

A standard 7 Days to Die installation contains these top-level directories:

| Directory | Purpose |
| --- | --- |
| `(root)` | Executables (`7DaysToDie.exe`, `7DaysToDie_EAC.exe`, `7dLauncher.exe`), Unity runtime (`UnityPlayer.dll`), Steam/NVIDIA libraries |
| `7DaysToDie_Data\` | Unity player data: `Managed\` (all .NET DLLs), `Plugins\` (native DLLs), `StreamingAssets\` (Addressables catalog, intro video) |
| `Data\` | Game content: `Config\` (XML configs), `Prefabs\` (POIs), `ItemIcons\`, `Music\`, `Bundles\`, `Addressables\`, `Worlds\`, `Stamps\` |
| `EasyAntiCheat\` | EAC binaries, certs, and localization |
| `Launcher\` | Game launcher translation files |
| `Licenses\` | Third-party library license texts |
| `Logos\` | Splash screen and app icon images |
| `MonoBleedingEdge\` | Mono runtime (`mono-2.0-bdwgc.dll`) and configuration |
| `Mods\` | Installed mods — the game loads valid mod folders (those containing `ModInfo.xml`). Mods can also be placed in `%APPDATA%\7DaysToDie\Mods\` (official recommendation); both locations work |

---

## Modlet Folder Structure

Mods can be placed in the game's `Mods\` folder or in `%APPDATA%\7DaysToDie\Mods\` (the currently recommended location). Each mod is a self-contained subfolder:

```text
Mods\
  <ModName>\
    ModInfo.xml          # Required — name, version, author, description
    Config\              # XML xpath patches (mirrors Data\Config\ structure)
    Harmony\             # Compiled C# DLL(s) for Harmony patches (optional)
    Resources\           # Unity AssetBundles, textures, sounds (optional)
    UIAtlases\           # Custom UI sprite atlases (optional)
```

### ModInfo.xml (Required)

Every mod **must** include a `ModInfo.xml`. There are two format versions:

**V2 format** (introduced in Alpha 21, recommended):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xml>
  <Name value="MyModName"/>             <!-- Required. Internal ID: latin letters, numbers, underscores, dashes only. No spaces. Must be globally unique. -->
  <DisplayName value="My Mod Name"/>    <!-- Required. Human-readable name shown in UI. -->
  <Version value="1.0.0"/>              <!-- Required. SemVer: major.minor[.build[.revision]] -->
  <Description value="What this mod does."/>  <!-- Optional -->
  <Author value="AuthorName"/>          <!-- Optional -->
  <Website value="https://example.com"/>      <!-- Optional -->
</xml>
```

**V1 format** (legacy, pre-Alpha 21):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ModInfo>
  <Name value="MyModName"/>
  <DisplayName value="My Mod Name"/>
  <Description value="What this mod does."/>
  <Author value="AuthorName"/>
  <Version value="1.0.0"/>
  <Website value="https://example.com"/>
</ModInfo>
```

Key differences: V2 uses `<xml>` as root (instead of `<ModInfo>`), `Name` is strictly an internal ID (no spaces), and `DisplayName` is the user-facing name. V1 is still loaded but logs a warning; TFP indicated V1 support may be dropped in future versions.

### Mod Load Order

- Mods are loaded **alphabetically** by folder name.
- Use numeric prefixes like `0_`, `1_`, `Z_` to control order.
- `0_TFP_Harmony` (official TFP mod) loads first.
- XML patches are applied in load order — later mods can override earlier ones.

---

## How to Test Mods

1. Copy (or symlink) the mod folder into `%APPDATA%\7DaysToDie\Mods\` (recommended) or the game's `Mods\` directory.
2. Launch the game **without EAC** (`7DaysToDie.exe` directly, not `7DaysToDie_EAC.exe`).
3. Check `Player.log` / `output_log` in the client log location for your version and launch method (commonly `%APPDATA%\..\LocalLow\The Fun Pimps\7 Days To Die\Player.log`).
4. The game validates XML on load — XPath errors are logged with the offending file and line.

---

## Key Tools for Modders

| Tool | Purpose | Phase |
| --- | --- | --- |
| **Text editor** (VS Code, Notepad++) | Edit XML configs, Localization.txt | 1, 2, 3 |
| **dnSpy** or **ILSpy** | Decompile `Assembly-CSharp.dll` to read game C# source | 2, 3 |
| **Visual Studio** or **Rider** | Write and compile Harmony C# mods | 2, 3 |
| **.NET Framework 4.8 SDK** | Build target for Harmony mod DLLs | 2, 3 |
| **Unity Editor** (matching game version) | Create AssetBundles (models, textures, prefabs) | 3 |
| **UABE** (Unity Asset Bundle Extractor) | Inspect and extract existing AssetBundles | 3 |
| **AssetStudio** | Browse and export assets from bundles | 3 |
| **7D2D Prefab Editor** | Create and edit POI prefabs | 3 |
| **Blender / 3ds Max** | Create 3D models for items, blocks, entities | 3 |
| **GIMP / Photoshop** | Create textures and item icons (PNG) | 1, 3 |

---

## Community Resources

### Official

| Resource | URL |
| --- | --- |
| The Fun Pimps Official Site | <https://7daystodie.com/> |
| 7D2D Steam Store Page | <https://store.steampowered.com/app/251570/7_Days_to_Die/> |
| TFP Community Forums | <https://community.thefunpimps.com/> |
| Game Modification Category | <https://community.thefunpimps.com/categories/game-modification.48/> |
| Tutorials & Guides | <https://community.thefunpimps.com/forums/tutorials-guides.39/> |
| Mods (Resources) | <https://community.thefunpimps.com/resources/> |

### Wikis & Knowledge Bases

| Resource | URL |
| --- | --- |
| 7 Days to Die Wiki (Fandom) | <https://7daystodie.fandom.com/wiki/7_Days_to_Die_Wiki> |
| 7D2D Modding Wiki | <https://7d2dsdx.github.io/> |
| XPath Modding Explanation Thread (sphereii) | <https://community.thefunpimps.com/threads/xpath-modding-explanation-thread.7653/> |

### Community Forums & Hubs

| Resource | URL |
| --- | --- |
| Nexus Mods — 7D2D | <https://www.nexusmods.com/7daystodie> |
| Reddit r/7daystodie | <https://www.reddit.com/r/7daystodie/> |
| Discord — Official 7D2D | <https://discord.gg/7daystodie> |
| Unofficial Modding Discord | <https://community.thefunpimps.com/threads/unnofficial-modding-discord.23400/> |
| Discord — 7D2D Modding | <https://discord.gg/7d2dmodding> |

### Modding References

| Resource | URL |
| --- | --- |
| Harmony Documentation | <https://harmony.pardeike.net/articles/intro.html> |
| HarmonyX (BepInEx fork) | <https://github.com/BepInEx/HarmonyX> |
| SphereII's DMT | <https://github.com/SphereII/DMT> |
| 7D2D Mod Launcher | <https://github.com/SphereII/The7D2DModLauncher> |
| KhaineGB's Modding Examples | <https://community.7daystodie.com/topic/19594-khainesgb-modlets/> |
| SphereII's Modlets & Tutorials | <https://community.7daystodie.com/topic/28540-sphereiis-modlets/> |

### Notable Total Conversion Mods (Study Material)

| Mod | Description |
| --- | --- |
| **Undead Legacy** | Complete overhaul: new crafting, UI, progression, textures, sounds |
| **Darkness Falls** | Adds classes, demons, new biomes, quests, NPCs |
| **Rebirth** | Survival-focused with new mechanics and progression |
| **War of the Walkers** | Expands content: items, entities, vehicles |
| **Ravenhearst** | Hardcore survival with overhauled crafting and building |

---

## EAC and Modding

- **EAC must be disabled** to use Harmony mods or any DLL-based mods.
- Launch `7DaysToDie.exe` directly (not via `7DaysToDie_EAC.exe`) to bypass EAC.
- XML-only modlets **can** work with EAC enabled (no DLLs involved), but it is safer to test without EAC.
- Servers using DLL/Harmony mods must disable EAC; clients connecting to such servers must also have EAC off. XML-only and some server-side-only mods can be EAC-compatible.

---

## Quick Reference: What Each Phase Covers

| Capability | Phase 1 (XML) | Phase 2 (Harmony) | Phase 3 (Total Conversion) |
| --- | --- | --- | --- |
| Change item stats, recipes, loot | Yes | — | Yes |
| Add new items/blocks/entities (data) | Yes | — | Yes |
| Modify UI layout (XUi) | Yes | — | Yes |
| Change game text (Localization) | Yes | — | Yes |
| Alter game logic / add new mechanics | — | Yes | Yes |
| Hook into game events programmatically | — | Yes | Yes |
| Replace models, textures, animations | — | — | Yes |
| Replace music, sounds, videos | — | — | Yes |
| Custom Unity AssetBundles | — | — | Yes |
| New POI prefabs / world generation | — | — | Yes |
| Replace splash screens, icons | — | — | Yes |

---

## Inventory Objects Reference — Config Files with Giveable Items

This section documents **every game configuration file** whose entries can appear in the player's inventory — i.e., objects obtainable via the **Creative Menu** (`CM`) or the console command **`giveself <name>`**.

Only **three config files** define inventory-compatible objects:

| File | Root Element | Object Tag | Total Objects |
| --- | --- | --- | --- |
| `Data/Config/items.xml` | `<items>` | `<item>` | **1 380** |
| `Data/Config/blocks.xml` | `<blocks>` | `<block>` | **6 289** |
| `Data/Config/item_modifiers.xml` | `<item_modifiers>` | `<item_modifier>` | **107** |
| | | **Grand Total** | **7 776** |

> **Important:** All 7 776 objects can be given to the player via `giveself <internal_name>` regardless of their `CreativeMode` setting. The `CreativeMode` property only controls visibility in the Creative Menu, not actual availability through console commands.

### CreativeMode Values

Every item, block, and modifier can have a `CreativeMode` property that controls whether it appears in the Creative Menu:

| Value | Meaning |
| --- | --- |
| *(not set / default)* | Inherits standard visibility — typically **visible** in the Creative Menu |
| `Player` | Explicitly visible to players in the Creative Menu |
| `Dev` | Visible only when the game is in Developer mode |
| `Test` | Visible only in test/debug builds |
| `None` | Hidden from the Creative Menu entirely (still giveable via `giveself`) |
| `Console` | Available only through console commands (rare, used by 2 items) |

### Creative Menu Group Categories

Items visible in the Creative Menu are organized into tab groups via the `Group` property. A single object can belong to multiple groups (comma-separated). The following groups exist across all three config files:

| Group | Visible Objects |
| --- | --- |
| `Building` | 131 |
| `advBuilding` | 121 |
| `Decor/Miscellaneous` | 99 |
| `Food/Cooking` | 73 |
| `Science` | 69 |
| `Ammo/Weapons` | 66 |
| `Resources` | 58 |
| `CFFood/Cooking` | 48 |
| `TCScience` | 44 |
| `Ranged Weapons` | 35 |
| `Tools/Traps` | 33 |
| `Ammo` | 23 |
| `Books` / `BooksOnly` / `TCReading` | 19 |
| `Melee Weapons` | 18 |
| `Medical` | 18 |
| `Special Items` | 18 |
| `TCMedical` | 15 |
| `CFDrink/Cooking` | 15 |
| `Basics` | 14 |
| `CFChemicals` | 13 |
| `Chemicals` | 12 |
| `Robotics` | 4 |

> Objects without a `Group` property are giveable via `giveself` but do not appear as a categorized tab in the Creative Menu.

---

### 1. `items.xml` — Holdable Items (1 380 objects)

Defines **all items the player can hold, use, equip, or consume**: weapons, tools, food, drinks, medicine, resources, ammunition, schematics, skill books, vehicle placement items, quest items, etc.

#### `items.xml` — CreativeMode Breakdown

| CreativeMode | Count | Description |
| --- | --- | --- |
| *(default)* | 593 | Standard visible items |
| `None` | 551 | Hidden from Creative Menu (internal items, masters, intermediates) |
| `Player` | 162 | Explicitly player-visible |
| `Dev` | 72 | Developer-only items |
| `Console` | 2 | Console-only items |
| **Total** | **1 380** | |

#### Major Item Categories

**Ranged Weapons** (~35 items) — Firearms, bows, crossbows, rocket launchers:

- Pistols: `gunHandgunT0PipePistol`, `gunHandgunT1Pistol`, `gunHandgunT2Magnum44`, etc.
- Rifles: `gunRifleT0PipeRifle`, `gunRifleT1HuntingRifle`, `gunRifleT3SniperRifle`, etc.
- Shotguns: `gunShotgunT0PipeShotgun`, `gunShotgunT1DoubleBarrel`, `gunShotgunT2PumpShotgun`, etc.
- Automatics: `gunMGT1AK47`, `gunMGT2TacticalAR`, etc.
- Bows: `gunBowT0PrimitiveBow`, `gunBowT1WoodenBow`, `gunBowT2CompoundBow`, `gunXBowT1CompoundCrossbow`, etc.
- Explosives: `gunExplosivesT3RocketLauncher`

**Melee Weapons** (~18 items) — Blades, clubs, spears, knuckles, stun batons:

- Blades: `meleeWpnBladeT0BoneKnife`, `meleeWpnBladeT1HuntingKnife`, `meleeWpnBladeT3Machete`
- Clubs: `meleeWpnClubT0WoodenClub`, `meleeWpnClubT1BaseballBat`, `meleeWpnClubT3SteelClub`
- Spears: `meleeWpnSpearT0StoneSpear`, `meleeWpnSpearT1IronSpear`, `meleeWpnSpearT3SteelSpear`
- Stun batons: `meleeWpnStunBatonT0StunBaton`, `meleeWpnStunBatonT3CattleProd`

**Tools** (~30 items) — Repair tools, axes, pickaxes, shovels, wrenches, augers, chainsaws:

- `meleeToolRepairT0StoneAxe`, `meleeToolRepairT1ClawHammer`, `meleeToolRepairT3Nailgun`
- `meleeToolAxeT1IronFireaxe`, `meleeToolAxeT3SteelAxe`
- `meleeToolPickT1IronPickaxe`, `meleeToolPickT3SteelPickaxe`
- `meleeToolShovelT1IronShovel`, `meleeToolShovelT3SteelShovel`
- `meleeToolWrenchT1Wrench`, `meleeToolWrenchT3Ratchet`
- `meleeToolChainsaw`, `meleeToolAuger`

**Ammunition** (~23 items) — Bullets, arrows, bolts, shells, rockets:

- `ammo9mmBulletBall`, `ammo9mmBulletHP`, `ammo9mmBulletAP`
- `ammo762mmBulletBall`, `ammo762mmBulletHP`, `ammo762mmBulletAP`
- `ammoArrowStone`, `ammoArrowIron`, `ammoArrowSteel`, `ammoArrowExploding`
- `ammoBoltSteel`, `ammoBoltExploding`
- `ammoShotgunSlug`, `ammoShotgunShell`, `ammoShotgunBreachingSlug`
- `ammoRocketHE`, `ammoRocketFrag`

**Food & Drinks** (~66 items) — Raw food, cooked meals, canned food, drinks, smoothies:

- Canned: `foodCanBeef`, `foodCanChili`, `foodCanSoup`, `foodCanPasta`
- Cooked: `foodGrilledMeat`, `foodSteakAndPotato`, `foodHoboStew`
- Smoothies: `foodOasisSmoothie`, `foodFrostbiteSmoothie`, `foodAtomicSmoothie`
- Drinks: `drinkJarBoiledWater`, `drinkJarCoffee`, `drinkJarBeer`, `drinkCanMegaCrush`

**Medicine & Science** (~18 items) — Healing items, antibiotics, medications:

- `medicalBandage`, `medicalFirstAidBandage`, `medicalFirstAidKit`
- `medicalAloeCream`, `medicalSplint`
- `drugAntibiotics`, `drugPainkillers`, `drugVitamins`

**Resources & Materials** (~60 items) — Crafting components, ores, materials:

- `resourceWood`, `resourceRockSmall`, `resourceIron`, `resourceSteel`
- `resourceForgedIron`, `resourceForgedSteel`, `resourceBulletCasing`
- `resourceGunPowder`, `resourceNail`, `resourceDuctTape`, `resourceGlue`

**Books & Schematics** (~20 items) — Skill books, perk magazines, crafting schematics:

- `bookFiremansAlmanacHeat`, `bookNightStalkerStealthDamage`, `bookRangersCraftingBow`
- Each book series grants bonuses from its respective perk line

**Robotic Companions** (4 items) — Automated turrets and drones:

- `gunBotT1JunkSledge`, `gunBotT2JunkTurret`, `gunBotT3JunkDrone`

**Vehicle Placement Items** — Vehicles exist in `vehicles.xml` as behavior definitions, but are **placed through items** defined in `items.xml`:

- `vehicleBicyclePlaceable`, `vehicleMinibikePlaceable`, `vehicleMotorcyclePlaceable`
- `vehicleTruck4x4Placeable`, `vehicleGyrocopterPlaceable`

**Special / Quest Items** (~23 items) — Quest rewards, treasure maps, admin tools:

- Hidden from the Creative Menu but usable via `giveself`

#### Hidden Items (`CreativeMode="None"`, 551 items)

These are not visible in the Creative Menu but can be given via `giveself`. They include:

- **Master templates** — base definitions other items extend (e.g., `meleeWpnBladeMaster`, `gunHandgunMaster`, `partsMaster`)
- **Internal quest items** — `questMaster`, `adminQuestTicketMaster`
- **Intermediate crafting items** — items referenced by recipes but not directly useful
- **Test items** — `TEST_ITEM_00` through `TEST_ITEM_09`
- **Armor masters** — `armorPrimitiveMaster`, `armorLightMaster`, `armorHeavyMaster`

---

### 2. `blocks.xml` — Placeable Blocks (6 289 objects)

Defines **all blocks that exist in the game world**: terrain, building materials, furniture, containers, doors, traps, electrical devices, decorations, vegetation, and POI (Point of Interest) components.

Blocks can also be received into inventory like items (as a held block) and placed in the world.

#### `blocks.xml` — CreativeMode Breakdown

| CreativeMode | Count | Description |
| --- | --- | --- |
| *(default)* | 3 709 | Standard blocks (many are POI-specific) |
| `Dev` | 1 342 | Developer-only blocks |
| `Player` | 814 | Explicitly player-visible in Creative Menu |
| `None` | 419 | Hidden from Creative Menu |
| `Test` | 5 | Test/debug blocks |
| **Total** | **6 289** | |

#### Block Classes

Blocks are not just simple cubes — they have functional classes:

| Block Class | Count | Description |
| --- | --- | --- |
| *(default block)* | 5 649 | Standard placeable blocks with no special behavior |
| `Loot` | 300 | Lootable containers (trash cans, cupboards, safes, etc.) |
| `DoorSecure` | 75 | Lockable/secure doors |
| `Light` | 39 | Light-emitting blocks |
| `Hazard` | 36 | Damaging environmental hazards |
| `CarExplodeLoot` | 28 | Lootable cars that can explode |
| `GameEvent` | 20 | Blocks that trigger game events |
| `SecureLoot` | 13 | Password-protected storage |
| `TrapDoor` | 12 | Trap door blocks |
| `PoweredDoor` | 11 | Electrically controlled doors |
| `CarExplode` | 11 | Exploding vehicles (non-lootable) |
| `VendingMachine` | 6 | Purchasable vending machines |
| `CompositeTileEntity` | 6 | Complex multi-part blocks |
| `Liquidv2` | 5 | Water/liquid blocks |
| `Ladder` | 5 | Climbable ladders |
| Other classes | ~68 | `Stairs`, `Tallgrass`, `QuestLoot`, `TorchHeatMap`, etc. |

#### Block Materials (top 15)

| Material | Count | Description |
| --- | --- | --- |
| `Mmetal` | 166 | Standard metal |
| `Mmetal_weak` | 46 | Weak metal |
| `Mfurniture` | 40 | Furniture |
| `Mmetal_hard` | 38 | Hardened metal |
| `Mmetal_thin` | 38 | Thin metal |
| `Mcloth` | 33 | Cloth/fabric |
| `Mwood_regular` | 30 | Standard wood |
| `Mwood_weak` | 30 | Weak wood |
| `Msteel` | 30 | Steel |
| `MclothStable` | 30 | Stable cloth |
| `Mglass` | 25 | Glass |
| `Mwood` | 24 | Generic wood |
| `Mdirt` | 23 | Dirt/terrain |
| `Msandstone` | 19 | Sandstone |
| `Mplastics` | 18 | Plastic |

#### Player-Visible Block Categories

Blocks with `CreativeMode="Player"` (814 blocks) organized by Group:

| Group | Count | Examples |
| --- | --- | --- |
| *(no group)* | 756 | Various building shapes, doors, windows, frames |
| `Science,TCScience` | 17 | Electrical devices, traps, generators |
| `Decor/Miscellaneous` | 14 | Decorative blocks, signs, flags |
| `Building,advBuilding` | 11 | Advanced construction blocks |
| `Basics,Food/Cooking,Building,advBuilding` | 3 | Campfire, forge, workbench |
| `Building,TCScience,advBuilding` | 3 | Technical building blocks |
| `Resources` | 3 | Resource storage blocks |

#### Developer Blocks (`CreativeMode="Dev"`, 1 342 blocks)

A large portion of blocks are marked Dev-only. These include:

- POI-specific structural blocks used by the world generator
- Variant shapes and damage states of building blocks
- Debug and testing blocks
- Alternative decorations not intended for normal gameplay

---

### 3. `item_modifiers.xml` — Weapon & Tool Mods (107 objects)

Defines **all modification attachments** for weapons, tools, armor, vehicles, and drones. These are inventory objects that can be installed into compatible equipment mod slots.

#### `item_modifiers.xml` — CreativeMode Breakdown

| CreativeMode | Count | Description |
| --- | --- | --- |
| *(default)* | 93 | Visible in Creative Menu |
| `None` | 5 | Hidden (master templates, special mods) |
| `Dev` | 5 | Developer-only mods |
| `Test` | 4 | Test entries (quest supplies, debug mods) |
| **Total** | **107** | |

#### Mod Categories

**Gun Mods** (25 mods) — Attachments for firearms:

- Barrel: `modGunBarrelExtender`, `modGunMuzzleBrake`, `modGunSoundSuppressorSilencer`
- Optics: `modGunScopeSmall`, `modGunScopeMedium`, `modGunScopeLarge`, `modGunReflexSight`, `modGunLaserSight`
- Grips/Stocks: `modGunForegrip`, `modGunRetractingStock`, `modGunBipod`
- Trigger: `modGunTriggerGroupSemi`, `modGunTriggerGroupBurst3`, `modGunTriggerGroupAutomatic`
- Magazine: `modGunMagazineExtender`, `modGunDrumMagazineExtender`, `modGunShotgunTubeExtenderMagazine`
- Shotgun-specific: `modShotgunSawedOffBarrel`, `modGunDuckbill`, `modGunChoke`
- Special: `modGunCrippleEm`, `modGunFlashlight`, `modGunBowPolymerString`, `modGunBowArrowRest`
- Hybrid: `modGunMeleeTheHunter`, `modGunMeleeRadRemover`

**Melee Mods** (16 mods) — Attachments for melee weapons and tools:

- Blades: `modMeleeTemperedBlade`, `modMeleeSerratedBlade`
- Head/Weight: `modMeleeWeightedHead`, `modMeleeStructuralBrace`
- Grips: `modMeleeErgonomicGrip`, `modMeleeFortifyingGrip`
- Club-specific: `modMeleeClubBarbedWire`, `modMeleeClubMetalSpikes`, `modMeleeClubMetalChain`, `modMeleeClubBurningShaft`
- Tool-specific: `modMeleeFiremansAxeMod`, `modMeleeGraveDigger`, `modMeleeBunkerBuster`, `modMeleeIronBreaker`, `modMeleeWoodSplitter`, `modMeleeDiamondTip`
- Stun Baton: `modMeleeStunBatonRepulsor`

**Armor Mods** (22 mods) — Attachments for clothing and armor:

- Insulation: `modArmorInsulatedLinerT1`/`T2`/`T3`
- Storage: `modArmorStoragePocket`, `modArmorDoubleStoragePocket`, `modArmorTripleStoragePocket`, `modArmorQuadStoragePocket`
- Protection: `modArmorPlatingBasic`, `modArmorPlatingReinforced`, `modArmorImpactBracing`
- Stealth: `modArmorMuffledConnectors`, `modArmorAdvancedMuffledConnectors`, `modArmorStealthBoots`
- Utility: `modArmorHelmetLight`, `modArmorNightVision`, `modArmorWaterPurifier`, `modArmorCigar`
- Attribute bonuses: `modArmorPerception`, `modArmorStrength`, `modArmorFortitude`, `modArmorAgility`, `modArmorIntellect`
- Other: `modArmorBandolier`, `modArmorImprovedFittings`, `modArmorCustomizedFittings`, `modArmorTreasureHunter`

**Fuel Tank Mods** (2 mods):

- `modFuelTankSmall`, `modFuelTankLarge`

**Dye Mods** (9 mods) — Color dyes for equipment:

- `modDyeBrown`, `modDyeRed`, `modDyeOrange`, `modDyeYellow`, `modDyeGreen`, `modDyeBlue`, `modDyePurple`, `modDyeBlack`, `modDyePink`
- Base: `modDyeWhite` (hidden, `CreativeMode="None"`)

**Vehicle Mods** (8 mods) — Attachments for vehicles:

- `modVehicleFuelSaver`, `modVehicleOffRoadHeadlights`, `modVehicleSuperCharger`
- `modVehicleExpandedSeat`, `modVehicleReserveFuelTank`
- `modVehiclePlow`, `modVehicleArmor`, `modVehicleStorage`
- Dev: `modVehicleMega`

**Robotic Drone Mods** (5 mods) — Attachments for the Junk Drone:

- `modRoboticDroneArmorPlatingMod`, `modRoboticDroneCargoMod`
- `modRoboticDroneMoraleBoosterMod`, `modRoboticDroneHeadlampMod`
- `modRoboticDroneMedicMod`
- Hidden: `modRoboticDroneWeaponMod`, `modRoboticDroneStunWeaponMod` (`CreativeMode="None"`)

**Developer/Test Mods** (9 mods):

- `modMeleeGunToolDecapitizer`, `modArmorJumpJets`, `modGunBowAdminArcheryReloadRecovery`, `modArmorAdminToughGuyShirt` (Dev)
- `questWhiteRiverSupplies`, `questCassadoreSupplies`, `modGunButtkick3000`, `modGunButtkick4000` (Test)
- `modGeneralMaster` (None — base template)

---

### Files That Do NOT Contain Inventory Objects

The following config files are often confused with item sources but do **not** define giveable objects:

| File | What It Defines | Relationship to Inventory |
| --- | --- | --- |
| `vehicles.xml` | Vehicle **behavior** (speed, physics, fuel, parts) | Vehicles are **placed via items** in `items.xml` (e.g., `vehicleMinibikePlaceable`). The `vehicles.xml` file only defines how they drive. |
| `recipes.xml` | **Crafting recipes** and ingredient lists | References items/blocks from the other files; does not create new objects. |
| `loot.xml` | **Loot tables** — probability tables for container drops | References items/blocks; does not create new objects. |
| `buffs.xml` | **Buffs and debuffs** — status effects on players/entities | Effects, not inventory objects. Some buffs are triggered by consuming items. |
| `progression.xml` | **Skills, perks, attributes** — the leveling tree | Purchased with skill points, not inventory objects. |
| `entityclasses.xml` | **Entities** — zombies, animals, NPCs | Spawned in the world, not placed in inventory. |
| `entitygroups.xml` | **Entity groups** — named spawn lists | References entities; does not create new objects. |
| `gamestages.xml` | **Horde scaling** — enemy waves by game stage | References entity groups; no inventory objects. |
| `spawning.xml` | **Biome/zone spawning rules** | References entity groups; no inventory objects. |
| `traders.xml` | **Trader inventories** and quest offerings | References items/blocks from other files. |
| `qualityinfo.xml` | **Quality tier** stat scaling rules | Modifies existing item stats; no new objects. |
| `Localization.txt` | **Display names and descriptions** for all game objects | Text strings only; no objects. |

---

*Next: [Phase 1 — XML Modlets](phase1_xml_modlets.md)*
