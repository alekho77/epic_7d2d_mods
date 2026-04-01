# Phase 2: Harmony Mods

**[Back to Modding Guide](modding_guide.md)** | **Previous: [Phase 1 — XML Modlets](phase1_xml_modlets.md)** | **Next: [Phase 3 — Total Conversion](phase3_total_conversion.md)**

Harmony mods use the **HarmonyX** runtime patching framework to modify game C# code at runtime without altering the original DLL files. This enables changes that are impossible with XML alone: new game mechanics, custom UI behaviors, altered AI routines, new console commands, network protocol changes, and more.

> **Prerequisite**: You should be comfortable with Phase 1 (XML modlets) before starting Harmony modding. Most Harmony mods also include XML patches.

---

## How Harmony Patching Works

1. The game loads your mod's DLL(s) from `Mods\YourMod\Harmony\`.
2. The HarmonyX framework reads `[HarmonyPatch]` attributes on your classes.
3. At runtime, Harmony **injects** your code before (Prefix), after (Postfix), or inside (Transpiler) the original game methods.
4. The original `Assembly-CSharp.dll` is **never modified on disk** — patches are applied in memory only.

### Patch Types

| Type | When It Runs | Use Case |
| --- | --- | --- |
| **Prefix** | Before the original method | Modify input parameters, skip the original method entirely (`return false`), add pre-checks |
| **Postfix** | After the original method | Modify return values, add side effects, read results |
| **Transpiler** | Rewrites IL instructions | Surgical changes to method internals (advanced) |
| **Finalizer** | After method (even on exception) | Exception handling, guaranteed cleanup |

---

## Required Tools

| Tool | Purpose |
| --- | --- |
| **dnSpy** or **ILSpy** | Decompile `Assembly-CSharp.dll` to read game source code. **Essential** — you cannot write patches without knowing the original code. |
| **Visual Studio** or **JetBrains Rider** | Write and compile your Harmony mod C# project |
| **.NET Framework 4.8 SDK** | The game targets .NET Framework (Mono runtime) |
| **NuGet** (or manual references) | Reference game DLLs in your project |

---

## Harmony Mod Folder Structure

```text
Mods\
  MyHarmonyMod\
    ModInfo.xml              # Required — same as XML modlets
    Harmony\
      MyHarmonyMod.dll       # Your compiled C# assembly
    Config\                  # Optional — XML patches (Phase 1)
      items.xml
      Localization.txt
```

