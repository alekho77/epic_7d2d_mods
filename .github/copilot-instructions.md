# epic_7d2d_mods — Copilot Instructions

This repository contains **7 Days to Die** modlets authored by **Aleksei Khozin** for the **EpicVales** Steam group. The `EV_` prefix in all mod folder names stands for *EpicVales*.

## General Instructions

### Language
- All code, comments, XML, Markdown files, and instructions must be written in **English**.
- Respond in the same language the user used in their request.
- Always append exactly **one sentence in English** at the very end of every reply summarizing what was done, regardless of the request language.

### Git Commit Policy
- **Never suggest committing changes** unless explicitly asked by the user.
- When a commit is requested, execute it using console `git` commands.
- Commit message must be exactly one sentence in English.

## Project Structure

All modlets live under the `/Mods` folder in the repository root. Each mod is a self-contained subfolder and **must** use the `EV_` prefix in its name:

```
Mods/
  EV_<ModName>/
    ModInfo.xml          # Required — name, version, author, description
    Config/              # XML overrides (items, blocks, recipes, entityclasses, etc.)
    Resources/           # Unity asset bundles, textures, sounds (optional)
    UIAtlases/           # Custom UI sprites (optional)
    Harmony/             # C# Harmony patches compiled to a DLL (optional)
```

## Key Conventions

- **All game data is XML.** 7D2D uses an xpath-based patching system — mod `Config/` files patch vanilla XML, they do not replace it.
- **XPath operations**: `set`, `append`, `insertAfter`, `insertBefore`, `remove`, `removeAttribute`, `setattribute`, `add`.
- **`ModInfo.xml` is mandatory** for every modlet and must follow the exact schema the game expects.
- Mod folder names must use the `EV_` prefix followed by `PascalCase` with no spaces (e.g., `EV_EnhancedMagnumDamage`).
- Keep each modlet focused on a single concern (e.g., one mod = one feature/overhaul).

## XML Patching Example

```xml
<!-- Config/items.xml -->
<configs>
  <!-- Append a new item -->
  <append xpath="/items">
    <item name="myCustomItem">
      <property name="Extends" value="meleeToolPickaxeT1Iron"/>
    </item>
  </append>

  <!-- Override a value on an existing item -->
  <set xpath="/items/item[@name='meleeToolPickaxeT1Iron']/property[@name='MagazineSize']/@value">50</set>
</configs>
```

## ModInfo.xml Schema

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ModInfo>
  <Name value="MyModName"/>
  <DisplayName value="My Mod Display Name"/>
  <Description value="Short description of what this mod does."/>
  <Author value="Aleksei Khozin"/>
  <Version value="1.0.0"/>
  <Website value="https://github.com/alekho77/epic_7d2d_mods"/>
</ModInfo>
```

## Vanilla Config Reference (Source of Truth)

The repository contains a `/Config` folder with the **original unmodified game configuration files**.

> **CRITICAL**: Before writing or modifying any mod, always read the relevant vanilla file(s) from `/Config` first.
> These files are the authoritative source for item names, property keys, buff IDs, perk names, UI elements, entity names, and all inter-file relationships.
> Never guess or assume values — look them up in the source files.

### Config File Reference

| File | Controls |
|------|----------|
| `items.xml` | All holdable items, weapons, tools, consumables and their properties |
| `blocks.xml` | Placeable world blocks and their properties |
| `recipes.xml` | Crafting recipes and ingredient lists |
| `loot.xml` | Loot containers, groups, and probability tables |
| `entityclasses.xml` | NPCs, zombies, animals — classes and AI properties |
| `entitygroups.xml` | Named groups of entities used by spawning/gamestages |
| `buffs.xml` | Player and entity buffs/debuffs and their effects |
| `progression.xml` | Skills, perks, leveling, and attribute trees |
| `gamestages.xml` | Horde night waves and spawn scaling by game stage |
| `spawning.xml` | Biome and zone spawning rules |
| `traders.xml` | Trader inventories, tiers, and quest offerings |
| `vehicles.xml` | Driveable vehicles and their properties |
| `item_modifiers.xml` | Weapon and tool attachments/mods |
| `qualityinfo.xml` | Item quality tiers and stat scaling |
| `archetypes.xml` | Entity archetypes (base templates for entityclasses) |
| `biomes.xml` | Biome definitions and surface/decoration rules |
| `challenges.xml` | In-game challenges and objectives |
| `events.xml` / `gameevents.xml` | Game event triggers and responses |
| `materials.xml` | Block material properties (hardness, damage types) |
| `quests.xml` | Quest definitions and reward tables |
| `rwgmixer.xml` | Random world generation settings |
| `shapes.xml` | Block shape definitions |
| `sounds.xml` | Sound event mappings |
| `weathersurvival.xml` | Weather and survival stat effects |
| `worldglobal.xml` | Global world settings |
| `ui_display.xml` | Stat/property display labels for the UI |
| `misc.xml` | Miscellaneous global game variables |
| `physicsbodies.xml` | Ragdoll/physics body definitions |
| `painting.xml` | Block painting textures |
| `nav_objects.xml` | Minimap/compass navigation icons |
| `music.xml` | Background music event mappings |
| `subtitles.xml` | Subtitle entries for audio events |
| `utilityai.xml` | AI utility scoring and behaviour trees |
| `dialogs.xml` | NPC dialog trees (trader conversations) |
| `npc.xml` | NPC-specific settings |
| `dmscontent.xml` | Diersville map static content |
| `twitch.xml` / `twitch_events.xml` | Twitch integration events |
| `videos.xml` | Intro/cutscene video references |
| `loadingscreen.xml` | Loading screen tip entries |
| `Localization.txt` | All in-game strings (key → language columns) |
| `BlockUpdates.csv` | Block upgrade/downgrade transition table |
| `Stealth.txt` | Stealth system parameters |
| `XML.txt` | Notes on the XML patching system |
| `XUi/` | In-game HUD and UI: `windows.xml`, `controls.xml`, `styles.xml`, `xui.xml` |
| `XUi_Common/` | Shared UI components: `controls.xml`, `styles.xml` |
| `XUi_Menu/` | Main menu UI: `windows.xml`, `controls.xml`, `styles.xml`, `xui.xml` |

## Game Version

Target the **latest stable release** unless the user explicitly specifies a different version in their request.

When searching forums, wikis, or any external materials: first determine the current latest stable version of 7 Days to Die, then scope all searches and references to that version. Modding APIs, XML schemas, and property names can differ significantly between versions.

## Testing Mods

The modded game installation path is stored in the environment variable `7D2D_MODED`.

1. Copy (or symlink) the mod folder into `$env:7D2D_MODED\Mods\`.
2. Launch the game — mod errors appear in `%APPDATA%\7DaysToDie\output_log.txt`.
3. The game validates XML on load; xpath errors are logged with the offending file and line.

## Anti-patterns

- Do **not** wrap multiple unrelated changes in a single modlet.
- Avoid editing vanilla config files directly — always use xpath patches.
- Do not use spaces in mod folder names or XML `name` attribute values for items/blocks if possible.
