# Phase 1: XML Modlets

**[Back to Modding Guide](modding_guide.md)** | **Next: [Phase 2 — Harmony Mods](phase2_harmony_mods.md)**

XML modlets are the simplest and most common form of 7 Days to Die modding. They use XPath expressions to patch the game's vanilla XML configuration files **without replacing them**. No compilation, no Unity project, no C# knowledge required.

---

## How XML Patching Works

The game loads all vanilla XML from `Data\Config\`, then iterates through every mod in `Mods\` (alphabetically) and applies their `Config\` XML patches on top. Your mod files **do not replace** vanilla files — they contain XPath operations that modify the in-memory XML tree.

### XPath Operations

| Operation | Description | Example |
| --- | --- | --- |
| `set` | Change an existing value | `<set xpath=".../@value">50</set>` |
| `append` | Add child nodes at the end of a parent | `<append xpath="/items"><item name="...">...</item></append>` |
| `insertAfter` | Insert nodes after a specific sibling | `<insertAfter xpath="/items/item[@name='gunPistol']">...</insertAfter>` |
| `insertBefore` | Insert nodes before a specific sibling | `<insertBefore xpath="...">...</insertBefore>` |
| `remove` | Delete a node | `<remove xpath="/items/item[@name='myItem']"/>` |
| `removeattribute` | Remove an attribute from a node | `<removeattribute xpath="..." name="count"/>` |
| `setattribute` | Set/add an attribute on a node | `<setattribute xpath="..." name="count" value="5"/>` |

### Patch File Structure

Every XML patch file must be wrapped in a `<configs>` root element:

```xml
<!-- Config/items.xml in your mod folder -->
<configs>
  <!-- Each operation is a direct child of <configs> -->
  <set xpath="/items/item[@name='meleeToolPickaxeT1Iron']/property[@name='DamageEntity']/@value">25</set>

  <append xpath="/items">
    <item name="myCustomItem">
      <property name="Extends" value="meleeToolPickaxeT1Iron"/>
      <property name="CustomIcon" value="myCustomItem"/>
    </item>
  </append>
</configs>
```

### XPath Syntax Quick Reference

| Pattern | Selects |
| --- | --- |
| `/items` | Root `<items>` element |
| `/items/item[@name='gunPistol']` | `<item>` with `name="gunPistol"` |
| `.../property[@name='DamageEntity']/@value` | The `value` attribute of a `property` node |
| `.../effect_group` | All `<effect_group>` children |
| `.../effect_group[@name='Base Effects']` | A specific named `effect_group` |
| `//item[@name='gunPistol']` | `item` anywhere in the tree (slower, use sparingly) |

### The `Extends` System

Items, blocks, and entities support inheritance via the `Extends` property:

```xml
<item name="myGun">
  <property name="Extends" value="gunPistol"/>
  <!-- Only override what you want to change -->
  <property name="DamageEntity" value="100"/>
</item>
```

Key rules for `Extends`:

- The child inherits **all** properties from the parent.
- Properties explicitly set on the child override the parent.
- `Extends` copies upgrade/downgrade paths in blocks.
- The `CreativeMode` property is **not inherited** — children remain visible by default.
- Extended items do **not** inherit auto-calculated weight — only items with actual recipes have it.
- If a block uses `Extends` but has its own `destroy` event, it uses its own; otherwise it inherits the parent's.

---

## Modlet Folder Layout

```text
Mods\
  MyModName\
    ModInfo.xml              # Required
    Config\
      items.xml              # Patches for Data\Config\items.xml
      blocks.xml             # Patches for Data\Config\blocks.xml
      recipes.xml            # Patches for Data\Config\recipes.xml
      Localization.txt       # Appended to vanilla Localization.txt
      XUi\
        windows.xml          # Patches for Data\Config\XUi\windows.xml
```

