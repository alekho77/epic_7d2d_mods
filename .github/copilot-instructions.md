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
    ModInfo.xml              # Required — name, version, author, description
    README.md                # Required — GitHub description (Markdown)
    NEXUS_DESCRIPTION.txt    # Required — Nexus Mods description (BBCode)
    Config/                  # XML overrides (items, blocks, recipes, entityclasses, etc.)
    Resources/               # Unity asset bundles, textures, sounds (optional)
    UIAtlases/               # Custom UI sprites (optional)
    Harmony/                 # C# Harmony patches compiled to a DLL (optional)
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

## Vanilla Game Data Reference (Source of Truth)

The repository contains a `/Data` folder with the **complete original unmodified game data** — a full copy of the `Data\` directory from the vanilla 7 Days to Die installation. Its structure mirrors the game installation as documented in `docs/modding_guide.md`:

| Subfolder | Contents |
|-----------|----------|
| `Data/Config/` | All XML configuration files — the primary modding reference |
| `Data/Prefabs/` | POI prefab definitions |
| `Data/ItemIcons/` | Item icon textures |
| `Data/Bundles/` | Legacy Unity AssetBundles |
| `Data/Addressables/` | Unity Addressables catalog and assets |
| `Data/Music/` | Background music tracks |
| `Data/Worlds/` | Bundled world maps |
| `Data/Stamps/` | World generation stamp assets |

> **CRITICAL**: Before writing or modifying any mod, always read the relevant vanilla file(s) from `/Data/Config` first.
> These files are the authoritative source for item names, property keys, buff IDs, perk names, UI elements, entity names, and all inter-file relationships.
> Never guess or assume values — look them up in the source files.
>
> When a request involves non-config assets (icons, prefabs, bundles, etc.), consult the relevant subfolder under `/Data` as well.

### Inventory Object Catalog (`docs/inventory_catalog.md`)

The file `docs/inventory_catalog.md` is a **pre-built catalog of all game objects** (items, blocks, and item modifiers) generated from the vanilla XML configs. Use it as the **first lookup step** when working with game objects:

1. **Find an object ID by name or description.** When the user refers to an object by its English name, Russian name, or description — search `docs/inventory_catalog.md` to resolve the internal ID (e.g., `gunHandgunT2Magnum44`).
2. **Browse object groups and categories.** The catalog is organized into categorized sections (Ranged Weapons, Melee Weapons, Loot Containers, Armor Mods, etc.) — use these to discover related objects or get a list of IDs in a specific group.
3. **Look up detailed properties in XML configs.** Once the internal ID is known, search the corresponding XML config file (`items.xml`, `blocks.xml`, or `item_modifiers.xml` under `/Data/Config/`) by the `name` attribute to find its full property set, effects, recipes, and relationships.

> **Workflow**: user description/name → search `docs/inventory_catalog.md` → get internal ID → search `/Data/Config/*.xml` by that ID for full details.

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

All files listed above are located under `/Data/Config/`.

## Game Version

Target the **latest stable release** unless the user explicitly specifies a different version in their request.

When searching forums, wikis, or any external materials: first determine the current latest stable version of 7 Days to Die, then scope all searches and references to that version. Modding APIs, XML schemas, and property names can differ significantly between versions.

## Testing Mods

The modded game installation path is stored in the environment variable `7D2D_MODED`.

1. Copy (or symlink) the mod folder into `$env:7D2D_MODED\Mods\`.
2. Launch the game — mod errors appear in `%APPDATA%\7DaysToDie\output_log.txt`.
3. The game validates XML on load; xpath errors are logged with the offending file and line.

## Nexus Mods Description (`NEXUS_DESCRIPTION.txt`)

Every modlet **must** include a `NEXUS_DESCRIPTION.txt` alongside its `README.md`. This file contains the mod description formatted in **BBCode** for direct copy-paste into a Nexus Mods page. When creating or updating a mod's `README.md`, always generate or update `NEXUS_DESCRIPTION.txt` as well.

### File Location

```
Mods/
  EV_<ModName>/
    README.md              # GitHub — Markdown
    NEXUS_DESCRIPTION.txt  # Nexus Mods — BBCode
```

### Mod Description Structure

Both `README.md` and `NEXUS_DESCRIPTION.txt` **must** follow the same section order. The structure merges our conventions with the [Nexus Mods recommended layout](https://wiki.nexusmods.com/index.php/Mod_description_best_practices).

| # | Section | Required | Purpose |
|---|---------|----------|---------|
| 1 | **Title** | ✅ | Human-readable mod name (not the folder name). In Markdown: `# Mod Title`. In BBCode: `[size=6][b]Mod Title[/b][/size]`. |
| 2 | **Description** | ✅ | `## Description` — one or two sentences explaining the main purpose. Followed by the server-side / client-side badge blockquote (see below). |
| 3 | **Features** | ✅ | `## Features` — bullet list of core features. |
| 4 | **How It Works** | optional | `## How It Works` — technical details for advanced users (xpath logic, formula, passive effect explanation). Include only when the mechanism is not obvious. |
| 5 | **Installation** | ✅ | `## Installation` — numbered steps to install the mod. |
| 6 | **Compatibility** | ✅ | `## Compatibility` — game version, mod type (server-side / client-side), and known conflicts. |
| 7 | **Changelog** | ✅ | `## Changelog` — version history with `### vX.Y.Z` sub-headings. |
| 8 | **Credits** | optional | `## Credits` — acknowledgements, inspirations, contributors. Omit if there are none. |
| 9 | **Footer** | ✅ | `---` separator followed by **Author**, **Version**, **Website** (Markdown only; omit in BBCode). |

#### Server-Side / Client-Side Badge

Place the badge inside a blockquote immediately after the description text:

**Markdown (server-side):**
```markdown
> ### 🟢 Server-Side Friendly
>
> **If you are running a dedicated server, this mod only needs to be installed on the server.**
> Players connecting to the server **do not need to download or install anything** on their game clients — all changes are synced automatically when they join.
```

**BBCode (server-side):**
```bbcode
[quote]
[color=#55aa55][size=4][b]Server-Side Friendly[/b][/size][/color]

[b]If you are running a dedicated server, this mod only needs to be installed on the server.[/b]
Players connecting to the server [b]do not need to download or install anything[/b] on their game clients — all changes are synced automatically when they join.
[/quote]
```

For client-side mods, use 🟡 and `[color=#cc9900]` instead.

### Nexus BBCode — Supported Tags

Nexus Mods uses a **limited subset of BBCode**. Only the tags below are reliably supported:

| Tag | Syntax | Notes |
|-----|--------|-------|
| Bold | `[b]text[/b]` | |
| Italic | `[i]text[/i]` | |
| Underline | `[u]text[/u]` | |
| Strikethrough | `[s]text[/s]` | |
| Font colour | `[color=#hex]text[/color]` | Hex format: `#RRGGBB` |
| Font size | `[size=N]text[/size]` | Integer, typically 1–7 |
| Font family | `[font=Name]text[/font]` | |
| Code block | `[code]text[/code]` | Monospaced block |
| Quote block | `[quote]text[/quote]` | |
| Unordered list | `[list][*]item[/list]` | |
| Ordered list | `[list=1][*]item[/list]` | |
| Center align | `[center]text[/center]` | |
| Right align | `[right]text[/right]` | |
| Spoiler | `[spoiler]text[/spoiler]` | Collapsible section |
| URL | `[url=https://...]text[/url]` | |
| Image | `[img]https://...[/img]` | Direct image URL only |

> **Tables are NOT supported** on Nexus. Convert Markdown tables to `[list]` with formatted items.

### Markdown → BBCode Conversion Rules

| Markdown | BBCode |
|----------|--------|
| `# Heading 1` | `[size=6][b]...[/b][/size]` |
| `## Heading 2` | `[size=5][b]...[/b][/size]` |
| `### Heading 3` | `[size=4][b]...[/b][/size]` |
| `**bold**` | `[b]...[/b]` |
| `*italic*` | `[i]...[/i]` |
| `> blockquote` | `[quote]...[/quote]` |
| `- item` / `* item` | `[list][*]item[/list]` |
| `1. item` | `[list=1][*]item[/list]` |
| `[text](url)` | `[url=...]text[/url]` |
| Tables | `[list]` with `[b]key:[/b] value` items |
| 🟢 (server-side badge) | `[color=#55aa55][b]Server-Side Friendly[/b][/color]` |
| 🟡 (client-side badge) | `[color=#cc9900][b]Client-Side Mod[/b][/color]` or `[b]Client + Server Mod[/b]` |

### Nesting Rules

- Tags must be **properly nested** — inner tags close before outer tags: `[size=5][b]...[/b][/size]` ✅
- Do **not** interleave tags: `[b][i]...[/b][/i]` ❌
- `[spoiler]` must be a top-level block — do not nest it inside `[quote]` or `[list]`.

## Anti-patterns

- Do **not** wrap multiple unrelated changes in a single modlet.
- Avoid editing vanilla config files directly — always use xpath patches.
- Do not use spaces in mod folder names or XML `name` attribute values for items/blocks if possible.
