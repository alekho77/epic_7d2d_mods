# 7 Days to Die — Complete File Inventory

All paths are relative to the game installation root.

## Legend

| Origin | Meaning |
| --- | --- |
| **TFP** | The Fun Pimps (game developer) |
| **Unity** | Unity engine / Unity Technologies |
| **.NET** | Mono / .NET framework |
| **Steam** | Valve / Steamworks |
| **3rd** | Third-party library |
| **EAC** | Easy Anti-Cheat (Epic) |
| **NVIDIA** | NVIDIA Corporation |
| **MS** | Microsoft (Xbox GDK) |

---

## Root Directory

| Path | Origin | Purpose |
| --- | --- | --- |
| `7DaysToDie.exe` | TFP | Main game executable (launches without EAC) |
| `7DaysToDie_EAC.exe` | TFP/EAC | EAC-enabled executable used in the anti-cheat startup path |
| `7dLauncher.exe` | TFP | Steam launcher executable — launches the game, shows launcher UI, can start without EAC |
| `UnityCrashHandler64.exe` | Unity | Handles Unity engine crash dumps |
| `UnityPlayer.dll` | Unity | Unity engine core runtime (native C++) |
| `UnityPlayer_Win64_player_mono_x64.pdb` | Unity | Debug symbols for `UnityPlayer.dll` |
| `UnityCrashHandler64.pdb` | Unity | Debug symbols for crash handler |
| `WindowsPlayer_player_Master_mono_x64.pdb` | Unity/TFP | Debug symbols for master player build |
| `nvngx_dlss.dll` | NVIDIA | DLSS (Deep Learning Super Sampling) native library |
| `NVUnityPlugin.dll` | NVIDIA | NVIDIA Unity integration plugin (native) |
| `steamclient64.dll` | Steam | Steam client runtime library (native) |
| `steam_appid.txt` | Steam | Steam Application ID (`251570`) |
| `tier0_s64.dll` | Steam | Valve low-level runtime library (native) |
| `vstdlib_s64.dll` | Steam | Valve standard library runtime (native) |
| `serverconfig.xml` | TFP | Dedicated server configuration template |
| `platform.cfg` | TFP | Platform-specific settings |
| `startdedicated.bat` | TFP | Launch script for dedicated server |
| `MicrosoftGame.Config` | MS | Microsoft Store / Xbox packaging config |
| `installscript.vdf` | Steam | Steam install/uninstall script |

---

## `7DaysToDie_Data\`

| Path | Origin | Purpose |
| --- | --- | --- |
| `7DaysToDie_Data\app.info` | Unity | Application metadata (company, product name) |
| `7DaysToDie_Data\boot.config` | Unity | Unity boot parameters (scripting backend, GC settings) |
| `7DaysToDie_Data\data.unity3d` | Unity | Packed Unity asset data (scenes, shaders, built-in resources) |
| `7DaysToDie_Data\resources.resource` | Unity | Packed resource assets |
| `7DaysToDie_Data\sharedassets2.resource` | Unity | Shared assets pack |
| `7DaysToDie_Data\RuntimeInitializeOnLoads.json` | Unity | Runtime initialization sequence definitions |
| `7DaysToDie_Data\ScriptingAssemblies.json` | Unity | List of assemblies loaded by the scripting runtime |

### `7DaysToDie_Data\Resources\`

| Path | Origin | Purpose |
| --- | --- | --- |
| `7DaysToDie_Data\Resources\unity default resources` | Unity | Built-in Unity default assets (shaders, materials, fonts) |

### `7DaysToDie_Data\StreamingAssets\`

| Path | Origin | Purpose |
| --- | --- | --- |
| `7DaysToDie_Data\StreamingAssets\aa\catalog.json` | Unity | Addressables catalog — master index mapping asset addresses to bundle paths |
| `7DaysToDie_Data\StreamingAssets\aa\settings.json` | Unity | Addressables system settings |
| `7DaysToDie_Data\StreamingAssets\aa\shaders.json` | Unity | Shader variant tracking data |
| `7DaysToDie_Data\StreamingAssets\aa\AddressablesLink\link.xml` | Unity | Link between Addressables and resources |
| `7DaysToDie_Data\StreamingAssets\Video\TFP_Intro.webm` | TFP | The Fun Pimps splash/intro video |

---

## `7DaysToDie_Data\Managed\` — Managed (.NET) DLLs

### TFP Game Assemblies

| Path | Origin | Purpose |
| --- | --- | --- |
| `7DaysToDie_Data\Managed\Assembly-CSharp.dll` | TFP | **Main game code** — all items, blocks, entities, AI, UI, networking, world gen, buffs, crafting, quests |
| `7DaysToDie_Data\Managed\Assembly-CSharp-firstpass.dll` | TFP | Early-init code loaded before main assembly — utility classes, base types |
| `7DaysToDie_Data\Managed\LogLibrary.dll` | TFP | Custom TFP logging framework |

### Third-Party Libraries

| Path | Origin | Purpose |
| --- | --- | --- |
| `7DaysToDie_Data\Managed\NGUI.dll` | 3rd | NGUI — underlying UI runtime library; game's moddable UI layer is XUi (`Data\Config\XUi\`) built on top of NGUI |
| `7DaysToDie_Data\Managed\NCalc.dll` | 3rd | Math expression evaluator (used in buff/progression formulas) |
| `7DaysToDie_Data\Managed\AstarPathfindingProject.dll` | 3rd | A* Pathfinding Project Pro — NPC/zombie navigation |
| `7DaysToDie_Data\Managed\Pathfinding.ClipperLib.dll` | 3rd | Polygon clipping for pathfinding mesh generation |
| `7DaysToDie_Data\Managed\Pathfinding.Ionic.Zip.Reduced.dll` | 3rd | Zip compression for pathfinding data |
| `7DaysToDie_Data\Managed\Pathfinding.Poly2Tri.dll` | 3rd | 2D polygon triangulation for pathfinding |
| `7DaysToDie_Data\Managed\InControl.dll` | 3rd | Controller/input mapping framework |
| `7DaysToDie_Data\Managed\InControl.Examples.dll` | 3rd | InControl usage examples |
| `7DaysToDie_Data\Managed\LiteNetLib.dll` | 3rd | UDP networking library (multiplayer) |
| `7DaysToDie_Data\Managed\MemoryPack.dll` | 3rd | Binary serialization (save data, network packets) |
| `7DaysToDie_Data\Managed\Newtonsoft.Json.dll` | 3rd | JSON.NET — JSON serialization |
| `7DaysToDie_Data\Managed\Utf8Json.dll` | 3rd | High-performance UTF-8 JSON serializer |
| `7DaysToDie_Data\Managed\Noemax.GZip.dll` | 3rd | GZip compression |
| `7DaysToDie_Data\Managed\Antlr3.Runtime.dll` | 3rd | ANTLR3 parser runtime (used by NCalc) |
| `7DaysToDie_Data\Managed\Backtrace.Unity.dll` | 3rd | Crash reporting SDK |
| `7DaysToDie_Data\Managed\zxing.unity.dll` | 3rd | QR/barcode scanning (Twitch integration) |
| `7DaysToDie_Data\Managed\enum2int.dll` | 3rd | Fast enum-to-int conversion |
| `7DaysToDie_Data\Managed\ScreenSpaceReflections.dll` | 3rd | Screen-space reflections post-process effect |
| `7DaysToDie_Data\Managed\HBAO.Runtime.dll` | 3rd | Horizon-Based Ambient Occlusion effect |
| `7DaysToDie_Data\Managed\HBAO.Demo.Runtime.dll` | 3rd | HBAO demo/sample runtime |
| `7DaysToDie_Data\Managed\AmplifyShaderEditor.Samples.BuiltIn.dll` | 3rd | Amplify Shader Editor sample shaders |

### Platform SDKs

| Path | Origin | Purpose |
| --- | --- | --- |
| `7DaysToDie_Data\Managed\com.rlabrecque.steamworks.net.dll` | 3rd | Steamworks.NET — Steam API wrapper (achievements, lobbies, workshop) |
| `7DaysToDie_Data\Managed\Discord.Sdk.dll` | 3rd | Discord Rich Presence / Game SDK |
| `7DaysToDie_Data\Managed\EOS.dll` | 3rd | Epic Online Services managed wrapper |
| `7DaysToDie_Data\Managed\XblPCSandbox.dll` | MS | Xbox Live PC sandbox |
| `7DaysToDie_Data\Managed\com.thenakeddev.dlss.Runtime.dll` | 3rd | NVIDIA DLSS Unity integration |
| `7DaysToDie_Data\Managed\com.thenakeddev.fsr.Runtime.dll` | 3rd | AMD FSR Unity integration |
| `7DaysToDie_Data\Managed\com.thenakeddev.fsr.Runtime.BIRP.dll` | 3rd | AMD FSR Built-In Render Pipeline support |

### Unity Engine Modules

