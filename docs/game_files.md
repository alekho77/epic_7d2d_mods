Here's the comprehensive table of the 7d2dmods game installation, with repetitive bulk assets grouped for readability.
Comprehensive table of the game installation has been compiled, covering all directories and files with origin classification, purpose descriptions, and ILSpy/dnSpy study recommendations for modding.

---

## 7 Days to Die — File Inventory (7d2dmods)

### Legend

| Origin Code | Meaning |
|---|---|
| **TFP** | The Fun Pimps (game developer) |
| **Unity** | Unity engine / Unity Technologies |
| **.NET** | Mono/.NET framework |
| **Steam** | Valve / Steamworks |
| **3rd** | Third-party library |
| **EAC** | Easy Anti-Cheat (Epic) |
| **NVIDIA** | NVIDIA Corporation |
| **MS** | Microsoft (Xbox GDK) |

### ILSpy/dnSpy Priority

| Rating | Meaning |
|---|---|
| **ESSENTIAL** | Must study — main game logic, core to modding |
| **USEFUL** | Contains APIs you may want to hook via Harmony |
| **REFERENCE** | Helpful to understand if you hit edge cases |
| **SKIP** | Not useful for modding |

---

### Root Directory (7d2dmods)

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `7DaysToDie.exe` | TFP | Main game executable (launches without EAC) | SKIP (native) |
| `7DaysToDie_EAC.exe` | TFP/EAC | Game launcher with EAC protection (default Steam launch) | SKIP (native) |
| `7dLauncher.exe` | TFP | Game launcher/patcher UI | SKIP (native) |
| `UnityCrashHandler64.exe` | Unity | Handles Unity engine crash dumps | SKIP |
| `UnityPlayer.dll` | Unity | Unity engine core runtime (native C++) | SKIP (native) |
| `UnityPlayer_Win64_player_mono_x64.pdb` | Unity | Debug symbols for UnityPlayer.dll | SKIP |
| `UnityCrashHandler64.pdb` | Unity | Debug symbols for crash handler | SKIP |
| `WindowsPlayer_player_Master_mono_x64.pdb` | Unity/TFP | Debug symbols for master player build | SKIP |
| `nvngx_dlss.dll` | NVIDIA | DLSS (Deep Learning Super Sampling) library | SKIP (native) |
| `NVUnityPlugin.dll` | NVIDIA | NVIDIA Unity integration plugin | SKIP (native) |
| `steamclient64.dll` | Steam | Steam client runtime library | SKIP (native) |
| `steam_appid.txt` | Steam | Steam application ID (text: `251570`) | SKIP |
| `tier0_s64.dll` | Steam | Valve low-level runtime library | SKIP (native) |
| `vstdlib_s64.dll` | Steam | Valve standard library runtime | SKIP (native) |
| `serverconfig.xml` | TFP | Dedicated server configuration template | SKIP (XML — useful for server admins) |
| `platform.cfg` | TFP | Platform-specific settings | SKIP |
| `startdedicated.bat` | TFP | Launch script for dedicated server | SKIP |
| `MicrosoftGame.Config` | MS | Microsoft Store / Xbox packaging config | SKIP |
| `installscript.vdf` | Steam | Steam install/uninstall script | SKIP |

---

### `7DaysToDie_Data\` (Unity Player Data)

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `app.info` | Unity | Application metadata (company, product name) | SKIP |
| `boot.config` | Unity | Unity boot parameters (scripting backend, GC settings) | SKIP |
| `data.unity3d` | Unity | Packed Unity asset data (scenes, shaders, resources) | SKIP (binary asset) |
| `resources.resource` | Unity | Packed resource assets | SKIP (binary asset) |
| `sharedassets2.resource` | Unity | Shared assets pack | SKIP (binary asset) |
| `RuntimeInitializeOnLoads.json` | Unity | Runtime initialization sequence definitions | REFERENCE |
| `ScriptingAssemblies.json` | Unity | List of assemblies loaded by the scripting runtime | REFERENCE |

---

### `7DaysToDie_Data\Managed\` — .NET / Managed DLLs

This is the **most important directory for modders**. All C# game logic lives here.

#### TFP Game Assemblies (MUST STUDY)

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `Assembly-CSharp.dll` | **TFP** | **MAIN GAME CODE** — all items, blocks, entities, AI, UI, networking, world gen, buffs, crafting, quests, etc. | **ESSENTIAL** |
| `Assembly-CSharp-firstpass.dll` | **TFP** | Early-init code (loaded before main assembly — utility classes, base types) | **ESSENTIAL** |
| `LogLibrary.dll` | TFP | Custom TFP logging framework | USEFUL |

#### Unity Engine Modules (~40 DLLs)

