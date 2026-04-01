# Phase 3: Total Conversion / Deep Modding

**[Back to Modding Guide](modding_guide.md)** | **Previous: [Phase 2 — Harmony Mods](phase2_harmony_mods.md)**

A total conversion mod (like **Undead Legacy**, **Darkness Falls**, or **Ravenhearst**) uses **all modding layers simultaneously**: XML data patches, Harmony C# patches, custom Unity assets, full UI overhaul, new music/sounds, custom icons, and potentially new prefabs and world generation rules.

This guide covers everything beyond Phases 1–2: the asset pipeline, UI replacement, audio/video, icons, prefabs, world generation, and Unity infrastructure.

> **Prerequisite**: You must be proficient with both Phase 1 (XML modlets) and Phase 2 (Harmony mods) before attempting a total conversion.

---

## What Makes a Total Conversion

| Layer | Technology | Purpose |
| --- | --- | --- |
| Game Data | XML xpath patches | New items, blocks, recipes, buffs, perks, entities, quests, loot, traders, spawning |
| Game Logic | Harmony C# patches | New mechanics, altered AI, custom UI controllers, new console commands, network changes |
| Visuals | Unity AssetBundles + Addressables | New models, textures, animations, shaders, VFX |
| UI | XUi XML + NGUI patches | Redesigned HUD, menus, inventory, crafting screens |
| Audio | WAV files + XML mappings | New music tracks, sound effects, ambient sounds |
| Icons | PNG files | Custom item/block icons |
| World | Prefabs + RWG Config | New POIs, world generation rules, biome layouts |
| Text | Localization.txt | All in-game strings in all languages |

---

## Asset System Overview

The game uses two asset systems:

### Unity Addressables (Primary — Modern)