| Path | Origin | Purpose |
| --- | --- | --- |
| `7DaysToDie_Data\Managed\UnityEngine.dll` | Unity | Unity engine facade/entry point |
| `7DaysToDie_Data\Managed\UnityEngine.CoreModule.dll` | Unity | Core types: `GameObject`, `MonoBehaviour`, `Transform`, `Component` |
| `7DaysToDie_Data\Managed\UnityEngine.PhysicsModule.dll` | Unity | Physics, raycasts, colliders, rigidbodies |
| `7DaysToDie_Data\Managed\UnityEngine.Physics2DModule.dll` | Unity | 2D physics engine |
| `7DaysToDie_Data\Managed\UnityEngine.AnimationModule.dll` | Unity | Animation system (Animator, AnimationClip) |
| `7DaysToDie_Data\Managed\UnityEngine.AudioModule.dll` | Unity | Audio playback (`AudioSource`, `AudioClip`) |
| `7DaysToDie_Data\Managed\UnityEngine.UI.dll` | Unity | Built-in Unity UI (Canvas, Image, Text) |
| `7DaysToDie_Data\Managed\UnityEngine.UIModule.dll` | Unity | Low-level UI module |
| `7DaysToDie_Data\Managed\UnityEngine.UIElementsModule.dll` | Unity | Unity UI Toolkit module included in the build |
| `7DaysToDie_Data\Managed\UnityEngine.IMGUIModule.dll` | Unity | Immediate-mode GUI |
| `7DaysToDie_Data\Managed\UnityEngine.InputLegacyModule.dll` | Unity | Legacy `Input` class |
| `7DaysToDie_Data\Managed\UnityEngine.InputModule.dll` | Unity | Input system module |
| `7DaysToDie_Data\Managed\UnityEngine.TextRenderingModule.dll` | Unity | Text rendering (Font, TextMesh) |
| `7DaysToDie_Data\Managed\UnityEngine.TextCoreTextEngineModule.dll` | Unity | TextMeshPro underlying text engine |
| `7DaysToDie_Data\Managed\UnityEngine.TextCoreFontEngineModule.dll` | Unity | Font rendering engine |
| `7DaysToDie_Data\Managed\UnityEngine.ParticleSystemModule.dll` | Unity | Particle effects |
| `7DaysToDie_Data\Managed\UnityEngine.TerrainModule.dll` | Unity | Terrain system |
| `7DaysToDie_Data\Managed\UnityEngine.TerrainPhysicsModule.dll` | Unity | Terrain colliders |
| `7DaysToDie_Data\Managed\UnityEngine.AssetBundleModule.dll` | Unity | AssetBundle loading API |
| `7DaysToDie_Data\Managed\UnityEngine.JSONSerializeModule.dll` | Unity | JSON utility |
| `7DaysToDie_Data\Managed\UnityEngine.ImageConversionModule.dll` | Unity | Texture encoding/decoding (PNG, JPG) |
| `7DaysToDie_Data\Managed\UnityEngine.VideoModule.dll` | Unity | Video playback |
| `7DaysToDie_Data\Managed\UnityEngine.VFXModule.dll` | Unity | Visual Effects Graph |
| `7DaysToDie_Data\Managed\UnityEngine.VehiclesModule.dll` | Unity | Wheel colliders, vehicle physics |
| `7DaysToDie_Data\Managed\UnityEngine.WindModule.dll` | Unity | Wind zones for vegetation animation |
| `7DaysToDie_Data\Managed\UnityEngine.AIModule.dll` | Unity | NavMesh and AI navigation |
| `7DaysToDie_Data\Managed\UnityEngine.AccessibilityModule.dll` | Unity | Accessibility features |
| `7DaysToDie_Data\Managed\UnityEngine.AndroidJNIModule.dll` | Unity | Android JNI bridge — platform-specific module included in the build |
| `7DaysToDie_Data\Managed\UnityEngine.ARModule.dll` | Unity | Augmented Reality — platform-specific module included in the build |
| `7DaysToDie_Data\Managed\UnityEngine.ClothModule.dll` | Unity | Cloth simulation |
| `7DaysToDie_Data\Managed\UnityEngine.ClusterInputModule.dll` | Unity | Cluster rendering input |
| `7DaysToDie_Data\Managed\UnityEngine.ClusterRendererModule.dll` | Unity | Cluster rendering |
| `7DaysToDie_Data\Managed\UnityEngine.ContentLoadModule.dll` | Unity | Content loading subsystem |
| `7DaysToDie_Data\Managed\UnityEngine.CrashReportingModule.dll` | Unity | Crash reporting |
| `7DaysToDie_Data\Managed\UnityEngine.DirectorModule.dll` | Unity | Timeline director |
| `7DaysToDie_Data\Managed\UnityEngine.DSPGraphModule.dll` | Unity | DSP audio graph |
| `7DaysToDie_Data\Managed\UnityEngine.GameCenterModule.dll` | Unity | Apple GameCenter — platform-specific module included in the build |
| `7DaysToDie_Data\Managed\UnityEngine.GIModule.dll` | Unity | Global Illumination |
| `7DaysToDie_Data\Managed\UnityEngine.GridModule.dll` | Unity | Grid/Tilemap grid |
| `7DaysToDie_Data\Managed\UnityEngine.HotReloadModule.dll` | Unity | Hot reload support |
| `7DaysToDie_Data\Managed\UnityEngine.LocalizationModule.dll` | Unity | Localization subsystem |
| `7DaysToDie_Data\Managed\UnityEngine.NVIDIAModule.dll` | Unity | NVIDIA integration module |
| `7DaysToDie_Data\Managed\UnityEngine.PerformanceReportingModule.dll` | Unity | Performance metrics reporting |
| `7DaysToDie_Data\Managed\UnityEngine.ProfilerModule.dll` | Unity | Profiler API |
| `7DaysToDie_Data\Managed\UnityEngine.PropertiesModule.dll` | Unity | Properties module |
| `7DaysToDie_Data\Managed\UnityEngine.RuntimeInitializeOnLoadManagerInitializerModule.dll` | Unity | Runtime init-on-load manager |
| `7DaysToDie_Data\Managed\UnityEngine.ScreenCaptureModule.dll` | Unity | Screenshot capture |
| `7DaysToDie_Data\Managed\UnityEngine.SharedInternalsModule.dll` | Unity | Shared engine internals |
| `7DaysToDie_Data\Managed\UnityEngine.SpriteMaskModule.dll` | Unity | Sprite masking |
| `7DaysToDie_Data\Managed\UnityEngine.SpriteShapeModule.dll` | Unity | Sprite shapes |
| `7DaysToDie_Data\Managed\UnityEngine.StreamingModule.dll` | Unity | Asset streaming |
| `7DaysToDie_Data\Managed\UnityEngine.SubstanceModule.dll` | Unity | Substance materials |
| `7DaysToDie_Data\Managed\UnityEngine.SubsystemsModule.dll` | Unity | Subsystem management |
| `7DaysToDie_Data\Managed\UnityEngine.TilemapModule.dll` | Unity | 2D Tilemap |
| `7DaysToDie_Data\Managed\UnityEngine.TLSModule.dll` | Unity | TLS/SSL support |
| `7DaysToDie_Data\Managed\UnityEngine.UmbraModule.dll` | Unity | Umbra occlusion culling |
| `7DaysToDie_Data\Managed\UnityEngine.UnityAnalyticsCommonModule.dll` | Unity | Analytics common types |
| `7DaysToDie_Data\Managed\UnityEngine.UnityAnalyticsModule.dll` | Unity | Unity Analytics |
| `7DaysToDie_Data\Managed\UnityEngine.UnityConnectModule.dll` | Unity | Unity Connect services |
| `7DaysToDie_Data\Managed\UnityEngine.UnityCurlModule.dll` | Unity | libcurl wrapper |
| `7DaysToDie_Data\Managed\UnityEngine.UnityTestProtocolModule.dll` | Unity | Test protocol |
| `7DaysToDie_Data\Managed\UnityEngine.UnityWebRequestModule.dll` | Unity | HTTP web requests |
| `7DaysToDie_Data\Managed\UnityEngine.UnityWebRequestAssetBundleModule.dll` | Unity | Web request for asset bundles |
| `7DaysToDie_Data\Managed\UnityEngine.UnityWebRequestAudioModule.dll` | Unity | Web request for audio clips |
| `7DaysToDie_Data\Managed\UnityEngine.UnityWebRequestTextureModule.dll` | Unity | Web request for textures |
| `7DaysToDie_Data\Managed\UnityEngine.UnityWebRequestWWWModule.dll` | Unity | Legacy WWW web request |
| `7DaysToDie_Data\Managed\UnityEngine.VRModule.dll` | Unity | Virtual Reality |
| `7DaysToDie_Data\Managed\UnityEngine.XRModule.dll` | Unity | Extended Reality (XR) |

### Unity Packages