| Path Pattern | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `UnityEngine.dll` | Unity | Unity engine facade/entry point | REFERENCE |
| `UnityEngine.CoreModule.dll` | Unity | Core types: `GameObject`, `MonoBehaviour`, `Transform`, `Component` | REFERENCE |
| `UnityEngine.PhysicsModule.dll` | Unity | Physics, raycasts, colliders, rigidbodies | REFERENCE |
| `UnityEngine.AnimationModule.dll` | Unity | Animation system (Animator, AnimationClip) | SKIP |
| `UnityEngine.AudioModule.dll` | Unity | Audio playback, `AudioSource`, `AudioClip` | SKIP |
| `UnityEngine.UI.dll` | Unity | Built-in Unity UI (Canvas, Image, Text) | REFERENCE |
| `UnityEngine.UIModule.dll` | Unity | Low-level UI module | SKIP |
| `UnityEngine.UIElementsModule.dll` | Unity | UIToolkit (not used by the game UI) | SKIP |
| `UnityEngine.IMGUIModule.dll` | Unity | Immediate-mode GUI | SKIP |
| `UnityEngine.InputLegacyModule.dll` | Unity | Legacy Input class | SKIP |
| `UnityEngine.TextRenderingModule.dll` | Unity | Text rendering (Font, TextMesh) | SKIP |
| `UnityEngine.ParticleSystemModule.dll` | Unity | Particle effects | SKIP |
| `UnityEngine.TerrainModule.dll` | Unity | Terrain system | SKIP |
| `UnityEngine.TerrainPhysicsModule.dll` | Unity | Terrain colliders | SKIP |
| `UnityEngine.AssetBundleModule.dll` | Unity | AssetBundle loading | REFERENCE |
| `UnityEngine.JSONSerializeModule.dll` | Unity | JSON utility | SKIP |
| `UnityEngine.ImageConversionModule.dll` | Unity | Texture encoding/decoding | SKIP |
| `UnityEngine.TextCoreTextEngineModule.dll` | Unity | TextMeshPro underlying engine | SKIP |
| `UnityEngine.TextCoreFontEngineModule.dll` | Unity | Font rendering engine | SKIP |
| Other `UnityEngine.*.dll` (~22 more) | Unity | Networking, VR, Video, Vehicles, AI, Subsystems, etc. | SKIP |

#### Unity Packages

| Path Pattern | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `Unity.TextMeshPro.dll` | Unity | TextMeshPro text rendering (game uses this for UI text) | SKIP |
| `Unity.Addressables.dll` | Unity | Addressable Asset System (asset loading/management) | REFERENCE |
| `Unity.ResourceManager.dll` | Unity | Resource management for Addressables | SKIP |
| `Unity.Burst.dll` / `Unity.Burst.Unsafe.dll` | Unity | Burst compiler runtime (high-perf math/ECS) | SKIP |
| `Unity.Collections.dll` | Unity | Native collections (NativeArray, etc.) | SKIP |
| `Unity.Mathematics.dll` | Unity | High-perf math library | SKIP |
| `Unity.Animation.Rigging.dll` | Unity | Animation rigging constraints | SKIP |
| `Unity.Postprocessing.Runtime.dll` | Unity | Post-processing stack (bloom, AO, etc.) | SKIP |
| `Unity.TerrainTools.dll` | Unity | Terrain tools runtime | SKIP |
| `Unity.RenderPipelines.Core.Runtime.dll` | Unity | Render pipeline core | SKIP |
| `Unity.Jobs.dll` | Unity | C# Job System | SKIP |
| `Unity.Profiling.Core.dll` | Unity | Profiling API | SKIP |
| `Unity.InputSystem.dll` | Unity | New Input System package | SKIP |

#### .NET Framework Assemblies

| Path Pattern | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `mscorlib.dll` | .NET | Core .NET runtime (object, string, collections) | SKIP |
| `System.dll` | .NET | Core System classes (IO, Net, Config) | SKIP |
| `System.Core.dll` | .NET | LINQ, Expressions, dynamic types | SKIP |
| `System.Xml.dll` / `System.Xml.Linq.dll` | .NET | XML parsing (used by the game for configs) | SKIP |
| `System.Net.Http.dll` | .NET | HTTP client | SKIP |
| `System.Data.dll` | .NET | ADO.NET data access | SKIP |
| Other `System.*.dll` (~15 more) | .NET | Various framework libraries | SKIP |
| `Mono.Security.dll` | .NET | Mono security/crypto | SKIP |
| `netstandard.dll` | .NET | .NET Standard 2.0 shim | SKIP |