Your `Config\` folder mirrors the game's `Data\Config\` structure. The file names must match exactly.

---

## Localization

`Localization.txt` is a **tab-separated** file with this header:

```text
Key,File,Type,UsedInMainMenu,NoTranslate,english,Context / Alternate Text,german,spanish,french,italian,japanese,koreana,polish,brazilian,russian,turkish,schinese,tchinese
```

| Column | Purpose |
| --- | --- |
| `Key` | Unique string key referenced by XML configs (e.g., item descriptions) |
| `File` | Source file category: `blocks`, `items`, `buffs`, etc. |
| `Type` | Entry type: `Block`, `Item`, `Buff`, `Quest`, etc. |
| `UsedInMainMenu` | Leave empty unless shown in main menu |
| `NoTranslate` | `x` if the string should not be translated |
| `english` | The English text |
| Remaining columns | Translations (can be left empty) |

Your mod's `Localization.txt` is **appended** to the vanilla file. Add only your new entries:

```text
myCustomItem,items,Item,,,"My Custom Pickaxe","A powerful mining tool",,,,,,,,,,,
myCustomItemDesc,items,Item,,,"A legendary pickaxe forged in fire.",,,,,,,,,,,,
```

---

## XML Configuration Files Reference

All files are located in `Data\Config\` relative to the game installation root. All are valid targets for modlet XPath patches.

### Core Game Data Files

| File | Purpose | Typical Modlet Uses |
| --- | --- | --- |
| `items.xml` | **All holdable items**: weapons, tools, consumables, resources, ammo, armor, clothing. Defines stats (damage, range, magazine size, degradation), visual properties, action types, sound references, passive effects. | Change weapon damage, add new items via `Extends`, tweak stack sizes, modify repair costs, add new effect groups |
| `blocks.xml` | **All placeable blocks**: terrain, building materials, workstations, doors, traps, containers, plants, trees, electrical components. Defines shapes, textures, materials, hit points, upgrade/downgrade paths. | Add new blocks/workstations, change block HP, modify upgrade paths, add new traps, change harvest yields |
| `recipes.xml` | **Crafting recipes**: ingredients, quantities, crafting area (hand, workbench, forge, etc.), unlock requirements, craft time, output count. | Add recipes for new items, change ingredient costs, add new crafting stations to existing recipes |
| `loot.xml` | **Loot system**: loot containers (desks, cars, safes, zombies), loot groups (probabilistic item pools), quality scaling, quest reward loot. | Change loot drop rates, add items to loot pools, create new loot containers, modify scrap returns |
| `entityclasses.xml` | **Entity classes**: zombies, animals, NPCs, traders. Defines health, speed, damage, AI tasks, loot on death, appearance models, ragdoll physics. | Add new zombie types, change entity stats, create boss entities, modify trader protected zones |
| `entitygroups.xml` | **Entity spawn groups**: named collections of entities used by gamestages, spawning rules, and screamer hordes. Maps group names to entity lists with probability weights. | Add new entities to existing groups, create custom spawn groups for biomes or horde nights |
| `buffs.xml` | **Buffs and debuffs**: status effects, passive effects, timed effects, triggered effects. Uses NCalc expressions for dynamic calculations. Contains effect requirements, durations, stacking rules, and CV (current value) modifications. | Add new buffs/debuffs, change effect durations, create custom mechanics via trigger/requirement system |
| `progression.xml` | **Skill tree**: attributes (Perception, Strength, etc.), perks, crafting skills, level requirements, stat bonuses per level. Uses NCalc expressions for scaling formulas. | Add new perks, change unlock requirements, modify stat bonuses, restructure the perk tree |
| `gamestages.xml` | **Horde night waves**: defines what entities spawn at each gamestage, wave timing, counts, and difficulty scaling. Also controls wandering hordes. | Change horde composition, add boss waves, modify difficulty curve, create custom gamestage groups |
| `spawning.xml` | **Biome/zone spawning**: rules for ambient spawn groups in each biome (forest, desert, snow, wasteland, burnt). Day vs night, density, respawn timers. | Change biome enemy density, add entities to biome spawns, modify day/night spawn behavior |
| `traders.xml` | **Trader system**: trader types (Jen, Bob, Hugh, Joel, Rekt), inventory tiers, item pools per tier, restock timers, quest tier offerings, protected zone size. | Add items to trader pools, change prices, modify restock rates, add new trader tiers |
| `vehicles.xml` | **Vehicles**: bicycle, minibike, motorcycle, 4x4 truck, gyrocopter. Properties: speed, fuel capacity, storage, handling, crafting requirements. | Change vehicle speed/storage, modify fuel consumption, alter crafting costs |

### Items, Modifiers, and Quality

| File | Purpose | Typical Modlet Uses |
| --- | --- | --- |
| `item_modifiers.xml` | **Weapon/tool mods**: barrel mods, scope mods, grip mods, dyes, cosmetic mods. Defines stat modifications applied when installed. | Add new weapon mods, change mod bonuses, add mod slots to items |
| `qualityinfo.xml` | **Quality tiers**: defines stat scaling per quality level (1–6). Controls how damage, durability, and secondary stats scale with quality. | Change quality scaling curves, rebalance tier progression |

### World Configuration

| File | Purpose | Typical Modlet Uses |
| --- | --- | --- |
| `biomes.xml` | **Biome definitions**: surface blocks, sub-surface layers, decoration placement (trees, rocks, grass), prefab spawning rules per biome. | Change biome terrain composition, modify decoration density, add custom biome features |
| `rwgmixer.xml` | **Random World Generation**: city sizes, town spacing, road types, POI placement rules, biome distribution, wilderness rules. | Modify world generation parameters, change city density, POI placement rules |
| `worldglobal.xml` | **Global world settings**: day/night cycle duration, ambient light, moon phases, loot respawn time, zombie feralness settings, blood moon frequency. | Change day length, modify blood moon frequency, adjust global loot respawn |
| `weathersurvival.xml` | **Weather and survival**: temperature effects, wetness, hypothermia/hyperthermia thresholds, weather impact on stamina. | Adjust temperature thresholds, change weather severity effects |

### AI and Entity Behavior

| File | Purpose | Typical Modlet Uses |
| --- | --- | --- |
| `utilityai.xml` | **AI behavior trees**: utility scoring for AI decisions (attack, flee, wander, investigate). Defines how entities prioritize actions. | Modify zombie behavior, change AI aggression, create custom AI routines |
| `archetypes.xml` | **Entity archetypes**: base templates that `entityclasses.xml` entries can inherit from. Defines shared property sets. | Create new archetypes for custom entity families |

### NPC and Quest System

| File | Purpose | Typical Modlet Uses |
| --- | --- | --- |
| `quests.xml` | **Quest definitions**: quest types (clear, fetch, treasure, buried supply), objectives, rewards, difficulty tiers, POI requirements. | Add new quests, modify rewards, create quest chains |
| `challenges.xml` | **Challenges**: in-game challenge objectives and rewards (kill X zombies, craft Y items, etc.). | Add new challenges, modify challenge requirements |
| `dialogs.xml` | **NPC dialogs**: trader conversation trees, dialog options, response conditions, quest offerings. | Add dialog options, create new trader conversations |
| `npc.xml` | **NPC configuration**: NPC-specific settings, hireable NPC properties. | Modify NPC settings |

### Sounds and Music

| File | Purpose | Typical Modlet Uses |
| --- | --- | --- |
| `sounds.xml` | **Sound events**: maps action names to audio files and playback parameters. Every gunshot, footstep, UI click, zombie growl is defined here. | Change weapon sounds, add sounds for new items, modify ambient sounds |
| `music.xml` | **Music events**: maps game states/biomes to music tracks. Controls combat music, exploration music, horde night music. | Change music assignments, add custom music tracks |
| `subtitles.xml` | **Subtitles**: subtitle text for audio events (for accessibility). | Add subtitles for new sounds |

### Materials and Physics

| File | Purpose | Typical Modlet Uses |
| --- | --- | --- |
| `materials.xml` | **Block materials**: hardness, damage resistance by type (bullet, melee, explosion), harvest tool, particle effects on hit, repair material. | Change block resistance, add new material types, modify harvest drops |
| `physicsbodies.xml` | **Ragdoll physics**: physics body definitions for entities (limb mass, joint limits). | Modify ragdoll behavior |
| `shapes.xml` | **Block shapes**: 3D shape definitions that blocks can use. Maps shape names to mesh data. | Reference only — new shapes require Unity AssetBundles (Phase 3) |

### UI Configuration

| File | Purpose | Typical Modlet Uses |
| --- | --- | --- |
| `XUi\windows.xml` | **In-game HUD windows**: inventory, crafting, map, toolbelt, health bars, loot containers, vehicle UI, compass. | Rearrange UI elements, add new UI panels, modify existing windows |
| `XUi\controls.xml` | **Reusable UI controls**: buttons, item slots, labels, progress bars, icons — building blocks used by `windows.xml`. | Modify control appearance, add custom controls |
| `XUi\styles.xml` | **UI styles**: colors, fonts, sizes, paddings, anchors. | Restyle the UI, change color schemes |
| `XUi\xui.xml` | **XUi root**: binds window names to their controller classes and defines the load list. | Register new windows, change controller bindings |
| `XUi_Menu\windows.xml` | **Main menu UI**: new game, continue, multiplayer, settings screens. | Modify main menu layout |
| `XUi_Menu\controls.xml` | Main menu controls | Modify menu controls |
| `XUi_Menu\styles.xml` | Main menu styles | Restyle main menu |
| `XUi_Menu\xui.xml` | Main menu root | Register menu windows |
| `XUi_Common\controls.xml` | **Shared UI controls**: common components used by both HUD and Menu. | Modify shared elements |
| `XUi_Common\styles.xml` | Shared styles | Modify shared styles |

### Display and Presentation

| File | Purpose | Typical Modlet Uses |
| --- | --- | --- |
| `ui_display.xml` | **UI display labels**: maps property names to display strings in the item inspection UI (e.g., "Entity Damage", "Block Damage"). | Add display labels for custom properties |
| `painting.xml` | **Block painting**: available paint textures for the painting system. | Add custom paint textures |
| `nav_objects.xml` | **Navigation icons**: minimap and compass icons for tracked objects (traders, quests, allies). | Add custom map markers |
| `loadingscreen.xml` | **Loading screen tips**: text displayed on loading screens. | Add custom tips, change existing tips |

### Events and Triggers

| File | Purpose | Typical Modlet Uses |
| --- | --- | --- |
| `events.xml` | **Event triggers**: defines what events the game can fire (entity death, block destroyed, item crafted). | Reference for buff/quest triggers |
| `gameevents.xml` | **Event responses**: what happens when events fire (spawn entity, play sound, give buff). | Create custom event-driven mechanics |

### Integrations

| File | Purpose | Typical Modlet Uses |
| --- | --- | --- |
| `twitch.xml` | **Twitch integration**: actions available for Twitch viewers to trigger in-game. | Add custom Twitch actions |
| `twitch_events.xml` | **Twitch events**: specific Twitch event definitions and their effects. | Customize Twitch interactions |
| `videos.xml` | **Video playback**: references to video files played by the game (intro, cutscenes). | Change intro video |
| `dmscontent.xml` | **Diersville content**: static content for the Diersville map. | Modify map-specific spawns |

### Supplementary Data Files

| File | Format | Purpose |
| --- | --- | --- |
| `Localization.txt` | TSV | All in-game strings — item names, descriptions, UI labels, buff names, quest text. Key → language columns. Mods append to this. |
| `BlockUpdates.csv` | CSV | Block upgrade/downgrade transition table (material → upgraded material). |
| `blockplaceholders.xml` | XML | Block placeholder substitution rules for prefab loading. |
| `OversizedConversionTargets.txt` | Text | List of oversized blocks that get auto-converted. |
| `Stealth.txt` | Text | Stealth system parameter documentation. |
| `XML.txt` | Text | Developer notes on the XML system, block naming conventions, property documentation. **Read this file** — it contains valuable property explanations. |

---

## Common Modlet Patterns

### Pattern 1: Modify a Property Value

```xml
<configs>
  <set xpath="/items/item[@name='gunPistol']/property[@name='DamageEntity']/@value">50</set>