| Path | Origin | Purpose |
| --- | --- | --- |
| `7DaysToDie_Data\Managed\Unity.Addressables.dll` | Unity | Addressable Asset System (asset loading/management) |
| `7DaysToDie_Data\Managed\Unity.ResourceManager.dll` | Unity | Resource management for Addressables |
| `7DaysToDie_Data\Managed\Unity.TextMeshPro.dll` | Unity | TextMeshPro text rendering |
| `7DaysToDie_Data\Managed\Unity.Burst.dll` | Unity | Burst compiler runtime |
| `7DaysToDie_Data\Managed\Unity.Burst.Unsafe.dll` | Unity | Burst unsafe utilities |
| `7DaysToDie_Data\Managed\Unity.Collections.dll` | Unity | Native collections (`NativeArray`, etc.) |
| `7DaysToDie_Data\Managed\Unity.Collections.LowLevel.ILSupport.dll` | Unity | Low-level IL support for collections |
| `7DaysToDie_Data\Managed\Unity.Mathematics.dll` | Unity | High-performance math library |
| `7DaysToDie_Data\Managed\Unity.Animation.Rigging.dll` | Unity | Animation rigging constraints |
| `7DaysToDie_Data\Managed\Unity.Animation.Rigging.DocCodeExamples.dll` | Unity | Animation rigging code examples |
| `7DaysToDie_Data\Managed\Unity.Postprocessing.Runtime.dll` | Unity | Post-processing stack (bloom, AO, color grading) |
| `7DaysToDie_Data\Managed\Unity.TerrainTools.dll` | Unity | Terrain tools runtime |
| `7DaysToDie_Data\Managed\Unity.Profiling.Core.dll` | Unity | Profiling API |
| `7DaysToDie_Data\Managed\Unity.MemoryProfiler.dll` | Unity | Memory profiler |
| `7DaysToDie_Data\Managed\Unity.ScriptableBuildPipeline.dll` | Unity | Scriptable build pipeline |
| `7DaysToDie_Data\Managed\Unity.Microsoft.GDK.dll` | MS | Xbox/MS Store GDK integration |
| `7DaysToDie_Data\Managed\Unity.Microsoft.GDK.Tools.dll` | MS | GDK tools |

### .NET / Mono Framework

| Path | Origin | Purpose |
| --- | --- | --- |
| `7DaysToDie_Data\Managed\mscorlib.dll` | .NET | Core .NET runtime (object, string, collections, threading) |
| `7DaysToDie_Data\Managed\System.dll` | .NET | Core System classes (IO, Net, Config, Diagnostics) |
| `7DaysToDie_Data\Managed\System.Core.dll` | .NET | LINQ, Expressions, dynamic types |
| `7DaysToDie_Data\Managed\System.Xml.dll` | .NET | XML DOM and XPath processing |
| `7DaysToDie_Data\Managed\System.Xml.Linq.dll` | .NET | LINQ to XML |
| `7DaysToDie_Data\Managed\System.Net.Http.dll` | .NET | HTTP client |
| `7DaysToDie_Data\Managed\System.Data.dll` | .NET | ADO.NET data access |
| `7DaysToDie_Data\Managed\System.Data.DataSetExtensions.dll` | .NET | DataSet LINQ extensions |
| `7DaysToDie_Data\Managed\System.Drawing.dll` | .NET | GDI+ graphics (System.Drawing) |
| `7DaysToDie_Data\Managed\System.IO.Compression.dll` | .NET | Compression streams (deflate, gzip) |
| `7DaysToDie_Data\Managed\System.IO.Compression.FileSystem.dll` | .NET | Zip file I/O |
| `7DaysToDie_Data\Managed\System.Numerics.dll` | .NET | Numeric types (BigInteger, Complex) |
| `7DaysToDie_Data\Managed\System.Runtime.dll` | .NET | Runtime support types |
| `7DaysToDie_Data\Managed\System.Runtime.CompilerServices.Unsafe.dll` | .NET | Unsafe memory operations |
| `7DaysToDie_Data\Managed\System.Runtime.Serialization.dll` | .NET | Data contract serialization |
| `7DaysToDie_Data\Managed\System.Security.dll` | .NET | Security and cryptography extensions |
| `7DaysToDie_Data\Managed\System.ServiceModel.Internals.dll` | .NET | WCF internals |
| `7DaysToDie_Data\Managed\System.ServiceProcess.dll` | .NET | Windows service support |
| `7DaysToDie_Data\Managed\System.Transactions.dll` | .NET | Transaction management |
| `7DaysToDie_Data\Managed\System.Windows.Forms.dll` | .NET | Windows Forms (minimal, used for clipboard/dialogs) |
| `7DaysToDie_Data\Managed\System.ComponentModel.Composition.dll` | .NET | MEF (Managed Extensibility Framework) |
| `7DaysToDie_Data\Managed\System.Configuration.dll` | .NET | App configuration system |
| `7DaysToDie_Data\Managed\System.Configuration.Install.dll` | .NET | Install/uninstall components |
| `7DaysToDie_Data\Managed\System.EnterpriseServices.dll` | .NET | COM+ enterprise services |
| `7DaysToDie_Data\Managed\Mono.Posix.dll` | .NET | POSIX API wrapper for Mono |
| `7DaysToDie_Data\Managed\Mono.Security.dll` | .NET | Mono security/crypto |
| `7DaysToDie_Data\Managed\Mono.WebBrowser.dll` | .NET | Mono embedded web browser |
| `7DaysToDie_Data\Managed\netstandard.dll` | .NET | .NET Standard 2.0 compatibility shim |
| `7DaysToDie_Data\Managed\Accessibility.dll` | .NET | Accessibility support types |
| `7DaysToDie_Data\Managed\Unity.InputSystem.dll` | Unity | New Input System package |

---

## `7DaysToDie_Data\Plugins\x86_64\` — Native Plugins

| Path | Origin | Purpose |
| --- | --- | --- |
| `7DaysToDie_Data\Plugins\x86_64\steam_api64.dll` | Steam | Steamworks native API |
| `7DaysToDie_Data\Plugins\x86_64\EOSSDK-Win64-Shipping.dll` | 3rd (Epic) | Epic Online Services native SDK |
| `7DaysToDie_Data\Plugins\x86_64\discord_partner_sdk.dll` | 3rd | Discord SDK native library |
| `7DaysToDie_Data\Plugins\x86_64\InControlNative.dll` | 3rd | InControl native input handler |
| `7DaysToDie_Data\Plugins\x86_64\lib_burst_generated.dll` | Unity | Burst-compiled native code |
| `7DaysToDie_Data\Plugins\x86_64\BacktraceCrashpadWindows.dll` | 3rd | Backtrace crash capture |
| `7DaysToDie_Data\Plugins\x86_64\backtrace_native_xbox.dll` | 3rd | Xbox-specific Backtrace |
| `7DaysToDie_Data\Plugins\x86_64\crashpad_handler.dll` | 3rd | Crashpad crash handler |
| `7DaysToDie_Data\Plugins\x86_64\ControllerExt.dll` | 3rd | Extended controller support |
| `7DaysToDie_Data\Plugins\x86_64\getrss.dll` | 3rd | Memory usage (RSS) monitoring |
| `7DaysToDie_Data\Plugins\x86_64\Magick.dll` | 3rd | ImageMagick — image processing |
| `7DaysToDie_Data\Plugins\x86_64\xaudio2_9redist.dll` | MS | XAudio2 redistributable (audio backend) |
| `7DaysToDie_Data\Plugins\x86_64\XCurl.dll` | MS | Xbox HTTP/CURL library |
| `7DaysToDie_Data\Plugins\x86_64\XGameRuntime.Thunks.dll` | MS | Xbox Game Runtime thunks |
| `7DaysToDie_Data\Plugins\x86_64\XInputInterface64.dll` | MS | XInput (gamepad input) |
| `7DaysToDie_Data\Plugins\x86_64\Microsoft.Xbox.Services.GDK.C.Thunks.dll` | MS | Xbox services GDK thunks |

---

## `Data\` — Game Content Root

| Path | Origin | Purpose |
| --- | --- | --- |
| `Data\7dtd_icon.ico` | TFP | Game icon file |

### `Data\Config\` — XML Configuration Files