#### Third-Party Libraries (Modding-Relevant)

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `0Harmony.dll` | 3rd (HarmonyX) | **Harmony patching framework** — your Harmony mods depend on this | **ESSENTIAL** |
| `Mono.Cecil.dll` / `MonoMod.*.dll` | 3rd | Cecil IL manipulation + MonoMod (used by Harmony internally) | REFERENCE |
| `AstarPathfindingProject.dll` | 3rd | A* Pathfinding Project — NPC/zombie navigation | USEFUL |
| `Pathfinding.ClipperLib.dll` | 3rd | Polygon clipping for pathfinding mesh generation | SKIP |
| `Pathfinding.Ionic.Zip.dll` | 3rd | Zip compression for path data | SKIP |
| `Pathfinding.JsonFx.dll` | 3rd | JSON serialization for path data | SKIP |
| `NGUI.dll` | 3rd | NGUI — game's primary UI system (not Unity UI!) | **USEFUL** |
| `InControl.dll` | 3rd | Controller/input mapping framework | REFERENCE |
| `NCalc.dll` | 3rd | Math expression evaluator (used in buff/progression formulas) | USEFUL |
| `Newtonsoft.Json.dll` | 3rd | JSON.NET serialization | SKIP |
| `Utf8Json.dll` | 3rd | High-perf JSON serializer | SKIP |
| `MemoryPack.Core.dll` / `MemoryPack.dll` | 3rd | Binary serialization (save data, network packets) | REFERENCE |
| `LiteNetLib.dll` | 3rd | UDP networking library (multiplayer) | REFERENCE |
| `Noemax.GZip.dll` | 3rd | GZip compression | SKIP |
| `Antlr3.Runtime.dll` | 3rd | ANTLR parser runtime (used by NCalc) | SKIP |
| `Backtrace.Unity.dll` | 3rd | Crash reporting SDK | SKIP |
| `zxing.unity.dll` | 3rd | QR/barcode scanning (Twitch integration) | SKIP |
| `enum2int.dll` | 3rd | Fast enum-to-int conversion | SKIP |

#### Platform SDKs

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `com.rlabrecque.steamworks.net.dll` | 3rd | Steamworks.NET — Steam API wrapper (achievements, lobbies, workshop) | REFERENCE |
| `Discord.Sdk.dll` | 3rd | Discord Rich Presence / Game SDK | SKIP |
| `com.epicgames.eos.dll` / `Epic.OnlineServices.dll` | 3rd | Epic Online Services (cross-platform networking) | SKIP |
| `XblPCSandbox.dll` | MS | Xbox Live PC sandbox | SKIP |
| `Unity.Microsoft.GDK.dll` | MS | Xbox/MS Store GDK integration | SKIP |

#### Graphics & Effects

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `com.thenakeddev.dlss.Runtime.dll` | 3rd | DLSS Unity integration | SKIP |
| `com.thenakeddev.fsr.Runtime.dll` | 3rd | AMD FSR Unity integration | SKIP |
| `HBAO.Runtime.dll` | 3rd | Horizon-Based Ambient Occlusion | SKIP |
| `ScreenSpaceReflections.dll` | 3rd | Screen-space reflections effect | SKIP |

---

### `7DaysToDie_Data\Plugins\x86_64\` — Native Plugins

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `steam_api64.dll` | Steam | Steamworks native API | SKIP (native) |
| `EOSSDK-Win64-Shipping.dll` | 3rd (Epic) | Epic Online Services native SDK | SKIP (native) |
| `discord_partner_sdk.dll` | 3rd (Discord) | Discord SDK native lib | SKIP (native) |
| `InControlNative.dll` | 3rd | InControl native input handler | SKIP (native) |
| `lib_burst_generated.dll` | Unity | Burst-compiled native code | SKIP (native) |
| `BacktraceCrashpadWindows.dll` | 3rd | Backtrace crash capture | SKIP (native) |
| `backtrace_native_xbox.dll` | 3rd | Xbox-specific Backtrace | SKIP (native) |
| `crashpad_handler.dll` | 3rd | Crashpad crash handler | SKIP (native) |
| `ControllerExt.dll` | 3rd | Extended controller support | SKIP (native) |
| `getrss.dll` | 3rd | Memory usage monitoring (RSS) | SKIP (native) |
| `Magick.dll` | 3rd | ImageMagick — image processing | SKIP (native) |
| `xaudio2_9redist.dll` | MS | XAudio2 redistributable (audio backend) | SKIP (native) |
| `XCurl.dll` | MS | Xbox HTTP/CURL library | SKIP (native) |
| `XGameRuntime.Thunks.dll` | MS | Xbox Game Runtime thunks | SKIP (native) |
| `XInputInterface64.dll` | MS | XInput (gamepad input) | SKIP (native) |
| `Microsoft.Xbox.Services.GDK.C.Thunks.dll` | MS | Xbox services GDK thunks | SKIP (native) |

---

### `7DaysToDie_Data\StreamingAssets\`

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `aa/catalog.json` | Unity | Addressables catalog (asset addresses → bundle paths) | SKIP |
| `aa/settings.json` | Unity | Addressables system settings | SKIP |
| `aa/shaders.json` | Unity | Shader variant tracking data | SKIP |
| `aa/AddressablesLink/` (folder) | Unity | Links between Addressables and resources | SKIP |
| `Video/TFP_Intro.webm` | TFP | The Fun Pimps splash/intro video | SKIP |