The game auto-discovers and loads all `.dll` files in the `Harmony\` folder.

---

## Files to Study with dnSpy / ILSpy

### Essential (Must Decompile)

| File | Location | What to Study |
| --- | --- | --- |
| `Assembly-CSharp.dll` | `7DaysToDie_Data\Managed\` | **The main game code.** All game logic lives here: item system (`ItemClass`, `ItemValue`, `ItemAction*`), block system (`Block`, `BlockValue`), entity system (`Entity`, `EntityAlive`, `EntityPlayer`, `EntityZombie`), crafting (`Recipe`, `CraftingManager`), loot (`LootContainer`, `LootManager`), buff system (`BuffClass`, `MinEffectController`), progression (`Progression`, `ProgressionClass`), UI controllers (`XUiC_*`), world generation (`ChunkProviderGenerateWorld`), networking (`NetPackage*`), AI (`EAI*` tasks), console commands (`ConsoleCmdAbstract`). |
| `Assembly-CSharp-firstpass.dll` | `7DaysToDie_Data\Managed\` | Early-init utilities, base types loaded before the main assembly. Contains foundational helpers used throughout the game. |
| `0Harmony.dll` | `7DaysToDie_Data\Managed\` | The HarmonyX framework itself. Study its API: `Harmony`, `HarmonyPatch`, `HarmonyPrefix`, `HarmonyPostfix`, `HarmonyTranspiler`, `AccessTools`, `CodeInstruction`. |

### Useful (Study When Needed)

| File | Location | What to Study |
| --- | --- | --- |
| `NGUI.dll` | `7DaysToDie_Data\Managed\` | The game's UI framework. Not standard Unity UI — it uses NGUI (`UILabel`, `UISprite`, `UIWidget`, `UIPanel`, `UIGrid`). Study this when patching UI behavior. |
| `NCalc.dll` | `7DaysToDie_Data\Managed\` | Math expression evaluator. Used in `buffs.xml` and `progression.xml` for dynamic formulas. Understanding the evaluator helps when creating custom effects. |
| `AstarPathfindingProject.dll` | `7DaysToDie_Data\Managed\` | A* Pathfinding Project Pro. Handles NPC/zombie navigation. Study when modifying entity movement, pathfinding, or creating custom AI. |
| `LogLibrary.dll` | `7DaysToDie_Data\Managed\` | TFP's custom logging library. Useful for understanding the game's internal logging. |

### Reference (Occasional Lookup)

| File | Location | What to Study |
| --- | --- | --- |
| `InControl.dll` | `7DaysToDie_Data\Managed\` | Input mapping framework. Study when patching input handling or adding custom keybinds. |
| `LiteNetLib.dll` | `7DaysToDie_Data\Managed\` | UDP networking library. Study when modifying multiplayer behavior or adding net-synced features. |
| `MemoryPack.Core.dll` | `7DaysToDie_Data\Managed\` | Binary serialization for save data and network packets. Study when patching save/load or network sync. |
| `com.rlabrecque.steamworks.net.dll` | `7DaysToDie_Data\Managed\` | Steamworks.NET wrapper. Study for Steam API hooks (achievements, lobbies). |
| `Mono.Cecil.dll` | `7DaysToDie_Data\Managed\` | IL manipulation library used internally by Harmony. Reference for advanced Transpiler work. |
| `MonoMod.RuntimeDetour.dll` | `7DaysToDie_Data\Managed\` | Low-level method detouring (used by HarmonyX). |
| `UnityEngine.CoreModule.dll` | `7DaysToDie_Data\Managed\` | Unity core types: `GameObject`, `MonoBehaviour`, `Transform`. Reference for understanding Unity object lifecycle. |
| `UnityEngine.PhysicsModule.dll` | `7DaysToDie_Data\Managed\` | Physics, raycasts, colliders. Reference for patching physics interactions. |
| `UnityEngine.UI.dll` | `7DaysToDie_Data\Managed\` | Standard Unity UI (not primarily used by the game, which uses NGUI). |
| `Unity.Addressables.dll` | `7DaysToDie_Data\Managed\` | Addressable Asset System. Reference for understanding asset loading. |

### Official TFP Harmony Example

| Path | Purpose |
| --- | --- |
| `Mods\0_TFP_Harmony\` | The Fun Pimps' official Harmony mod. Study its DLL structure and patches as a reference for how TFP themselves use Harmony. Loaded first (prefix `0_`). |

---

## Key Game Classes to Know

These are the most commonly patched classes in `Assembly-CSharp.dll`:

### Items and Inventory

| Class | Responsibility |
| --- | --- |
| `ItemClass` | Base class for all item definitions. Properties, actions, effects. |
| `ItemValue` | Runtime instance of an item: quality, durability, mods, metadata. |
| `ItemAction` | Base class for item actions (use, attack, place). |
| `ItemActionAttack` | Melee attack action. |
| `ItemActionRanged` | Ranged weapon firing. |
| `ItemActionEat` | Consumable use action. |
| `ItemStack` | Stack of items (ItemValue + count). |
| `Inventory` | Player inventory management. |
| `XUiC_ItemStack` | UI controller for item slot display. |

### Blocks and World

| Class | Responsibility |
| --- | --- |
| `Block` | Base class for all block definitions. |
| `BlockValue` | Runtime instance of a placed block. |
| `BlockShape` | 3D shape of a block. |
| `World` | The game world: chunk management, block access, entity tracking. |
| `Chunk` | Single world chunk (16×256×16 blocks). |
| `ChunkProviderGenerateWorld` | Random world generation. |

### Entities

| Class | Responsibility |
| --- | --- |
| `Entity` | Base class for all world entities. |
| `EntityAlive` | Living entity: health, buffs, death, inventory. |
| `EntityPlayer` | The player. |
| `EntityPlayerLocal` | The local (controlling) player. |
| `EntityZombie` | Zombie entity. |
| `EntityAnimal` | Animal entity. |
| `EntityTrader` | Trader NPC. |
| `EntityNPC` | Generic NPC. |

### Buffs and Effects

| Class | Responsibility |
| --- | --- |
| `BuffClass` | Buff definition (loaded from `buffs.xml`). |
| `BuffValue` | Runtime buff instance on an entity. |
| `MinEffectController` | Manages active effects on an entity. |
| `MinEffectGroup` | Group of passive/triggered effects. |

### Crafting and Recipes

| Class | Responsibility |
| --- | --- |
| `Recipe` | Crafting recipe definition. |
| `CraftingManager` | Manages crafting queue and recipe lookup. |
| `XUiC_CraftingQueue` | UI controller for the crafting queue. |

### Loot

| Class | Responsibility |
| --- | --- |
| `LootContainer` | Loot container definition. |
| `LootManager` | Manages loot generation. |

### Progression and Skills

| Class | Responsibility |
| --- | --- |
| `Progression` | Player's progression state (level, XP, skill points). |
| `ProgressionClass` | Skill/perk definition. |
| `ProgressionValue` | Current level of a specific perk. |

### UI System

| Class | Responsibility |
| --- | --- |
| `XUi` | Main XUi system manager. |
| `XUiController` | Base class for all UI controllers. |
| `XUiC_*` | Specific UI controllers: `XUiC_ItemStack`, `XUiC_RecipeList`, `XUiC_MapArea`, etc. |
| `XUiView` | View layer of the XUi system. |
| `GUIWindowManager` | Legacy window management. |

### AI

| Class | Responsibility |
| --- | --- |
| `EAIManager` | Entity AI manager. |
| `EAITask*` | Individual AI tasks: `EAITaskWander`, `EAITaskApproachAndAttack`, `EAITaskInvestigate`, etc. |

### Networking

| Class | Responsibility |
| --- | --- |
| `NetPackage` | Base class for network packets. |
| `NetPackage*` | Specific packet types for every networked action. |
| `ConnectionManager` | Manages multiplayer connections. |

### Console Commands

| Class | Responsibility |
| --- | --- |
| `ConsoleCmdAbstract` | Base class for console commands. Subclass this to add new commands. |
| `SdtdConsole` | Console system manager. |

---

## Minimal Harmony Mod Example

### Project Setup

1. Create a new **.NET Framework 4.8 Class Library** project.
2. Add references to (copy from `7DaysToDie_Data\Managed\`):
   - `Assembly-CSharp.dll`
   - `Assembly-CSharp-firstpass.dll`
   - `0Harmony.dll`
   - `UnityEngine.dll`
   - `UnityEngine.CoreModule.dll`
   - `LogLibrary.dll` (if using game logging)
3. Set **Copy Local = false** for all game references (they're already in the game folder).
4. Build the DLL and place it in `Mods\YourMod\Harmony\`.

### Example: Modify Melee Damage

```csharp
using HarmonyLib;
using System.Reflection;