| Path | Origin | Purpose |
| --- | --- | --- |
| `Data\Config\items.xml` | TFP | All holdable items: weapons, tools, consumables, resources, ammo and their properties |
| `Data\Config\blocks.xml` | TFP | All placeable blocks: terrain, structures, doors, traps, workstations, storage |
| `Data\Config\recipes.xml` | TFP | Crafting recipes: ingredients, output amounts, required workstations |
| `Data\Config\loot.xml` | TFP | Loot containers, loot groups, probability tables, quest loot |
| `Data\Config\entityclasses.xml` | TFP | Zombie, animal, NPC, bandit class definitions — stats, AI, meshes, sounds |
| `Data\Config\entitygroups.xml` | TFP | Named groups of entities used by gamestage spawning |
| `Data\Config\buffs.xml` | TFP | Buffs, debuffs, status effects — triggers, durations, stacking, passive effects |
| `Data\Config\progression.xml` | TFP | Skills, perks, attributes, level scaling, skill point costs |
| `Data\Config\gamestages.xml` | TFP | Horde night wave definitions, spawn scaling by gamestage |
| `Data\Config\spawning.xml` | TFP | Biome and zone spawning rules — which entities spawn where |
| `Data\Config\traders.xml` | TFP | Trader inventories, tiers, restock settings, quest offerings |
| `Data\Config\vehicles.xml` | TFP | Vehicle definitions, properties, fuel, storage, speed |
| `Data\Config\item_modifiers.xml` | TFP | Weapon/tool mod attachments, dyes, cosmetic slots |
| `Data\Config\quests.xml` | TFP | Quest definitions, objectives, reward tables, quest chains |
| `Data\Config\biomes.xml` | TFP | Biome definitions: surface blocks, sub-biomes, decoration spawns |
| `Data\Config\sounds.xml` | TFP | Sound event mappings: every game action → audio file(s) |
| `Data\Config\materials.xml` | TFP | Block material properties: hardness, damage resistance, particle effects |
| `Data\Config\shapes.xml` | TFP | Block shape definitions (3D mesh shape references) |
| `Data\Config\qualityinfo.xml` | TFP | Item quality tiers and stat scaling per tier |
| `Data\Config\worldglobal.xml` | TFP | Global world settings: day length, day/night cycle, loot respawn, blood moon |
| `Data\Config\weathersurvival.xml` | TFP | Weather effects on player survival stats (temperature, wetness) |
| `Data\Config\painting.xml` | TFP | Block painting textures catalogue |
| `Data\Config\nav_objects.xml` | TFP | Minimap/compass navigation icons |
| `Data\Config\archetypes.xml` | TFP | Entity archetypes — base templates for entityclasses |
| `Data\Config\dialogs.xml` | TFP | NPC dialog trees (trader conversations, quest dialogs) |
| `Data\Config\npc.xml` | TFP | NPC-specific settings |
| `Data\Config\challenges.xml` | TFP | In-game challenges and objectives |
| `Data\Config\events.xml` | TFP | Game event trigger definitions |
| `Data\Config\gameevents.xml` | TFP | Game event response/action definitions |
| `Data\Config\rwgmixer.xml` | TFP | Random World Generation recipe — cities, roads, biome placement |
| `Data\Config\utilityai.xml` | TFP | AI utility scoring and behaviour trees for entities |
| `Data\Config\misc.xml` | TFP | Miscellaneous global game variables |
| `Data\Config\physicsbodies.xml` | TFP | Ragdoll/physics body definitions |
| `Data\Config\ui_display.xml` | TFP | Stat/property display labels for the UI |
| `Data\Config\music.xml` | TFP | Background music event mappings: biome/situation → tracks |
| `Data\Config\subtitles.xml` | TFP | Subtitle entries for audio events |
| `Data\Config\dmscontent.xml` | TFP | Dynamic Music System (DMS) configuration and content definitions |
| `Data\Config\twitch.xml` | TFP | Twitch integration configuration |
| `Data\Config\twitch_events.xml` | TFP | Twitch integration event definitions |
| `Data\Config\videos.xml` | TFP | Intro/cutscene video references |
| `Data\Config\loadingscreen.xml` | TFP | Loading screen tip text entries |
| `Data\Config\blockplaceholders.xml` | TFP | Block placeholder substitution rules during world load |
| `Data\Config\Localization.txt` | TFP | All in-game strings — TSV format, key → language columns (english, german, spanish, french, italian, japanese, koreana, polish, brazilian, russian, turkish, schinese, tchinese) |
| `Data\Config\BlockUpdates.csv` | TFP | Block upgrade/downgrade transition table |
| `Data\Config\OversizedConversionTargets.txt` | TFP | Oversized block conversion list |
| `Data\Config\Stealth.txt` | TFP | Stealth system parameters |
| `Data\Config\XML.txt` | TFP | Developer notes on the XML patching system, Extends, block naming conventions |

### `Data\Config\XUi\` — In-Game HUD UI

| Path | Origin | Purpose |
| --- | --- | --- |
| `Data\Config\XUi\windows.xml` | TFP | All in-game HUD windows: inventory, crafting, loot, map, compass, health bars, hotbar, container UI, vehicle UI, trader UI |
| `Data\Config\XUi\controls.xml` | TFP | Reusable UI components: buttons, item slots, icons, lists, grids, scrollbars |
| `Data\Config\XUi\styles.xml` | TFP | UI styles: colors, font sizes, padding, alignment, anchoring |
| `Data\Config\XUi\xui.xml` | TFP | Root XUi file — binds windows, controls, styles together, defines window loading |

### `Data\Config\XUi_Menu\` — Main Menu UI

| Path | Origin | Purpose |
| --- | --- | --- |
| `Data\Config\XUi_Menu\windows.xml` | TFP | Main menu windows: start screen, settings, world selection, multiplayer browser |
| `Data\Config\XUi_Menu\controls.xml` | TFP | Menu-specific UI components |
| `Data\Config\XUi_Menu\styles.xml` | TFP | Menu UI styles |
| `Data\Config\XUi_Menu\xui.xml` | TFP | Menu root XUi file |

### `Data\Config\XUi_Common\` — Shared UI Components

| Path | Origin | Purpose |
| --- | --- | --- |
| `Data\Config\XUi_Common\controls.xml` | TFP | Shared controls used by both HUD and Menu |
| `Data\Config\XUi_Common\styles.xml` | TFP | Shared styles used by both HUD and Menu |

### `Data\ItemIcons\` — Item/Block Icons (~5091 PNG files)

| Path | Origin | Purpose |
| --- | --- | --- |
| `Data\ItemIcons\*.png` | TFP | PNG icon sprites for every item and block. Filename matches `name` attribute from `items.xml` / `blocks.xml` (e.g., `gunPistol.png`, `drinkJarBoiledWater.png`). Typically 116×116 or 232×232 px with transparency. |

### `Data\Music\` — Music Tracks (~496 WAV files)

| Path | Origin | Purpose |
| --- | --- | --- |
| `Data\Music\*.wav` | TFP | WAV music tracks. Naming convention: `NNN_<type>_NN.wav`. Types: `combat`, `explore`, `suspense`, `building`, `ambient`, `bloodmoon`. Used by the dynamic music system; see `dmscontent.xml` and possibly `music.xml`. |

### `Data\Bluffs\`

| Path | Origin | Purpose |
| --- | --- | --- |
| `Data\Bluffs\bluff1.tga` | TFP | Terrain bluff texture #1 |
| `Data\Bluffs\bluff2.tga` | TFP | Terrain bluff texture #2 |

### `Data\Stamps\` — Terrain Generation Stamps (~28 files)

| Path | Origin | Purpose |
| --- | --- | --- |
| `Data\Stamps\base_01.raw` | TFP | Base terrain elevation stamp |
| `Data\Stamps\canyon_01.raw` | TFP | Canyon terrain stamp |
| `Data\Stamps\crater_01.raw` | TFP | Crater terrain stamp |
| `Data\Stamps\desert_land_border_01.raw` | TFP | Desert land border stamp #1 |
| `Data\Stamps\desert_land_border_02.raw` | TFP | Desert land border stamp #2 |
| `Data\Stamps\desert_mountains_01.raw` | TFP | Desert mountains stamp #1 |
| `Data\Stamps\desert_mountains_02.raw` | TFP | Desert mountains stamp #2 |
| `Data\Stamps\filler_biome_01.png` | TFP | Filler biome shape |
| `Data\Stamps\ground_01.raw` | TFP | Ground elevation stamp |
| `Data\Stamps\hills_01.raw` | TFP | Hills terrain stamp #1 |
| `Data\Stamps\hills_02.raw` | TFP | Hills terrain stamp #2 |
| `Data\Stamps\lake_01.raw` | TFP | Lake terrain stamp #1 |
| `Data\Stamps\lake_02.raw` | TFP | Lake terrain stamp #2 |
| `Data\Stamps\land_border_01.raw` | TFP | Land border stamp |
| `Data\Stamps\mountains_01.raw` | TFP | Mountains stamp #1 |
| `Data\Stamps\mountains_02.raw` | TFP | Mountains stamp #2 |
| `Data\Stamps\plains_01.raw` | TFP | Plains stamp #1 |
| `Data\Stamps\plains_02.raw` | TFP | Plains stamp #2 |
| `Data\Stamps\river_01.png` | TFP | River shape stamp #1 |
| `Data\Stamps\river_02.png` | TFP | River shape stamp #2 |
| `Data\Stamps\rwg_tile_cap.png` | TFP | RWG road tile: dead end cap |
| `Data\Stamps\rwg_tile_corner.png` | TFP | RWG road tile: corner |
| `Data\Stamps\rwg_tile_intersection.png` | TFP | RWG road tile: intersection |
| `Data\Stamps\rwg_tile_straight.png` | TFP | RWG road tile: straight |
| `Data\Stamps\rwg_tile_t.png` | TFP | RWG road tile: T-junction |
| `Data\Stamps\water_border_01.raw` | TFP | Water border stamp |