---

### `7DaysToDie_Data\Resources\`

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `unity default resources` | Unity | Built-in Unity default assets (shaders, materials, fonts) | SKIP |

---

### `Data\` — Game Content Root

#### `Data\Config\` — **XML Configuration Files (CRITICAL for Modlets)**

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `items.xml` | TFP | All holdable items: weapons, tools, consumables, resources, ammo + all properties | SKIP (XML — **key modlet target**) |
| `blocks.xml` | TFP | All placeable blocks, doors, traps, terrain, workstations | SKIP (XML — **key modlet target**) |
| `recipes.xml` | TFP | Crafting recipes, ingredients, required stations | SKIP (XML — **key modlet target**) |
| `loot.xml` | TFP | Loot containers, loot groups, probability tables, quest loot | SKIP (XML — **key modlet target**) |
| `entityclasses.xml` | TFP | Zombie, animal, NPC class definitions + AI/stats | SKIP (XML — **key modlet target**) |
| `entitygroups.xml` | TFP | Entity spawn groups used by gamestages/spawning | SKIP (XML — **key modlet target**) |
| `buffs.xml` | TFP | Buffs, debuffs, status effects and their triggers/actions | SKIP (XML — **key modlet target**) |
| `progression.xml` | TFP | Skills, perks, attributes, level scaling | SKIP (XML — **key modlet target**) |
| `gamestages.xml` | TFP | Horde night waves, spawn scaling by gamestage | SKIP (XML — **key modlet target**) |
| `spawning.xml` | TFP | Biome/zone spawning rules | SKIP (XML — **key modlet target**) |
| `traders.xml` | TFP | Trader inventories, tiers, restock settings | SKIP (XML — **key modlet target**) |
| `vehicles.xml` | TFP | Vehicle definitions and properties | SKIP (XML — modlet target) |
| `item_modifiers.xml` | TFP | Weapon/tool mod attachments (mods, dyes) | SKIP (XML — modlet target) |
| `quests.xml` | TFP | Quest definitions, objectives, rewards | SKIP (XML — modlet target) |
| `biomes.xml` | TFP | Biome definitions, surfaces, decoration spawns | SKIP (XML — modlet target) |
| `sounds.xml` | TFP | Sound event mappings (action → audio file) | SKIP (XML — modlet target) |
| `materials.xml` | TFP | Block material properties (hardness, resistance, particles) | SKIP (XML — modlet target) |
| `shapes.xml` | TFP | Block shape definitions (3D mesh shapes) | SKIP (XML) |
| `qualityinfo.xml` | TFP | Item quality tiers and stat scaling per tier | SKIP (XML — modlet target) |
| `worldglobal.xml` | TFP | Global world settings (day/night cycle, weather) | SKIP (XML — modlet target) |
| `weathersurvival.xml` | TFP | Weather and survival stat effects (temperature, wetness) | SKIP (XML) |
| `painting.xml` | TFP | Block painting textures | SKIP (XML) |
| `nav_objects.xml` | TFP | Minimap/compass navigation icons | SKIP (XML) |
| `archetypes.xml` | TFP | Entity archetypes (base templates) | SKIP (XML) |
| `dialogs.xml` | TFP | NPC dialog trees (trader conversations) | SKIP (XML) |
| `npc.xml` | TFP | NPC-specific settings | SKIP (XML) |
| `challenges.xml` | TFP | In-game challenges and objectives | SKIP (XML) |
| `events.xml` | TFP | Game event triggers | SKIP (XML) |
| `gameevents.xml` | TFP | Game event responses | SKIP (XML) |
| `rwgmixer.xml` | TFP | Random World Generation rules | SKIP (XML) |
| `utilityai.xml` | TFP | AI utility scoring and behaviour trees | SKIP (XML) |
| `misc.xml` | TFP | Miscellaneous global game variables | SKIP (XML) |
| `physicsbodies.xml` | TFP | Ragdoll/physics body definitions | SKIP (XML) |
| `ui_display.xml` | TFP | Stat/property display labels for the UI | SKIP (XML) |
| `music.xml` | TFP | Background music event mappings | SKIP (XML) |
| `subtitles.xml` | TFP | Subtitle entries for audio events | SKIP (XML) |
| `dmscontent.xml` | TFP | Diersville map static content definitions | SKIP (XML) |
| `twitch.xml` / `twitch_events.xml` | TFP | Twitch integration event definitions | SKIP (XML) |
| `videos.xml` | TFP | Intro/cutscene video references | SKIP (XML) |
| `loadingscreen.xml` | TFP | Loading screen tips | SKIP (XML) |
| `blockplaceholders.xml` | TFP | Block placeholder substitution rules | SKIP (XML) |
| `Localization.txt` | TFP | **All in-game strings** (TSV: key → language columns) | SKIP (text — **key modlet target**) |
| `BlockUpdates.csv` | TFP | Block upgrade/downgrade transition table | SKIP (CSV) |
| `OversizedConversionTargets.txt` | TFP | Oversized block conversion list | SKIP (text) |
| `Stealth.txt` | TFP | Stealth system parameters | SKIP (text) |
| `XML.txt` | TFP | Notes on the XML patching system | SKIP (doc) |
| `XUi/*.xml` | TFP | HUD and in-game UI: windows, controls, styles | SKIP (XML — modlet target for UI mods) |
| `XUi_Common/*.xml` | TFP | Shared UI components | SKIP (XML) |
| `XUi_Menu/*.xml` | TFP | Main menu UI | SKIP (XML) |