Location: `Data\Addressables\Standalone\`

The Addressables system is the game's primary asset delivery mechanism. Assets are packed into `.bundle` files, and a catalog maps logical addresses to physical bundle locations.

| Bundle | Contents |
| --- | --- |
| `blocktextureatlases_assets_all.bundle` | Texture atlas for **all** block surfaces — replacing this changes the look of the entire world |
| `terraintextures_assets_all.bundle` | Terrain surface textures (dirt, stone, snow, sand, grass) |
| `shapes_assets_all.bundle` | Block shape geometry (3D mesh data for all block shapes) |
| `effects_assets_all.bundle` | All VFX: explosions, fire, blood, smoke, muzzle flash |
| `shaders_assets_all.bundle` | Custom shaders controlling how surfaces render |
| `prefabs_assets_all.bundle` | Prefab structure asset data |
| `meshdescriptions_assets_all.bundle` | Mesh descriptions (LOD levels, collider shapes) |
| `soundmixers_assets_all.bundle` | Audio mixer configurations (volume balancing) |
| `animations_assets_animations/` | Entity and player animation bundles |
| `automatic_assets_entities/` | Entity model and material bundles (animals, NPCs) |
| `automatic_assets_sounds/` | Sound effect bundles |
| `automatic_assets_generic/` | Generic asset bundles |
| `automatic_assets_dlc/` | DLC content bundles |
| `automatic_assets_twitchdrops/` | Twitch drops content |
| `player_assets_entities/` | Player character model bundles |
| `zombies_assets_entities/` | Zombie model and texture bundles |
| `textures_assets_textures/` | General textures (UI elements, misc) |

**Catalog file**: `7DaysToDie_Data\StreamingAssets\aa\catalog.json` — the master index mapping every asset address to its physical bundle. This is the key to understanding how the game finds and loads any resource.

### Legacy AssetBundles (Secondary)

Location: `Data\Bundles\Standalone\Entities\`

| Bundle | Contents |
| --- | --- |
| `Entities` / `Entities.manifest` | Unity AssetBundle containing entity models (zombies, animals, NPCs) |
| `trees` / `trees.manifest` | Tree and vegetation models |

### Working with Asset Bundles

**Tools needed:**

| Tool | Purpose |
| --- | --- |
| **Unity Editor** (matching game version) | Create new AssetBundles from your custom models/textures. The Unity version must match the game's engine version. |
| **UABE (Unity Asset Bundle Extractor)** | Extract and replace individual assets within existing bundles |
| **AssetStudio** | Browse and preview assets inside bundles (read-only, great for research) |
| **AssetRipper** | Extract assets from bundles into a Unity project |

**Workflow for replacing assets:**

1. Use **AssetStudio** to browse existing bundles and identify the asset you want to replace.
2. Create your replacement asset in the appropriate tool (Blender for models, Photoshop/GIMP for textures).
3. Import into a **Unity project** matching the game's Unity version.
4. Build a new AssetBundle with matching paths, or use **UABE** to inject replacements into the existing bundle.
5. Place modified bundles in your mod folder — the game's mod loader can override Addressable assets.

---

## Full UI Replacement

The game UI is built with **NGUI** (third-party UI framework, not standard Unity UI) plus a custom **XUi** XML layer on top. Total conversions typically overhaul the entire UI.

### UI File Structure

| Path | Controls |
| --- | --- |
| `Data\Config\XUi\windows.xml` | **All in-game HUD windows**: inventory, crafting, loot, map, compass, health bars, hotbar, container windows, vehicle UI, trader UI |
| `Data\Config\XUi\controls.xml` | Reusable UI components: buttons, slots, icons, lists, grids, scrollbars |
| `Data\Config\XUi\styles.xml` | UI styles: colors, font sizes, padding, alignment, anchoring |
| `Data\Config\XUi\xui.xml` | Root XUi file — binds everything together, defines window loading |
| `Data\Config\XUi_Menu\windows.xml` | **Main menu**: start screen, settings, world selection, multiplayer browser |
| `Data\Config\XUi_Menu\controls.xml` | Menu-specific UI components |
| `Data\Config\XUi_Menu\styles.xml` | Menu styles |
| `Data\Config\XUi_Menu\xui.xml` | Menu root file |
| `Data\Config\XUi_Common\controls.xml` | Shared controls used by both HUD and Menu |
| `Data\Config\XUi_Common\styles.xml` | Shared styles |

### UI Modding Approaches

1. **XML-only** (Phase 1): Use xpath patches to modify existing windows, controls, and styles. Good for layout changes, adding elements, restyling.
2. **XML + Custom Controllers** (Phase 2+): Write C# `XUiController` subclasses for new behavior, then bind them to UI elements via XML. Requires Harmony.
3. **Full Replacement**: Replace entire XUi files. Your mod provides complete `windows.xml` etc. instead of xpath patches. Most total conversions do this.

### Key UI Classes (in Assembly-CSharp.dll)

| Class | Purpose |
| --- | --- |
| `XUi` | Main XUi system manager |
| `XUiController` | Base controller — subclass for custom window logic |
| `XUiC_ItemStack` | Single item slot controller |
| `XUiC_RecipeList` | Recipe list in crafting UI |
| `XUiC_MapArea` | Map display controller |
| `XUiC_CraftingQueue` | Crafting queue display |
| `XUiC_CharacterFrameWindow` | Character stats/equipment window |
| `XUiV_*` | View classes (rendering layer) |
| `NGUITools`, `UILabel`, `UISprite`, `UIWidget`, `UIPanel` | NGUI framework classes |

---

## Music and Sound Replacement

### Music Files

Location: `Data\Music\` (~400+ WAV files)

Naming convention: `NNN_<type>_NN.wav` where `NNN` is a numeric index and `<type>` indicates the context:

| Type | When It Plays |
| --- | --- |
| `combat` | During combat encounters |
| `explore` | While exploring the world |
| `suspense` | Tense moments, nearby threats |
| `building` | While building/crafting |
| `ambient` | Background atmosphere |

### Sound Configuration

| File | Controls |
| --- | --- |
| `Data\Config\music.xml` | Maps music tracks to game events, biomes, and situations |
| `Data\Config\sounds.xml` | Maps **all** sound events: weapon firing, melee hits, footsteps, UI clicks, zombie screams, animal sounds, environmental audio, door opens, explosions, etc. |

### Replacing Audio

1. Create your WAV files matching the expected format (44100 Hz, 16-bit PCM is standard).
2. Either replace files in `Data\Music\` or add new files and update `music.xml`/`sounds.xml` mappings.
3. For sounds loaded via Addressables (`automatic_assets_sounds\` bundles), you need to rebuild the bundle.

---

## Icon Replacement

Location: `Data\ItemIcons\` (~5000+ PNG files)

Each item and block can have an icon. The filename corresponds to the `name` attribute in `items.xml` or `blocks.xml`.

- Example: `gunPistol.png` is the icon for `<item name="gunPistol">`.
- Icons are typically 116×116 or 232×232 pixels with transparency.
- Place custom icons in your mod's folder or override existing ones.

For total conversions, you typically create a full custom icon set.

---

## Splash Screens and Branding

| Path | Purpose |
| --- | --- |
| `Logos\SplashScreen.png` | Engine splash screen shown during startup |
| `Logos\Square150x150Logo.png` (and similar) | Application icons for Windows/Store |
| `Logos\StoreLogo.png` | Store listing logo |
| `EasyAntiCheat\SplashScreen.png` | EAC splash (shown when launching with EAC) |
| `Data\Config\loadingscreen.xml` | Loading screen tip text entries |

### Video

| Path | Purpose |
| --- | --- |
| `7DaysToDie_Data\StreamingAssets\Video\TFP_Intro.webm` | Intro video (TFP splash). Replace with your own `.webm` video. |
| `Data\Config\videos.xml` | Video file references used by the game |

---

## Prefabs and World Generation

### Prefab Structure

Location: `Data\Prefabs\`

| Subfolder | Contents |
| --- | --- |
| `POIs\` (~500+ POIs) | **Points of Interest**: houses, stores, factories, hospitals, caves, trader bases. Each POI consists of multiple files |
| `Parts\` | Reusable building components/parts |
| `RWGTiles\` | Road and city tile templates for random world generation |
| `Test\` | Development/test prefabs |

**POI File Format** (each POI has):

| Extension | Purpose |
| --- | --- |
| `.xml` | Metadata (dimensions, biome tags, difficulty tier) |
| `.tts` | Block data (the actual block layout) |
| `.blocks.nim` | Block NIM data |
| `.mesh` | Navigation mesh for AI pathfinding |
| `.jpg` | Preview image |
| `.ins` | Instance data |

### Terrain Stamps

Location: `Data\Stamps\` (~26 files)

`.raw` and `.png` files used by the RWG (Random World Generator) to stamp terrain features: mountains, hills, lakes, rivers, valleys.

### World Generation

| File | Controls |
| --- | --- |
| `Data\Config\rwgmixer.xml` | Random World Generation recipe — defines how cities, roads, biomes, wilderness are laid out |
| `Data\Config\biomes.xml` | Biome definitions: surface blocks, decorations, sub-biomes |
| `Data\Config\spawning.xml` | What entities spawn in each biome/zone |

### Pre-built Worlds

Location: `Data\Worlds\`

| World | Purpose |
| --- | --- |
| `Navezgane/` | The hand-crafted official campaign map. Study its file structure as a reference for custom worlds. |
| `Empty/` | Empty world template |
| `Pregen06k01/`, `Pregen06k02/` | Pre-generated 6K random worlds |
| `Pregen08k01/`, `Pregen08k02/` | Pre-generated 8K random worlds |

---

## Unity Infrastructure Files

These files control the Unity runtime and are relevant when adding custom assemblies or understanding load behavior.

| Path | Purpose |
| --- | --- |
| `7DaysToDie_Data\ScriptingAssemblies.json` | List of assemblies loaded by the scripting runtime. Relevant when adding your own DLLs. |
| `7DaysToDie_Data\RuntimeInitializeOnLoads.json` | Runtime initialization sequence. Important for understanding early-stage patches. |
| `7DaysToDie_Data\boot.config` | Unity runtime boot configuration (scripting backend, GC settings). |
| `7DaysToDie_Data\StreamingAssets\aa\catalog.json` | Addressables catalog — the master index for all addressable assets. |
| `7DaysToDie_Data\StreamingAssets\aa\settings.json` | Addressables system settings. |
| `MonoBleedingEdge\` | Mono runtime environment — `mono-2.0-bdwgc.dll` is the actual C# virtual machine. |

---

## Total Conversion Mod Structure

A full total conversion typically has a structure like this:

```text
Mods\
  MyTotalConversion\
    ModInfo.xml
    Harmony\
      MyTotalConversion.dll         # Core C# patches
      MyTCHelpers.dll               # Additional utility patches
    Config\
      items.xml                     # Complete item overhaul
      blocks.xml                    # Complete block overhaul
      recipes.xml                   # Complete crafting overhaul
      buffs.xml                     # New buff system
      progression.xml               # Custom skill tree
      entityclasses.xml             # New enemies and NPCs
      entitygroups.xml              # New spawn groups
      gamestages.xml                # Custom difficulty scaling
      spawning.xml                  # Custom spawn rules
      loot.xml                      # Custom loot tables
      traders.xml                   # Redesigned traders
      vehicles.xml                  # Custom vehicles
      item_modifiers.xml            # New weapon mods
      quests.xml                    # Custom quest system
      challenges.xml                # Custom challenges
      biomes.xml                    # Biome modifications
      materials.xml                 # Custom materials
      qualityinfo.xml               # Quality tier changes
      worldglobal.xml               # Global settings
      weathersurvival.xml           # Survival mechanics
      sounds.xml                    # Sound mapping changes
      music.xml                     # Music mapping changes
      dialogs.xml                   # NPC dialog trees
      utilityai.xml                 # AI behavior changes
      rwgmixer.xml                  # World generation rules
      Localization.txt              # All text strings
      XUi\
        windows.xml                 # Full HUD replacement
        controls.xml                # Custom UI controls
        styles.xml                  # Custom UI styles
        xui.xml                     # XUi root
      XUi_Menu\
        windows.xml                 # Full menu replacement
        controls.xml
        styles.xml
        xui.xml
    Resources\
      MyCustomBundle.unity3d        # Custom asset bundles
    UIAtlases\
      ItemIconAtlas\                # Custom icon atlas sprites
    ItemIcons\                      # Custom item icons (PNG)