### `Data\UMATextures\`

| Path | Origin | Purpose |
| --- | --- | --- |
| `Data\UMATextures\` | TFP | Directory present; empty in this build snapshot |

### `Data\Prefabs\` — World Prefab Structures

| Path | Origin | Purpose |
| --- | --- | --- |
| `Data\Prefabs\POIs\` (~1041 POIs, 6227 files) | TFP | Points of Interest: houses, stores, factories, farms, caves, hospitals, trader bases, etc. POIs typically include files such as `.xml` (metadata, dimensions, biome tags, tier), `.tts` (block data), `.nim` (block NIM), `.mesh` (AI nav mesh), `.jpg` (preview), `.ins` (instance data) |
| `Data\Prefabs\Parts\` (3143 files) | TFP | Reusable prefab components/building parts |
| `Data\Prefabs\RWGTiles\` (348 files) | TFP | Random World Generation road/city tile templates |
| `Data\Prefabs\Test\` (580 files) | TFP | Development/test prefabs |

### `Data\Bundles\Standalone\Entities\` — Legacy AssetBundles

| Path | Origin | Purpose |
| --- | --- | --- |
| `Data\Bundles\Standalone\Entities\Entities` | TFP | Unity AssetBundle containing entity models (zombies, animals, NPCs) |
| `Data\Bundles\Standalone\Entities\Entities.manifest` | TFP | Manifest for Entities bundle |
| `Data\Bundles\Standalone\Entities\trees` | TFP | Unity AssetBundle containing tree/vegetation models |
| `Data\Bundles\Standalone\Entities\trees.manifest` | TFP | Manifest for trees bundle |

### `Data\Addressables\Standalone\` — Addressable Asset Bundles

#### Global Bundles

| Path | Origin | Purpose |
| --- | --- | --- |
| `…\7c401d1245288cd4ca6169241e1a104c_unitybuiltinshaders.bundle` | Unity | Built-in shader variants |
| `…\blocktextureatlases_assets_all.bundle` | TFP | Texture atlas for all block surfaces |
| `…\terraintextures_assets_all.bundle` | TFP | Terrain surface textures (dirt, stone, snow, sand, grass) |
| `…\shapes_assets_all.bundle` | TFP | Block shape geometry (3D mesh data for all block shapes) |
| `…\effects_assets_all.bundle` | TFP | All VFX: explosions, fire, blood, smoke, muzzle flash |
| `…\shaders_assets_all.bundle` | TFP | Custom shaders |
| `…\prefabs_assets_all.bundle` | TFP | Prefab structure asset data |
| `…\meshdescriptions_assets_all.bundle` | TFP | Mesh descriptions (LOD levels, collider shapes) |
| `…\soundmixers_assets_all.bundle` | TFP | Audio mixer configurations (volume balancing) |

#### Animation Bundles (`animations_assets_animations\`)

| Path | Origin | Purpose |
| --- | --- | --- |
| `…\animations_assets_animations\zombie.bundle` | TFP | Zombie animation clips |

#### Entity Bundles (`automatic_assets_entities\`)

| Path | Origin | Purpose |
| --- | --- | --- |
| `…\automatic_assets_entities\animals.bundle` | TFP | Animal models and materials |
| `…\automatic_assets_entities\appliances.bundle` | TFP | Appliance entity models |
| `…\automatic_assets_entities\banditprops.bundle` | TFP | Bandit prop models |
| `…\automatic_assets_entities\bandits.bundle` | TFP | Bandit NPC models and materials |
| `…\automatic_assets_entities\buildings.bundle` | TFP | Building entity models |
| `…\automatic_assets_entities\commercial.bundle` | TFP | Commercial store entity models |
| `…\automatic_assets_entities\crafting.bundle` | TFP | Crafting station entity models |
| `…\automatic_assets_entities\debris.bundle` | TFP | Debris/rubble entity models |
| `…\automatic_assets_entities\decor.bundle` | TFP | Decorative entity models |
| `…\automatic_assets_entities\doors.bundle` | TFP | Door entity models |
| `…\automatic_assets_entities\effects.bundle` | TFP | Effect entity models |
| `…\automatic_assets_entities\electrical.bundle` | TFP | Electrical component entity models |
| `…\automatic_assets_entities\elevators.bundle` | TFP | Elevator entity models |
| `…\automatic_assets_entities\furniture.bundle` | TFP | Furniture entity models |
| `…\automatic_assets_entities\gore.bundle` | TFP | Gore/body part entity models |
| `…\automatic_assets_entities\industrial.bundle` | TFP | Industrial object entity models |
| `…\automatic_assets_entities\lighting.bundle` | TFP | Light fixture entity models |
| `…\automatic_assets_entities\lootcontainers.bundle` | TFP | Loot container entity models |
| `…\automatic_assets_entities\minerals.bundle` | TFP | Mineral/ore entity models |
| `…\automatic_assets_entities\misc.bundle` | TFP | Miscellaneous entity models |
| `…\automatic_assets_entities\outdoordecor.bundle` | TFP | Outdoor decoration models |
| `…\automatic_assets_entities\plants.bundle` | TFP | Plant entity models |
| `…\automatic_assets_entities\plumbing.bundle` | TFP | Plumbing fixture models |
| `…\automatic_assets_entities\quests.bundle` | TFP | Quest-related entity models |
| `…\automatic_assets_entities\respawnpoints.bundle` | TFP | Respawn point entity models |
| `…\automatic_assets_entities\sandbags.bundle` | TFP | Sandbag entity models |
| `…\automatic_assets_entities\signs.bundle` | TFP | Sign entity models |
| `…\automatic_assets_entities\streetsigns.bundle` | TFP | Street sign entity models |
| `…\automatic_assets_entities\supplycrate.bundle` | TFP | Supply crate entity models |
| `…\automatic_assets_entities\supplyplane.bundle` | TFP | Supply plane entity models |
| `…\automatic_assets_entities\traders.bundle` | TFP | Trader entity models |
| `…\automatic_assets_entities\traps.bundle` | TFP | Trap entity models |
| `…\automatic_assets_entities\vehicles.bundle` | TFP | Vehicle entity models |
| `…\automatic_assets_entities\player\common.bundle` | TFP | Player common entity assets |

#### Sound Bundles (`automatic_assets_sounds\`)

| Path | Origin | Purpose |
| --- | --- | --- |
| `…\automatic_assets_sounds\ambient_loops.bundle` | TFP | Ambient loop sound effects |
| `…\automatic_assets_sounds\ambient_oneshots.bundle` | TFP | Ambient one-shot sound effects |
| `…\automatic_assets_sounds\animals.bundle` | TFP | Animal sound effects |
| `…\automatic_assets_sounds\biomes.bundle` | TFP | Biome ambient sounds |
| `…\automatic_assets_sounds\buffs.bundle` | TFP | Buff/debuff sound effects |
| `…\automatic_assets_sounds\campfire.bundle` | TFP | Campfire sounds |
| `…\automatic_assets_sounds\chem_station.bundle` | TFP | Chemistry station sounds |
| `…\automatic_assets_sounds\collector.bundle` | TFP | Collector sounds |
| `…\automatic_assets_sounds\crafting.bundle` | TFP | General crafting sounds |
| `…\automatic_assets_sounds\destroyblock.bundle` | TFP | Block destruction sounds |
| `…\automatic_assets_sounds\doors.bundle` | TFP | Door open/close sounds |
| `…\automatic_assets_sounds\drone.bundle` | TFP | Drone sounds |
| `…\automatic_assets_sounds\electricity.bundle` | TFP | Electrical sounds |
| `…\automatic_assets_sounds\enemies.bundle` | TFP | Enemy vocalization sounds |
| `…\automatic_assets_sounds\explosions.bundle` | TFP | Explosion sounds |
| `…\automatic_assets_sounds\foliage.bundle` | TFP | Foliage rustle sounds |
| `…\automatic_assets_sounds\forge.bundle` | TFP | Forge sounds |
| `…\automatic_assets_sounds\hazards.bundle` | TFP | Environmental hazard sounds |
| `…\automatic_assets_sounds\impactsurface.bundle` | TFP | Impact on surface sounds (by material) |
| `…\automatic_assets_sounds\items.bundle` | TFP | Item pickup/use sounds |
| `…\automatic_assets_sounds\loot.bundle` | TFP | Loot container open/close sounds |
| `…\automatic_assets_sounds\misc.bundle` | TFP | Miscellaneous sounds |
| `…\automatic_assets_sounds\music.bundle` | TFP | Music tracks (Addressable version) |
| `…\automatic_assets_sounds\pickups.bundle` | TFP | Item pickup sounds |
| `…\automatic_assets_sounds\player_common.bundle` | TFP | Common player sounds (breathing, jumping, landing) |
| `…\automatic_assets_sounds\player_female.bundle` | TFP | Female player voice sounds |
| `…\automatic_assets_sounds\player_male.bundle` | TFP | Male player voice sounds |
| `…\automatic_assets_sounds\prefabs.bundle` | TFP | Prefab ambient sounds |
| `…\automatic_assets_sounds\quests.bundle` | TFP | Quest system sounds |
| `…\automatic_assets_sounds\step.bundle` | TFP | Footstep sounds (by surface material) |
| `…\automatic_assets_sounds\supplydrops.bundle` | TFP | Supply drop sounds |
| `…\automatic_assets_sounds\switches.bundle` | TFP | Switch/lever sounds |
| `…\automatic_assets_sounds\throwimpact.bundle` | TFP | Thrown item impact sounds |
| `…\automatic_assets_sounds\tools.bundle` | TFP | Tool use sounds |
| `…\automatic_assets_sounds\traps.bundle` | TFP | Trap trigger/activation sounds |
| `…\automatic_assets_sounds\triggeredevents.bundle` | TFP | Triggered event sounds |
| `…\automatic_assets_sounds\twitch.bundle` | TFP | Twitch integration sounds |
| `…\automatic_assets_sounds\ui.bundle` | TFP | UI interaction sounds (clicks, hover, confirm) |
| `…\automatic_assets_sounds\useactions.bundle` | TFP | Item use action sounds |
| `…\automatic_assets_sounds\vehicles.bundle` | TFP | Vehicle engine/horn sounds |
| `…\automatic_assets_sounds\vo.bundle` | TFP | Voice-over sounds |
| `…\automatic_assets_sounds\weapons.bundle` | TFP | Weapon firing/reload sounds |

#### Generic/Other Bundles

| Path | Origin | Purpose |
| --- | --- | --- |
| `…\automatic_assets_generic\itemicons.bundle` | TFP | Item icon atlas (Addressable) |
| `…\automatic_assets_other\items.bundle` | TFP | Item models and materials |

#### DLC Cosmetic Bundles (`automatic_assets_dlc\`)

| Path | Origin | Purpose |
| --- | --- | --- |
| `…\automatic_assets_dlc\butchercosmetic.bundle` | TFP | Butcher cosmetic DLC |
| `…\automatic_assets_dlc\christmascosmetics.bundle` | TFP | Christmas cosmetics DLC |
| `…\automatic_assets_dlc\classicsurvivorcosmetic.bundle` | TFP | Classic Survivor cosmetic DLC |
| `…\automatic_assets_dlc\crimsonwarlordcosmetic.bundle` | TFP | Crimson Warlord cosmetic DLC |
| `…\automatic_assets_dlc\desertcosmetic.bundle` | TFP | Desert cosmetic DLC |
| `…\automatic_assets_dlc\femalepimpcosmetic.bundle` | TFP | Female Pimp cosmetic DLC |
| `…\automatic_assets_dlc\hellreavercosmetic.bundle` | TFP | Hell Reaver cosmetic DLC |
| `…\automatic_assets_dlc\hoardercosmetic.bundle` | TFP | Hoarder cosmetic DLC |
| `…\automatic_assets_dlc\maraudercosmetic.bundle` | TFP | Marauder cosmetic DLC |
| `…\automatic_assets_dlc\monstermaskcosmetics.bundle` | TFP | Monster Mask cosmetics DLC |
| `…\automatic_assets_dlc\piratecosmetic.bundle` | TFP | Pirate cosmetic DLC |
| `…\automatic_assets_dlc\samuraicosmetic.bundle` | TFP | Samurai cosmetic DLC |
| `…\automatic_assets_dlc\storymaskcosmetics.bundle` | TFP | Story Mask cosmetics DLC |

#### Twitch Drops Bundles (`automatic_assets_twitchdrops\`)

| Path | Origin | Purpose |
| --- | --- | --- |
| `…\automatic_assets_twitchdrops\crackabookstoregearhat.bundle` | TFP | Crack-a-Book store gear hat |
| `…\automatic_assets_twitchdrops\crackabookstoregearoutfit.bundle` | TFP | Crack-a-Book store gear outfit |
| `…\automatic_assets_twitchdrops\generalstoregearhat.bundle` | TFP | General Store gear hat |
| `…\automatic_assets_twitchdrops\generalstoregearoutfit.bundle` | TFP | General Store gear outfit |
| `…\automatic_assets_twitchdrops\mopowerstoregearhat.bundle` | TFP | Mo' Power store gear hat |
| `…\automatic_assets_twitchdrops\mopowerstoregearoutfit.bundle` | TFP | Mo' Power store gear outfit |
| `…\automatic_assets_twitchdrops\passngasstoregearhat.bundle` | TFP | Pass-N-Gas store gear hat |
| `…\automatic_assets_twitchdrops\passngasstoregearoutfit.bundle` | TFP | Pass-N-Gas store gear outfit |
| `…\automatic_assets_twitchdrops\pimphatblue.bundle` | TFP | Blue Pimp Hat drop |
| `…\automatic_assets_twitchdrops\pimphatpurple.bundle` | TFP | Purple Pimp Hat drop |
| `…\automatic_assets_twitchdrops\popnpillsstoregearhat.bundle` | TFP | Pop-N-Pills store gear hat |
| `…\automatic_assets_twitchdrops\popnpillsstoregearoutfit.bundle` | TFP | Pop-N-Pills store gear outfit |
| `…\automatic_assets_twitchdrops\savagecountrystoregearhat.bundle` | TFP | Savage Country store gear hat |
| `…\automatic_assets_twitchdrops\savagecountrystoregearoutfit.bundle` | TFP | Savage Country store gear outfit |
| `…\automatic_assets_twitchdrops\shamwaystoregearhat.bundle` | TFP | Shamway store gear hat |
| `…\automatic_assets_twitchdrops\shamwaystoregearoutfit.bundle` | TFP | Shamway store gear outfit |
| `…\automatic_assets_twitchdrops\shotgunmessiahstoregearhat.bundle` | TFP | Shotgun Messiah store gear hat |
| `…\automatic_assets_twitchdrops\shotgunmessiahstoregearoutfit.bundle` | TFP | Shotgun Messiah store gear outfit |
| `…\automatic_assets_twitchdrops\watcher.bundle` | TFP | Watcher Twitch drop |
| `…\automatic_assets_twitchdrops\workingstiffsstoregearhat.bundle` | TFP | Working Stiff's store gear hat |
| `…\automatic_assets_twitchdrops\workingstiffsstoregearoutfit.bundle` | TFP | Working Stiff's store gear outfit |

#### Texture Bundles (`textures_assets_textures\`)

| Path | Origin | Purpose |
| --- | --- | --- |
| `…\textures_assets_textures\environment.bundle` | TFP | Environment textures |
| `…\textures_assets_textures\graphics.bundle` | TFP | Graphics/rendering textures |
| `…\textures_assets_textures\hud.bundle` | TFP | HUD textures |
| `…\textures_assets_textures\ui.bundle` | TFP | UI textures |

#### Zombie Entity Bundles (`zombies_assets_entities\zombies\`)

| Path | Origin | Purpose |
| --- | --- | --- |
| `…\zombies_assets_entities\zombies\arlene.bundle` | TFP | Zombie Arlene model |
| `…\zombies_assets_entities\zombies\bigmama.bundle` | TFP | Zombie Big Mama model |
| `…\zombies_assets_entities\zombies\biker.bundle` | TFP | Zombie Biker model |
| `…\zombies_assets_entities\zombies\boe.bundle` | TFP | Zombie Boe model |
| `…\zombies_assets_entities\zombies\burnt.bundle` | TFP | Zombie Burnt model |
| `…\zombies_assets_entities\zombies\chuck.bundle` | TFP | Zombie Chuck model |
| `…\zombies_assets_entities\zombies\cocktailwaitress.bundle` | TFP | Zombie Cocktail Waitress model |
| `…\zombies_assets_entities\zombies\common.bundle` | TFP | Common zombie shared assets |
| `…\zombies_assets_entities\zombies\cop.bundle` | TFP | Zombie Cop model |
| `…\zombies_assets_entities\zombies\crawler.bundle` | TFP | Zombie Crawler model |
| `…\zombies_assets_entities\zombies\darlene.bundle` | TFP | Zombie Darlene model |
| `…\zombies_assets_entities\zombies\demolition.bundle` | TFP | Zombie Demolition model |
| `…\zombies_assets_entities\zombies\dog.bundle` | TFP | Zombie Dog model |
| `…\zombies_assets_entities\zombies\frostclaw.bundle` | TFP | Zombie Frostclaw model |
| `…\zombies_assets_entities\zombies\hawaiian.bundle` | TFP | Zombie Hawaiian model |
| `…\zombies_assets_entities\zombies\hazmat.bundle` | TFP | Zombie Hazmat model |
| `…\zombies_assets_entities\zombies\joe.bundle` | TFP | Zombie Joe model |
| `…\zombies_assets_entities\zombies\lab.bundle` | TFP | Zombie Lab model |
| `…\zombies_assets_entities\zombies\lumberjack.bundle` | TFP | Zombie Lumberjack model |
| `…\zombies_assets_entities\zombies\marlene.bundle` | TFP | Zombie Marlene model |
| `…\zombies_assets_entities\zombies\mechanic.bundle` | TFP | Zombie Mechanic model |
| `…\zombies_assets_entities\zombies\moe.bundle` | TFP | Zombie Moe model |
| `…\zombies_assets_entities\zombies\mutated.bundle` | TFP | Zombie Mutated model |
| `…\zombies_assets_entities\zombies\nurse.bundle` | TFP | Zombie Nurse model |
| `…\zombies_assets_entities\zombies\plaguespitter.bundle` | TFP | Plague Spitter model |
| `…\zombies_assets_entities\zombies\rancher.bundle` | TFP | Zombie Rancher model |
| `…\zombies_assets_entities\zombies\sand.bundle` | TFP | Zombie Sand model |
| `…\zombies_assets_entities\zombies\screamer.bundle` | TFP | Zombie Screamer model |
| `…\zombies_assets_entities\zombies\snow.bundle` | TFP | Zombie Snow model |
| `…\zombies_assets_entities\zombies\soldier.bundle` | TFP | Zombie Soldier model |
| `…\zombies_assets_entities\zombies\spider.bundle` | TFP | Zombie Spider model |
| `…\zombies_assets_entities\zombies\steve.bundle` | TFP | Zombie Steve model |
| `…\zombies_assets_entities\zombies\suit.bundle` | TFP | Zombie Suit model |
| `…\zombies_assets_entities\zombies\thug.bundle` | TFP | Zombie Thug model |
| `…\zombies_assets_entities\zombies\tomclark.bundle` | TFP | Zombie Tom Clark model |
| `…\zombies_assets_entities\zombies\wight.bundle` | TFP | Zombie Wight model |
| `…\zombies_assets_entities\zombies\worker.bundle` | TFP | Zombie Worker model |
| `…\zombies_assets_entities\zombies\yo.bundle` | TFP | Zombie Yo model |

#### Player Entity Bundles (`player_assets_entities\player\`)

Organized by gender → category. Both male and female have the same gear/hair sets.

| Path | Origin | Purpose |
| --- | --- | --- |
| `…\player\common.bundle` | TFP | Player common shared assets |
| `…\player\female\common.bundle` | TFP | Female player common assets |
| `…\player\male\common.bundle` | TFP | Male player common assets |

**Gear bundles** (`player\{female,male}\gear\`): `assassin`, `biker`, `commando`, `enforcer`, `farmer`, `fiber`, `fitness`, `lumberjack`, `miner`, `nerd`, `nomad`, `preacher`, `raider`, `ranger`, `santahat`, `scavenger`, `stealth` — each as a `.bundle` file.

**Hair bundles** (`player\{female,male}\hair\`): `afro_curly`, `buzzcut`, `comb_over`, `cornrows`, `dreads`, `flattop_fro`, `midpart_karen_messy`, `midpart_long`, `midpart_mid`, `midpart_short`, `midpart_shoulder`, `mohawk`, `pixie_cut`, `ponytail`, `sidepart_long`, `sidepart_mid`, `sidepart_short`, `slicked_back`, `slicked_back_long`, `small_fro` — each as a `.bundle` file.

**Head bundles** (`player\{female,male}\heads\{asian,black,native,white}\`): `01.bundle`, `02.bundle`, `03.bundle`, `04.bundle` — 4 variants per ethnicity per gender (32 head bundles total).

**Facial hair bundles** (male only) (`player\male\facialhair\`): `beard.bundle`, `chops.bundle`, `mustache.bundle`.

### `Data\Worlds\` — Pre-built Worlds

| Path | Origin | Purpose |
| --- | --- | --- |
| `Data\Worlds\Empty\` | TFP | Empty world template |
| `Data\Worlds\Navezgane\` | TFP | Hand-crafted official campaign map |
| `Data\Worlds\Playtesting\` | TFP | QA/testing world |
| `Data\Worlds\Pregen06k01\` | TFP | Pre-generated 6K random world #1 |
| `Data\Worlds\Pregen06k02\` | TFP | Pre-generated 6K random world #2 |
| `Data\Worlds\Pregen08k01\` | TFP | Pre-generated 8K random world #1 |
| `Data\Worlds\Pregen08k02\` | TFP | Pre-generated 8K random world #2 |

---

## `EasyAntiCheat\`

| Path | Origin | Purpose |
| --- | --- | --- |
| `EasyAntiCheat\EasyAntiCheat_EOS_Setup.exe` | EAC | EAC installer/setup |
| `EasyAntiCheat\install_eac.bat` | EAC | EAC install script |
| `EasyAntiCheat\uninstall_eac.bat` | EAC | EAC uninstall script |
| `EasyAntiCheat\Settings.json` | EAC | EAC configuration |
| `EasyAntiCheat\SplashScreen.png` | EAC | EAC loading splash image |
| `EasyAntiCheat\Certificates\base.bin` | EAC | EAC integrity certificate (binary) |
| `EasyAntiCheat\Certificates\base.cer` | EAC | EAC integrity certificate |
| `EasyAntiCheat\Certificates\runtime.conf` | EAC | EAC runtime configuration |
| `EasyAntiCheat\Licenses\Apache-2.0.txt` | EAC | Apache 2.0 license text |
| `EasyAntiCheat\Licenses\Licenses.txt` | EAC | Combined license notices |
| `EasyAntiCheat\Licenses\MIT.txt` | EAC | MIT license text |
| `EasyAntiCheat\Localization\ar_sa.cfg` | EAC | Arabic localization |
| `EasyAntiCheat\Localization\cs_cz.cfg` | EAC | Czech localization |
| `EasyAntiCheat\Localization\de_de.cfg` | EAC | German localization |
| `EasyAntiCheat\Localization\en_us.cfg` | EAC | English localization |
| `EasyAntiCheat\Localization\es_ar.cfg` | EAC | Spanish (Argentina) localization |
| `EasyAntiCheat\Localization\es_es.cfg` | EAC | Spanish (Spain) localization |
| `EasyAntiCheat\Localization\fr_fr.cfg` | EAC | French localization |
| `EasyAntiCheat\Localization\id_id.cfg` | EAC | Indonesian localization |
| `EasyAntiCheat\Localization\it_it.cfg` | EAC | Italian localization |
| `EasyAntiCheat\Localization\ja_ja.cfg` | EAC | Japanese localization |
| `EasyAntiCheat\Localization\ko_kr.cfg` | EAC | Korean localization |
| `EasyAntiCheat\Localization\nl_nl.cfg` | EAC | Dutch localization |
| `EasyAntiCheat\Localization\pl_pl.cfg` | EAC | Polish localization |
| `EasyAntiCheat\Localization\pt_br.cfg` | EAC | Portuguese (Brazil) localization |
| `EasyAntiCheat\Localization\ru_ru.cfg` | EAC | Russian localization |
| `EasyAntiCheat\Localization\th_th.cfg` | EAC | Thai localization |
| `EasyAntiCheat\Localization\tr_tr.cfg` | EAC | Turkish localization |
| `EasyAntiCheat\Localization\vi_vn.cfg` | EAC | Vietnamese localization |
| `EasyAntiCheat\Localization\zh_cn.cfg` | EAC | Chinese Simplified localization |
| `EasyAntiCheat\Localization\zh_tw.cfg` | EAC | Chinese Traditional localization |

---

## `Launcher\`

| Path | Origin | Purpose |
| --- | --- | --- |
| `Launcher\7dLauncher.po` | TFP | Launcher UI translations (English, PO format) |
| `Launcher\7dLauncher.de.po` | TFP | Launcher UI translations (German, PO format) |

---

## `Licenses\` — Third-Party License Files (19 files)

| Path | Origin | Purpose |
| --- | --- | --- |
| `Licenses\AmplifyMotion-MIT.txt` | 3rd | Amplify Motion — MIT license |
| `Licenses\ANTLR3-BSD.txt` | 3rd | ANTLR3 parser — BSD license |
| `Licenses\Backtrace-MIT.txt` | 3rd | Backtrace crash reporting — MIT license |
| `Licenses\cecil-MIT.txt` | 3rd | Mono.Cecil IL manipulation — MIT license |
| `Licenses\Crc32.NET-MIT.txt` | 3rd | CRC32 hash — MIT license |
| `Licenses\GameSense-MIT.txt` | 3rd | SteelSeries GameSense — MIT license |
| `Licenses\getRSS.c.txt` | 3rd | getRSS memory tracker — license |
| `Licenses\HarmonyX-MIT.txt` | 3rd | HarmonyX patching framework — MIT license |
| `Licenses\LibNoise-LGPL.txt` | 3rd | LibNoise noise generation — LGPL license |
| `Licenses\LiteNetLib-MIT.txt` | 3rd | LiteNetLib networking — MIT license |
| `Licenses\MemoryPack-MIT.txt` | 3rd | MemoryPack serialization — MIT license |
| `Licenses\MonoMod-MIT.txt` | 3rd | MonoMod runtime detour — MIT license |
| `Licenses\NCalc-MIT.txt` | 3rd | NCalc expression evaluator — MIT license |
| `Licenses\Ncalc2-MIT.txt` | 3rd | NCalc2 fork — MIT license |
| `Licenses\SharpEXR-MIT.txt` | 3rd | SharpEXR OpenEXR reader — MIT license |
| `Licenses\Steamworks.NET-MIT.txt` | 3rd | Steamworks.NET — MIT license |
| `Licenses\UniLinq.txt` | 3rd | UniLinq — license |
| `Licenses\Utf8Json-MIT.txt` | 3rd | Utf8Json serializer — MIT license |
| `Licenses\ZXing-Apache2.0.txt` | 3rd | ZXing barcode — Apache 2.0 license |

---

## `Logos\`

| Path | Origin | Purpose |
| --- | --- | --- |
| `Logos\SplashScreenImage.png` | TFP | Engine splash screen shown during startup |
| `Logos\Square150x150Logo.png` | TFP | App icon tile 150×150 |
| `Logos\Square44x44Logo.png` | TFP | App icon tile 44×44 |
| `Logos\Square480x480Logo.png` | TFP | App icon tile 480×480 |
| `Logos\StoreLogo.png` | TFP | Store listing logo |

---

## `MonoBleedingEdge\` — Mono Runtime

| Path | Origin | Purpose |
| --- | --- | --- |
| `MonoBleedingEdge\EmbedRuntime\mono-2.0-bdwgc.dll` | .NET (Mono) | Mono runtime with Boehm-Demers-Weiser GC (the C# virtual machine) |
| `MonoBleedingEdge\EmbedRuntime\MonoPosixHelper.dll` | .NET (Mono) | POSIX helper for Mono |
| `MonoBleedingEdge\etc\mono\browscap.ini` | .NET (Mono) | Browser capability definitions |
| `MonoBleedingEdge\etc\mono\config` | .NET (Mono) | Mono DLL mapping configuration |
| `MonoBleedingEdge\etc\mono\2.0\machine.config` | .NET (Mono) | .NET 2.0 machine configuration |
| `MonoBleedingEdge\etc\mono\2.0\settings.map` | .NET (Mono) | .NET 2.0 settings mapping |
| `MonoBleedingEdge\etc\mono\2.0\web.config` | .NET (Mono) | .NET 2.0 web configuration |
| `MonoBleedingEdge\etc\mono\2.0\DefaultWsdlHelpGenerator.aspx` | .NET (Mono) | WSDL help page template |
| `MonoBleedingEdge\etc\mono\2.0\Browsers\Compat.browser` | .NET (Mono) | Browser compatibility definitions |
| `MonoBleedingEdge\etc\mono\4.0\machine.config` | .NET (Mono) | .NET 4.0 machine configuration |
| `MonoBleedingEdge\etc\mono\4.0\settings.map` | .NET (Mono) | .NET 4.0 settings mapping |
| `MonoBleedingEdge\etc\mono\4.0\web.config` | .NET (Mono) | .NET 4.0 web configuration |
| `MonoBleedingEdge\etc\mono\4.0\DefaultWsdlHelpGenerator.aspx` | .NET (Mono) | WSDL help page template |
| `MonoBleedingEdge\etc\mono\4.0\Browsers\Compat.browser` | .NET (Mono) | Browser compatibility definitions |
| `MonoBleedingEdge\etc\mono\4.5\machine.config` | .NET (Mono) | .NET 4.5 machine configuration |
| `MonoBleedingEdge\etc\mono\4.5\settings.map` | .NET (Mono) | .NET 4.5 settings mapping |
| `MonoBleedingEdge\etc\mono\4.5\web.config` | .NET (Mono) | .NET 4.5 web configuration |
| `MonoBleedingEdge\etc\mono\4.5\DefaultWsdlHelpGenerator.aspx` | .NET (Mono) | WSDL help page template |
| `MonoBleedingEdge\etc\mono\4.5\Browsers\Compat.browser` | .NET (Mono) | Browser compatibility definitions |
| `MonoBleedingEdge\etc\mono\mconfig\config.xml` | .NET (Mono) | Mono configuration tool settings |

---

## `Mods\` — Installed Mods

### `Mods\0_TFP_Harmony\` — Official TFP Harmony Framework

Loaded first due to `0_` prefix. Ships the HarmonyX runtime and TFP's own Harmony patches.

| Path | Origin | Purpose |
| --- | --- | --- |
| `Mods\0_TFP_Harmony\ModInfo.xml` | TFP | Mod metadata |
| `Mods\0_TFP_Harmony\TfpHarmony.dll` | TFP | TFP's own Harmony patches |
| `Mods\0_TFP_Harmony\TfpHarmony.pdb` | TFP | Debug symbols for TfpHarmony |
| `Mods\0_TFP_Harmony\0Harmony.dll` | 3rd (HarmonyX) | HarmonyX patching framework runtime |
| `Mods\0_TFP_Harmony\Mono.Cecil.dll` | 3rd | Mono.Cecil — IL assembly reading/writing |
| `Mods\0_TFP_Harmony\Mono.Cecil.Mdb.dll` | 3rd | Cecil MDB debug symbol support |
| `Mods\0_TFP_Harmony\Mono.Cecil.Pdb.dll` | 3rd | Cecil PDB debug symbol support |
| `Mods\0_TFP_Harmony\Mono.Cecil.Rocks.dll` | 3rd | Cecil utility extensions |
| `Mods\0_TFP_Harmony\MonoMod.Backports.dll` | 3rd | MonoMod .NET backports |
| `Mods\0_TFP_Harmony\MonoMod.Core.dll` | 3rd | MonoMod core detouring engine |
| `Mods\0_TFP_Harmony\MonoMod.Iced.dll` | 3rd | MonoMod x86/x64 instruction decoder (Iced) |
| `Mods\0_TFP_Harmony\MonoMod.ILHelpers.dll` | 3rd | MonoMod IL manipulation helpers |
| `Mods\0_TFP_Harmony\MonoMod.RuntimeDetour.dll` | 3rd | MonoMod runtime method detouring |
| `Mods\0_TFP_Harmony\MonoMod.Utils.dll` | 3rd | MonoMod utilities |
| `Mods\0_TFP_Harmony\System.ValueTuple.dll` | .NET | ValueTuple polyfill for older .NET |

### Third-Party Mods (Z_ prefix)

| Path | Origin | Purpose |
| --- | --- | --- |
| `Mods\Z_Armor_Balance\` | 3rd (community) | Armor balance adjustments |
| `Mods\Z_Armor_Improved\` | 3rd (community) | Improved armor system |
| `Mods\Z_Better_Quest_Reward\` | 3rd (community) | Enhanced quest rewards |
| `Mods\Z_Better_Stacks\` | 3rd (community) | Increased stack sizes |
| `Mods\Z_BigInv98slots\` | 3rd (community) | 98-slot inventory expansion |
| `Mods\Z_Bosses\` | 3rd (community) | Boss zombie encounters |
| `Mods\Z_Combinations\` | 3rd (community) | Item combination recipes |
| `Mods\Z_Contracts\` | 3rd (community) | Contract system |
| `Mods\Z_Craft_Ammo\` | 3rd (community) | Ammunition crafting changes |
| `Mods\Z_DECO\` | 3rd (community) | Decorative blocks/items |
| `Mods\Z_EliteZombies\` | 3rd (community) | Elite zombie variants |
| `Mods\Z_FearAndFatigue\` | 3rd (community) | Fear and fatigue mechanics |
| `Mods\Z_Game_Balance\` | 3rd (community) | General game balance changes |
| `Mods\Z_HUD\` | 3rd (community) | HUD modifications |
| `Mods\Z_Master_Skills\` | 3rd (community) | Master skill tree |
| `Mods\Z_Mining_Balance\` | 3rd (community) | Mining balance adjustments |
| `Mods\Z_PassiveSkills\` | 3rd (community) | Passive skill system |
| `Mods\Z_Perfection\` | 3rd (community) | Perfection system |
| `Mods\Z_Radiostation\` | 3rd (community) | Radio station gameplay feature |
| `Mods\Z_RareItems\` | 3rd (community) | Rare item drops |
| `Mods\Z_RareResources\` | 3rd (community) | Rare resource system |
| `Mods\Z_Rare_Modifiers\` | 3rd (community) | Rare item modifiers |
| `Mods\Z_RepairToolsXP\` | 3rd (community) | XP from tool repair |
| `Mods\Z_RoughTerrain\` | 3rd (community) | Rough terrain modifications |
| `Mods\Z_SelfTraits\` | 3rd (community) | Self-trait character system |
| `Mods\Z_Story\` | 3rd (community) | Story/quest content |
| `Mods\Z_SuperElixirs\` | 3rd (community) | Super elixir consumables |
| `Mods\Z_Universal_Parts\` | 3rd (community) | Universal crafting parts |
| `Mods\Z_Vulnerability\` | 3rd (community) | Vulnerability system |