#### Bulk Asset Directories

| Path | Origin | Contents | ILSpy? |
|---|---|---|---|
| `Data\ItemIcons\` (~5000+ files) | TFP | PNG icon sprites for every item/block in the game (e.g., `gunPistol.png`, `drinkJarBoiledWater.png`) | SKIP |
| `Data\Music\` (~400+ files) | TFP | WAV music tracks: combat, exploration, suspense, building, ambient (numbered series like `000_combat_01.wav`) | SKIP |
| `Data\Bluffs\` (2 files) | TFP | `bluff1.tga`, `bluff2.tga` — terrain bluff textures | SKIP |
| `Data\Stamps\` (~26 files) | TFP | `.raw`/`.png` terrain generation stamps (mountains, hills, lakes, rivers, valleys) | SKIP |
| `Data\UMATextures\` | TFP | Empty directory (UMA character textures placeholder) | SKIP |

#### `Data\Prefabs\` — World Prefab Structures

| Subfolder | Origin | Contents | ILSpy? |
|---|---|---|---|
| `POIs\` (~500+ POIs, each with 4-6 files) | TFP | **Points of Interest**: houses, stores, factories, farms, caves, offices, hospitals, trader bases, etc. Each POI has: `.xml` (metadata), `.tts` (block data), `.blocks.nim` (block NIM), `.mesh` (nav mesh), `.jpg` (preview), `.ins` (instance data) | SKIP |
| `Parts\` | TFP | Reusable prefab components/building parts | SKIP |
| `RWGTiles\` | TFP | Random World Generation road/city tiles | SKIP |
| `Test\` | TFP | Test/development prefabs | SKIP |

#### `Data\Bundles\Standalone\Entities\`

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `Entities` / `Entities.manifest` | TFP | Unity AssetBundle containing entity models (zombies, animals, NPCs) | SKIP (binary asset) |
| `trees` / `trees.manifest` | TFP | Unity AssetBundle containing tree/vegetation models | SKIP (binary asset) |

#### `Data\Addressables\Standalone\`

| Path Pattern | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `*_unitybuiltinshaders.bundle` | Unity | Built-in shader variants | SKIP |
| `animations_assets_animations/` | TFP | Entity/player animation bundles | SKIP |
| `automatic_assets_entities/` | TFP | Entity model/material bundles | SKIP |
| `automatic_assets_sounds/` | TFP | Sound effect bundles | SKIP |
| `automatic_assets_generic/` | TFP | Generic asset bundles | SKIP |
| `automatic_assets_dlc/` | TFP | DLC content bundles | SKIP |
| `automatic_assets_other/` | TFP | Miscellaneous asset bundles | SKIP |
| `automatic_assets_twitchdrops/` | TFP | Twitch drops content bundles | SKIP |
| `blocktextureatlases_assets_all.bundle` | TFP | Block texture atlas (all block surface textures) | SKIP |
| `effects_assets_all.bundle` | TFP | VFX/particle effect bundles | SKIP |
| `meshdescriptions_assets_all.bundle` | TFP | Mesh description data | SKIP |
| `player_assets_entities/` | TFP | Player model bundles | SKIP |
| `prefabs_assets_all.bundle` | TFP | Prefab structure bundles | SKIP |
| `shaders_assets_all.bundle` | TFP | Custom shader bundles | SKIP |
| `shapes_assets_all.bundle` | TFP | Block shape geometry bundles | SKIP |
| `soundmixers_assets_all.bundle` | TFP | Audio mixer settings | SKIP |
| `terraintextures_assets_all.bundle` | TFP | Terrain surface textures | SKIP |
| `textures_assets_textures/` | TFP | General texture bundles | SKIP |
| `zombies_assets_entities/` | TFP | Zombie-specific model bundles | SKIP |

#### `Data\Worlds\`

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `Empty/` | TFP | Empty world template | SKIP |
| `Navezgane/` | TFP | Hand-crafted campaign map | SKIP |
| `Playtesting/` | TFP | QA/testing world | SKIP |
| `Pregen06k01/`, `Pregen06k02/` | TFP | Pre-generated 6k random worlds | SKIP |
| `Pregen08k01/`, `Pregen08k02/` | TFP | Pre-generated 8k random worlds | SKIP |

---

### `EasyAntiCheat\`

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `EasyAntiCheat_EOS_Setup.exe` | EAC | EAC installer/setup | SKIP |
| `install.bat` / `uninstall.bat` | EAC | EAC install/uninstall scripts | SKIP |
| `Settings.json` | EAC | EAC configuration | SKIP |
| `SplashScreen.png` | EAC | EAC loading splash image | SKIP |
| `Certificates/` (3 files) | EAC | `base.bin`, `base.cer`, `runtime.conf` — EAC integrity certs | SKIP |
| `Licenses/` | EAC | EAC license files | SKIP |
| `Localization/` (20 `.cfg` files) | EAC | EAC UI translations (ar_sa, cs_cz, de_de, en_us, es_es, fr_fr, ja_ja, ko_kr, ru_ru, zh_cn, etc.) | SKIP |

---

### `Launcher\`

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `7dLauncher.po` / `7dLauncher.de.po` | TFP | Launcher UI translation files (English, German) | SKIP |

---

### `Licenses\` (19 `.txt` files)

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| License files for: AmplifyMotion, ANTLR3, Backtrace, Cecil, Crc32.NET, GameSense, HarmonyX, InControl, LibNoise, LiteNetLib, MemoryPack, MonoMod, NCalc, PathfindingProject, SharpEXR, Steamworks.NET, Utf8Json, ZXing, plus standard License.txt | Various (3rd) | Third-party library license texts | SKIP |

---

### `Logos\`

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `SplashScreen.png` | TFP | Game splash screen image | SKIP |
| `Square150x150Logo.png` etc. (5 PNG files) | TFP | App icon tiles for Windows/Store | SKIP |

---

### `MonoBleedingEdge\`

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `EmbedRuntime/mono-2.0-bdwgc.dll` | .NET (Mono) | Mono runtime with Boehm-Demers-Weiser GC (the actual C# VM) | SKIP (native) |
| `EmbedRuntime/MonoPosixHelper.dll` | .NET (Mono) | POSIX helper for Mono | SKIP (native) |
| `etc/mono/` | .NET (Mono) | Mono configuration files (machine.config, assembly remapping) | SKIP |

---

### Mods — Installed Mods (30 folders)

| Path | Origin | Purpose | ILSpy? |
|---|---|---|---|
| `0_TFP_Harmony/` | TFP | Official TFP Harmony mod framework (loaded first by `0_` prefix) | USEFUL (contains TFP Harmony patches) |

---

### Summary: What to Study for Modding

| Priority | Files | Why |
|---|---|---|
| **#1 ESSENTIAL** | `Assembly-CSharp.dll` | All game classes, methods, fields — the core of all Harmony patches |
| **#2 ESSENTIAL** | `Assembly-CSharp-firstpass.dll` | Base utility classes, loaded first |
| **#3 ESSENTIAL** | `0Harmony.dll` | Understand the Harmony API you'll use for patches |
| **#4 USEFUL** | `NGUI.dll` | Game UI system — needed for UI mods |
| **#5 USEFUL** | `NCalc.dll` | Expression evaluator used in buff/progression formulas |
| **#6 USEFUL** | `AstarPathfindingProject.dll` | AI navigation — relevant for entity behavior mods |
| **#7 USEFUL** | `0_TFP_Harmony/` mod | TFP's own Harmony patches — great reference examples |
| **#8 REFERENCE** | `Data\Config\*.xml` (all) | The XML configs are your primary modlet targets — study them as text, not in decompiler |

---

A table of all files and directories relevant for building a total conversion mod (like Undead Legacy) has been provided, organized by category: C# code, UI system, asset bundles, audio/video, icons, XML game data, world prefabs, and Unity infrastructure.
Для тотальной конверсии уровня Undead Legacy нужно знать гораздо больше, чем для простых модлетов. Вот целевая карта:

---

## Файлы и папки для изучения: Total Conversion Mod

### 1. Код игры (C# / Harmony) — без этого глубокие изменения невозможны

| Путь | Зачем изучать |
|---|---|
| `7DaysToDie_Data\Managed\Assembly-CSharp.dll` | **Главный код игры.** Все классы: крафт, инвентарь, AI, UI-контроллеры, загрузка ассетов, сетевой код. Декомпилировать в dnSpy/ILSpy и изучать структуру классов. Harmony-патчи пишутся именно сюда |
| `7DaysToDie_Data\Managed\Assembly-CSharp-firstpass.dll` | Базовые утилиты, загружаемые до основного кода. Часто содержит фундаментальные типы |
| `7DaysToDie_Data\Managed\0Harmony.dll` | API Harmony — знать `[HarmonyPatch]`, `Prefix`, `Postfix`, `Transpiler` |
| `7DaysToDie_Data\Managed\NGUI.dll` | Движок UI игры — **не** стандартный Unity UI. Без понимания NGUI нельзя делать глубокие изменения интерфейса |
| `7DaysToDie_Data\Managed\NCalc.dll` | Парсер математических выражений — используется в `buffs.xml` и `progression.xml`. Нужно знать синтаксис для сложных формул |
| `7DaysToDie_Data\Managed\AstarPathfindingProject.dll` | Навигация AI. Если меняешь размеры/поведение зомби — нужно понимать навмеш |
| `Mods\0_TFP_Harmony\` | Официальные Harmony-патчи TFP — **образец** как правильно патчить |

### 2. Полная замена UI / Меню / HUD

| Путь | Зачем изучать |
|---|---|
| `Data\Config\XUi\windows.xml` | **Все окна** игрового HUD: инвентарь, крафт, хот-бар, карта, компас, полоски здоровья, окна контейнеров |
| `Data\Config\XUi\controls.xml` | Переиспользуемые UI-компоненты (кнопки, слоты, иконки, списки) |
| `Data\Config\XUi\styles.xml` | Стили UI: цвета, размеры шрифтов, отступы, привязки |
| `Data\Config\XUi\xui.xml` | Корневой файл XUi — связывает всё вместе, определяет загрузку окон |
| `Data\Config\XUi_Menu\windows.xml` | **Главное меню** — экран запуска, настройки, выбор мира, мультиплеер |
| `Data\Config\XUi_Menu\controls.xml` | UI-компоненты главного меню |
| `Data\Config\XUi_Menu\styles.xml` | Стили главного меню |
| `Data\Config\XUi_Menu\xui.xml` | Корневой файл меню |
| `Data\Config\XUi_Common\controls.xml` | Общие контролы между HUD и Menu |
| `Data\Config\XUi_Common\styles.xml` | Общие стили |

### 3. Замена визуала: текстуры, меши, модели, эффекты

| Путь | Зачем изучать |
|---|---|
| `Data\Addressables\Standalone\` (весь каталог) | **Основная система ассетов.** Все текстуры, модели, анимации, эффекты загружаются через Addressables. Нужно изучить структуру бандлов и научиться заменять содержимое |
| `  blocktextureatlases_assets_all.bundle` | Атлас текстур ВСЕХ блоков — замена внешнего вида мира |
| `  terraintextures_assets_all.bundle` | Текстуры поверхности terrain — земля, камень, снег, песок |
| `  shapes_assets_all.bundle` | Геометрия форм блоков — замена 3D-форм |
| `  effects_assets_all.bundle` | Все VFX: взрывы, огонь, кровь, дым |
| `  shaders_assets_all.bundle` | Кастомные шейдеры — управление рендерингом |
| `  prefabs_assets_all.bundle` | Ассеты префабов |
| `  zombies_assets_entities\` | Модели и текстуры зомби |
| `  player_assets_entities\` | Модели и текстуры игрока |
| `  automatic_assets_entities\` | Прочие сущности (животные, NPC) |
| `  animations_assets_animations\` | Все анимации (движение, атаки, смерть) |
| `  automatic_assets_sounds\` | Звуковые бандлы |
| `  textures_assets_textures\` | Прочие текстуры (UI-элементы, иконки, разное) |
| `  meshdescriptions_assets_all.bundle` | Описания мешей (LOD, коллайдеры) |
| `  soundmixers_assets_all.bundle` | Аудио-миксеры (баланс громкости) |
| `Data\Bundles\Standalone\Entities\` | Старая система бандлов — модели entity + деревья |
| `7DaysToDie_Data\StreamingAssets\aa\catalog.json` | **Каталог Addressables** — карта: какой ассет лежит в каком бандле. Ключ к пониманию, как игра находит ресурсы |

### 4. Замена музыки, звуков, видео

| Путь | Зачем изучать |
|---|---|
| `Data\Music\` (~400+ WAV) | Все музыкальные треки. Структура именования: `NNN_<тип>_NN.wav` (combat, explore, suspense, building) |
| `Data\Config\music.xml` | Маппинг: какая музыка играет при каком событии/биоме |
| `Data\Config\sounds.xml` | Маппинг ВСЕХ звуковых событий: выстрелы, удары, шаги, UI-клики, крики зомби |
| `7DaysToDie_Data\StreamingAssets\Video\TFP_Intro.webm` | Интро-видео (заставка TFP) — заменяется своим видео |
| `Data\Config\videos.xml` | Список видео-файлов, воспроизводимых игрой |

### 5. Замена иконок и splash-экранов

| Путь | Зачем изучать |
|---|---|
| `Data\ItemIcons\` (~5000+ PNG) | Иконки ВСЕХ предметов/блоков. Имя файла = `name` из `items.xml`/`blocks.xml` |
| `Logos\SplashScreen.png` | Splash-экран при запуске движка |
| `Logos\Square*.png`, `Logos\StoreLogo.png` | Иконки приложения (Windows/Store) |
| `Data\Config\loadingscreen.xml` | Текст подсказок на экране загрузки |
| `EasyAntiCheat\SplashScreen.png` | Splash EAC (если запуск с EAC) |

### 6. Полная переработка игровых данных (XML)

| Путь | Что переделывается |
|---|---|
| `Data\Config\items.xml` | Все предметы — новое оружие, инструменты, броня, ресурсы, еда |
| `Data\Config\blocks.xml` | Все блоки — новые ворксейшены, блоки, двери, ловушки |
| `Data\Config\recipes.xml` | Вся система крафта с нуля |
| `Data\Config\loot.xml` | Полная переработка лута |
| `Data\Config\progression.xml` | Своё дерево перков/навыков/атрибутов |
| `Data\Config\buffs.xml` | Новые баффы, механики, триггеры |
| `Data\Config\entityclasses.xml` | Новые зомби, NPC, животные, боссы |
| `Data\Config\entitygroups.xml` | Группы спавна для переработанных сущностей |
| `Data\Config\gamestages.xml` | Новые волны и масштабирование сложности |
| `Data\Config\spawning.xml` | Новые правила спавна по биомам |
| `Data\Config\traders.xml` | Переработка торговцев |
| `Data\Config\vehicles.xml` | Новые/изменённые транспортные средства |
| `Data\Config\item_modifiers.xml` | Новые модификации оружия |
| `Data\Config\quests.xml` | Своя система квестов |
| `Data\Config\challenges.xml` | Свои челленджи |
| `Data\Config\biomes.xml` | Переработка биомов |
| `Data\Config\materials.xml` | Новые материалы блоков |
| `Data\Config\qualityinfo.xml` | Своя система качества |
| `Data\Config\worldglobal.xml` | Глобальные настройки мира (цикл дня, погода) |
| `Data\Config\weathersurvival.xml` | Выживание и погодные эффекты |
| `Data\Config\dialogs.xml` | NPC-диалоги |
| `Data\Config\utilityai.xml` | AI поведение сущностей |
| `Data\Config\Localization.txt` | **ВСЕ** тексты — названия, описания, UI-строки |

### 7. Мир и префабы

| Путь | Зачем изучать |
|---|---|
| `Data\Config\rwgmixer.xml` | Рецепт генерации случайного мира — города, дороги, биомы |
| `Data\Prefabs\POIs\` (~500+ POI) | Все здания мира. Формат: `.xml` (мета), `.tts` (блоки), `.mesh` (навмеш), `.jpg` (превью) |
| `Data\Prefabs\Parts\` | Составные части зданий |
| `Data\Prefabs\RWGTiles\` | Тайлы дорог/перекрёстков для RWG |
| `Data\Stamps\` | Штампы рельефа (горы, холмы, озёра, реки) |
| `Data\Worlds\Navezgane\` | Фиксированная карта — образец структуры мира |

### 8. Инфраструктура Unity (для создания своих ассетов)

| Путь | Зачем изучать |
|---|---|
| `7DaysToDie_Data\ScriptingAssemblies.json` | Какие сборки загружает рантайм — нужно знать при добавлении своих DLL |
| `7DaysToDie_Data\RuntimeInitializeOnLoads.json` | Порядок инициализации — важно для ранних патчей |
| `7DaysToDie_Data\boot.config` | Конфиг Unity-рантайма |
| `MonoBleedingEdge\` | Среда исполнения Mono — понимание ограничений .NET |

---

### Порядок изучения для Total Conversion

| Этап | Фокус | Ключевые файлы |
|---|---|---|
| **1** | Декомпиляция и изучение кода | `Assembly-CSharp.dll` в dnSpy |
| **2** | Изучение XML-системы | Все `Data\Config\*.xml` |
| **3** | Изучение UI-системы | `XUi\`, `XUi_Menu\`, `XUi_Common\` + `NGUI.dll` |
| **4** | Изучение системы ассетов | `catalog.json` + структура `Addressables\Standalone\` |
| **5** | Создание Unity-проекта | Для сборки своих AssetBundle с мешами/текстурами |
| **6** | Изучение Harmony API | `0Harmony.dll` + `0_TFP_Harmony\` как образец |
| **7** | Изучение префабов | POIs формат + инструменты TFP Editor |

Undead Legacy и подобные total conversion моды используют **все** эти слои одновременно: Harmony DLL для изменения поведения кода + XML для данных + Unity AssetBundles для визуала + XUi для интерфейса.