</configs>
```

### Pattern 2: Add a New Item (via Extends)

```xml
<configs>
  <append xpath="/items">
    <item name="gunPistolCustom">
      <property name="Extends" value="gunPistol"/>
      <property name="DamageEntity" value="100"/>
      <property name="DamageBlock" value="20"/>
      <property name="CustomIcon" value="gunPistolCustom"/>
    </item>
  </append>
</configs>
```

### Pattern 3: Add a Recipe

```xml
<configs>
  <append xpath="/recipes">
    <recipe name="gunPistolCustom" count="1" craft_area="workbench" craft_time="60">
      <ingredient name="resourceForgedIron" count="10"/>
      <ingredient name="resourceMechanicalParts" count="5"/>
      <ingredient name="gunPistolParts" count="4"/>
    </recipe>
  </append>
</configs>
```

### Pattern 4: Add Item to Loot Group

```xml
<configs>
  <append xpath="/lootcontainers/lootgroup[@name='groupWeapons']">
    <item name="gunPistolCustom" count="1" prob="0.05" quality_template="QLTemplateT2"/>
  </append>
</configs>
```

### Pattern 5: Modify XUi Window

```xml
<configs>
  <set xpath="/windows/window[@name='windowInventory']/rect[@name='headerPanel']/@height">40</set>
  <append xpath="/windows/window[@name='windowInventory']">
    <label text="Custom Mod Active" color="255,200,0" />
  </append>