// The mod's init class — Harmony auto-discovers [HarmonyPatch] classes
public class MyMod : IModApi
{
    public void InitMod(Mod _modInstance)
    {
        var harmony = new Harmony("com.myname.mymod");
        harmony.PatchAll(Assembly.GetExecutingAssembly());
        Log.Out("[MyMod] Harmony patches applied.");
    }
}

// Postfix patch: multiply all melee damage by 1.5x
[HarmonyPatch(typeof(ItemActionAttack))]
[HarmonyPatch("Hit")]
public class ItemActionAttack_Hit_Patch
{
    [HarmonyPrefix]
    public static void Prefix(WorldRayHitInfo hitInfo, ref float _damageScale)
    {
        _damageScale *= 1.5f;
    }
}
```

### Example: Add a Console Command

```csharp
public class ConsoleCmdHeal : ConsoleCmdAbstract
{
    public override string[] getCommands() => new[] { "heal" };

    public override string getDescription() => "Fully heals the local player";

    public override void Execute(List<string> _params, CommandSenderInfo _senderInfo)
    {
        var player = GameManager.Instance.World?.GetPrimaryPlayer();
        if (player != null)
        {
            player.Health = player.GetMaxHealth();
            player.Stamina = player.GetMaxStamina();
            Log.Out("[MyMod] Player healed.");
        }
    }
}
```

---

## The IModApi Interface

The game looks for classes implementing `IModApi` in your DLL:

```csharp
public interface IModApi
{
    void InitMod(Mod _modInstance);
}
```

- `InitMod` is called when the game loads your mod.
- Use it to apply Harmony patches, register event handlers, or initialize your mod's state.
- The `Mod` parameter provides access to the mod's path and `ModInfo.xml` data.

---

## Harmony Best Practices

### Do

- **Always decompile first.** Open `Assembly-CSharp.dll` in dnSpy and read the exact method signature before writing a patch.
- **Use Prefix for input modification**, Postfix for output modification.
- **Keep patches minimal.** Patch the smallest possible method to reduce compatibility conflicts with other mods.
- **Use `AccessTools`** for reflection: `AccessTools.Field(typeof(SomeClass), "privateField")`.
- **Log your patches.** Use `Log.Out("[YourMod] message")` for debugging.
- **Handle null checks.** The game state may be in unexpected states during loading/unloading.
- **Test in single-player first**, then verify multiplayer compatibility.

### Don't

- **Don't modify game DLLs on disk.** Always use runtime Harmony patches.
- **Don't patch too broadly.** Patching `Update()` on a core class runs your code every frame — use targeted patches.
- **Don't assume load order.** Other Harmony mods may patch the same methods. Use `HarmonyBefore`/`HarmonyAfter` attributes if needed.
- **Don't forget network sync.** If your patch changes game state, ensure it runs on both client and server in multiplayer.
- **Don't reference Harmony internals.** Only use the public API.

---

## Debugging Harmony Mods

1. **Check `output_log.txt`** (`%APPDATA%\7DaysToDie\output_log.txt`) for exceptions and your `Log.Out` messages.
2. **Use dnSpy's debugger** — attach to the running game process for breakpoints and inspection.
3. **Harmony debug logging** — enable verbose Harmony logs:

   ```csharp
   Harmony.DEBUG = true;
   ```

   This writes detailed patch application logs to the Player.log.
4. **Common errors**:
   - `MissingMethodException` — Method signature changed between game versions. Re-check in dnSpy.
   - `AmbiguousMatchException` — Multiple method overloads. Use `HarmonyPatch` with parameter types:

     ```csharp
     [HarmonyPatch(typeof(SomeClass), "Method", new Type[] { typeof(int), typeof(string) })]
     ```

   - `NullReferenceException` in Prefix — The game object may not be initialized yet. Add null checks.

---

## Combining Harmony with XML

Most real mods use **both** Harmony and XML:

```text
Mods\
  MyFullMod\
    ModInfo.xml
    Harmony\
      MyFullMod.dll          # C# logic patches
    Config\
      items.xml              # New items/stat changes
      recipes.xml            # New recipes
      buffs.xml              # New buffs (data)
      progression.xml        # New perks (data)
      Localization.txt       # Text for new content
```

- Use **XML** for all data changes (items, recipes, loot, buffs, UI layout).
- Use **Harmony** only for behavioral changes that XML cannot express (new mechanics, altered logic, custom UI controllers).

---

## EAC Considerations

- **Harmony mods require EAC to be disabled.** Launch `7DaysToDie.exe` directly.
- Servers running Harmony mods must disable EAC.
- All clients connecting to a modded server must also disable EAC.
- There is no way to use Harmony mods with EAC active.

---

*[Back to Modding Guide](modding_guide.md)* | *Previous: [Phase 1 — XML Modlets](phase1_xml_modlets.md)* | *Next: [Phase 3 — Total Conversion](phase3_total_conversion.md)*
