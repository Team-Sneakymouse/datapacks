# datapacks
Vanilla datapacks for our Minecraft servers

## dvz
Datapack to support DvZ gameplay and roleplay mechanics
Intended to be used with a **disabled** vanilla resource pack
- Re-enables loot tables for:
	- Scaffolding
- Re-enabled crafting recipes for:
	- Book cloning
	- Banner duplication
	- Shield customization
	- Firework stars and rockets
- Adds custom damage types:
	- `dvz:physical_slash`, `dvz:physical_blunt`, `dvz:physical:pierce`
	- `dvz:elemental_light`, `dvz:elemental:earth`, `dvz:elemental_ice`, `dvz:elemental_dark`, `dvz:elemental_arcane`, `dvz:elemental_fire`
- Adds tags:
	- damage types:
		- `#dvz:is_physical` (also includes the damage type `minecraft:player_attack`)
		- `#dvz:is_elemental`

## plots
Custom world generator for a plot world
- very (but not literally) flat world surface
- no caves
- no ores (also no dirt, gravel, sand, and stone patches)
- world layers
  - bedrock y=-64 to y=-60
  - deepslate y=-63 to y=5
  - stone y=0 to y=60
  - dirt and grass block y=50 to y=62
- populated with sparse oak trees, grass, and flowers