</configs>
```

### Pattern 6: Add Localization Entry

In `Config/Localization.txt` (tab-separated, appended to vanilla):

```text
gunPistolCustom,items,Item,,,"Custom Pistol",,,,,,,,,,,,
gunPistolCustomDesc,items,Item,,,"A specially modified pistol with enhanced damage.",,,,,,,,,,,,
```

---

## Debugging XML Modlets

1. **Check `output_log.txt`** — the game logs all XML parsing errors with file name and line number.
2. **Common XPath errors**:
   - Typo in item/block name — XPath silently matches nothing.
   - Wrong nesting level — `property` directly under `items` instead of under `item`.
   - Missing `@value` — `set` needs to target an attribute, not a node.
3. **Use `remove` carefully** — removing a node that other nodes reference can cascade errors.
4. **Load order matters** — if another mod removes a node before your mod patches it, your patch fails silently.
5. **Validate XPath** — test complex XPath expressions against the vanilla XML before deploying.

---

## Block and Item Naming Conventions

From the game's `XML.txt` developer notes:

**Block naming** follows the pattern: `[material/texture] [shape] [extra properties]`

| Shape Code | Block Shape |
| --- | --- |
| `block` | Full 1m cube |
| `half` | Half block |
| `quarter` | Quarter block |
| `eighth` | Eighth block |
| `pyramid` | Pyramid shape |
| `ramp` | 45-degree triangle |
| `stairs25` | 25cm steps |
| `stairs50` | 50cm steps |
| `pole` | Pole shape |
| `plate` | Plate (thin flat) |
| `CTRPlate` | Centered plate |
| `wedge` | 60-degree wedge |
| `CNRFull` | Corner (full base, for outside roof) |
| `CNRRamp` | Corner (triangle base) |
| `CNRInside` | Concave corner (for roofs) |
| `CNRRound` | Rounded corner |
| `gable` | Small triangle tip (roofs) |
| `sheet` | One-sided billboard |
| `CTRSheet` | Centered sheet (windows, glass panes) |
| `TRN` | Terrain shape |

Example names: `awningRedBlock`, `rebarFrameRamp`, `rConcreteCNRFull`, `rConcretePlate`

**`CreativeMode` property values**: `Player`, `Dev`, `None`, `Test`

- `Player` — visible in player creative menu
- `Dev` — visible only when dev button is active
- `None` — never displayed (master blocks)
- `Test` — only in Unity editor with dev button

---

## NCalc Expressions in buffs.xml and progression.xml

The game uses **NCalc** (math expression evaluator) for dynamic calculations in buffs and progression. Common variables:

| Variable | Available In | Meaning |
| --- | --- | --- |
| `@_level` | progression.xml | Current perk level |
| `@_maxLevel` | progression.xml | Max perk level |
| `{EntityDamage}` | buffs.xml | Current entity damage value |
| `{BlockDamage}` | buffs.xml | Current block damage value |
| `{HealthCurrent}` | buffs.xml | Current health |
| `{HealthMax}` | buffs.xml | Max health |
| `{StaminaCurrent}` | buffs.xml | Current stamina |
| `{FoodAmount}` | buffs.xml | Current food level |
| `{WaterAmount}` | buffs.xml | Current water level |

Example expression in `progression.xml`:

```xml
<effect_group>
  <passive_effect name="EntityDamage" operation="perc_add" value=".1,.5" level="1,5"/>
</effect_group>
```

---

*[Back to Modding Guide](modding_guide.md)* | *Next: [Phase 2 — Harmony Mods](phase2_harmony_mods.md)*
