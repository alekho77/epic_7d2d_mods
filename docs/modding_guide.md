# 7 Days to Die — Modding Guide

This guide covers three progressive phases of modding 7 Days to Die, from simple XML-only modlets to full total conversion overhauls. Each phase builds on the previous one.

- **[Phase 1: XML Modlets](phase1_xml_modlets.md)** — Data-only mods using XPath patches on game XML configs. No code, no compilation, no Unity project needed.
- **[Phase 2: Harmony Mods](phase2_harmony_mods.md)** — C# code mods using the HarmonyX patching framework to alter game behavior at runtime.
- **[Phase 3: Total Conversion / Deep Modding](phase3_total_conversion.md)** — Full overhauls involving custom assets (models, textures, sounds, animations), complete UI replacement, world generation, and everything from Phases 1–2 combined.

---

## Game Overview

| Property | Value |
|---|---|
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
|---|---|
| `(root)` | Executables (`7DaysToDie.exe`, `7DaysToDie_EAC.exe`, `7dLauncher.exe`), Unity runtime (`UnityPlayer.dll`), Steam/NVIDIA libraries |
| `7DaysToDie_Data\` | Unity player data: `Managed\` (all .NET DLLs), `Plugins\` (native DLLs), `StreamingAssets\` (Addressables catalog, intro video) |
| `Data\` | Game content: `Config\` (XML configs), `Prefabs\` (POIs), `ItemIcons\`, `Music\`, `Bundles\`, `Addressables\`, `Worlds\`, `Stamps\` |
| `EasyAntiCheat\` | EAC binaries, certs, and localization |
| `Launcher\` | Game launcher translation files |
| `Licenses\` | Third-party library license texts |
| `Logos\` | Splash screen and app icon images |
| `MonoBleedingEdge\` | Mono runtime (`mono-2.0-bdwgc.dll`) and configuration |
| `Mods\` | Installed mods — the game auto-loads every subfolder here |

---

## Modlet Folder Structure

All mods live in the game's `Mods\` folder. Each mod is a self-contained subfolder:

```
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

1. Copy (or symlink) the mod folder into the game's `Mods\` directory.
2. Launch the game **without EAC** (`7DaysToDie.exe` directly, not `7DaysToDie_EAC.exe`).
3. Check `%APPDATA%\7DaysToDie\output_log.txt` for errors.
4. The game validates XML on load — XPath errors are logged with the offending file and line.
5. For rapid iteration, use a dedicated modded copy of the game (environment variable `7D2D_MODED` can point to it).

---

## Key Tools for Modders

| Tool | Purpose | Phase |
|---|---|---|
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
|---|---|
| The Fun Pimps Official Site | https://7daystodie.com/ |
| 7D2D Steam Store Page | https://store.steampowered.com/app/251570/7_Days_to_Die/ |
| TFP Community Forums | https://community.thefunpimps.com/ |
| Game Modification Category | https://community.thefunpimps.com/categories/game-modification.48/ |
| Tutorials & Guides | https://community.thefunpimps.com/forums/tutorials-guides.39/ |
| Mods (Resources) | https://community.thefunpimps.com/resources/ |

### Wikis & Knowledge Bases

| Resource | URL |
|---|---|
| 7 Days to Die Wiki (Fandom) | https://7daystodie.fandom.com/wiki/7_Days_to_Die_Wiki |
| 7D2D Modding Wiki | https://7d2dsdx.github.io/ |
| XPath Modding Explanation Thread (sphereii) | https://community.thefunpimps.com/threads/xpath-modding-explanation-thread.7653/ |

### Community Forums & Hubs

| Resource | URL |
|---|---|
| Nexus Mods — 7D2D | https://www.nexusmods.com/7daystodie |
| Reddit r/7daystodie | https://www.reddit.com/r/7daystodie/ |
| Discord — Official 7D2D | https://discord.gg/7daystodie |
| Unofficial Modding Discord | https://community.thefunpimps.com/threads/unnofficial-modding-discord.23400/ |
| Discord — 7D2D Modding | https://discord.gg/7d2dmodding |

### Modding References

| Resource | URL |
|---|---|
| Harmony Documentation | https://harmony.pardeike.net/articles/intro.html |
| HarmonyX (BepInEx fork) | https://github.com/BepInEx/HarmonyX |
| Sphereii's DMT (Mod Launcher) | https://github.com/SphereII/DMT |
| KhaineGB's Modding Examples | https://community.7daystodie.com/topic/19594-khainesgb-modlets/ |
| SphereII's Modlets & Tutorials | https://community.7daystodie.com/topic/28540-sphereiis-modlets/ |

### Notable Total Conversion Mods (Study Material)

| Mod | Description |
|---|---|
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
- Servers using mods typically disable EAC — clients connecting must also have EAC off.

---

## Quick Reference: What Each Phase Covers

| Capability | Phase 1 (XML) | Phase 2 (Harmony) | Phase 3 (Total Conversion) |
|---|---|---|---|
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

*Next: [Phase 1 — XML Modlets](phase1_xml_modlets.md)*