```

---

## Study Order for Total Conversion

Follow this progression to build skills systematically:

| Step | Focus | Key Files / Tools |
| --- | --- | --- |
| **1** | Decompile and study game code | Open `Assembly-CSharp.dll` in dnSpy. Read class hierarchies for items, blocks, entities, UI. |
| **2** | Master XML data system | Study all `Data\Config\*.xml` files. Build complex modlets with cross-file relationships. |
| **3** | Learn the UI system | Study `XUi\`, `XUi_Menu\`, `XUi_Common\` XML files. Decompile `NGUI.dll` to understand the rendering layer. |
| **4** | Understand the asset pipeline | Study `catalog.json` and the `Addressables\Standalone\` bundle structure. Use AssetStudio to browse existing assets. |
| **5** | Create a Unity project | Set up a Unity Editor project matching the game's version. Learn to build custom AssetBundles with models and textures. |
| **6** | Write Harmony patches | Study `0Harmony.dll` API and `0_TFP_Harmony\` as a reference. Write patches for game logic changes. |
| **7** | Build prefabs and worlds | Study POI format, learn TFP's prefab editor. Create custom POIs and world generation rules. |

> **Key insight**: Total conversion mods like Undead Legacy use **all** of these layers simultaneously — Harmony DLLs for behavior changes + XML for data + Unity AssetBundles for visuals + XUi for interface + custom audio/icons/prefabs. Mastering each layer individually before combining them is essential.

---

## Native Plugins (Reference Only)

Location: `7DaysToDie_Data\Plugins\x86_64\`

These are native (non-.NET) DLLs that cannot be Harmony-patched. Listed for completeness:

| File | Origin | Purpose |
| --- | --- | --- |
| `steam_api64.dll` | Steam | Steamworks native API |
| `EOSSDK-Win64-Shipping.dll` | Epic | Epic Online Services native SDK |
| `discord_partner_sdk.dll` | Discord | Discord SDK |
| `InControlNative.dll` | 3rd party | InControl native input handler |
| `lib_burst_generated.dll` | Unity | Burst-compiled native code |
| `BacktraceCrashpadWindows.dll` | 3rd party | Crash capture |
| `ControllerExt.dll` | 3rd party | Extended controller support |
| `Magick.dll` | 3rd party | ImageMagick — image processing |
| `xaudio2_9redist.dll` | Microsoft | XAudio2 audio backend |
| Various Xbox/MS DLLs | Microsoft | Xbox/Store platform support |

---

## EAC and Distribution

- Total conversion mods **always** require EAC to be disabled.
- Most total conversions include a custom launcher or install script.
- Distribution typically happens via **mod launchers** (e.g., the 7D2D Mod Launcher by sphereii) or manual download from Nexus Mods / mod author websites.
- Ensure your mod's `ModInfo.xml` correctly declares all dependencies if you split your conversion into multiple modlets.

---

## Notable Total Conversion References

Study these mods (via their public documentation, not by redistributing their code) to understand approaches used by the community:

| Mod | Scope | What to Study |
| --- | --- | --- |
| **Undead Legacy** | Full overhaul | Complete rework of crafting, progression, entities, UI, assets |
| **Darkness Falls** | Full overhaul | New classes, demons, endgame content, custom entities |
| **Rebirth** | Full overhaul | New mechanics, extended progression, custom AI |
| **War of the Walkers** | Full overhaul | New content, vehicles, NPCs, quests |
| **Ravenhearst** | Full overhaul + custom assets | Extensive UI overhaul, new models, hardcore survival mechanics |

---

*[Back to Modding Guide](modding_guide.md)* | *Previous: [Phase 2 — Harmony Mods](phase2_harmony_mods.md)*
