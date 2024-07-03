import os
import json
import shutil
import re

# before running:
# 1. delete "advancements", "loot_tables", and "recipes" directories in "data/minecraft"
# 2. paste the "advancements", "loot_tables", and "recipes" directories from the vanilla jar into "data/minecraft"
# 3. run this script

def main():
	# advancements
	categories = os.listdir("data/minecraft/advancements")
	for category in categories:
		print(f"Invalidating advancements for {category}")
		for category2 in os.listdir(f"data/minecraft/advancements/{category}"):
			if os.path.isfile(f"data/minecraft/advancements/{category}/{category2}"):
				override_advancement(f"data/minecraft/advancements/{category}/{category2}")
			else:
				for advancement in os.listdir(f"data/minecraft/advancements/{category}/{category2}"):
					override_advancement(f"data/minecraft/advancements/{category}/{category2}/{advancement}")

	# loot_tables
	def override_loot_tables_recursivel(path):
		if os.path.isfile(path):
			override_loot_table(path)
		else:
			for sub_loot_table in os.listdir(path):
				override_loot_tables_recursivel(f"{path}/{sub_loot_table}")
	categories = os.listdir("data/minecraft/loot_tables")
	for category in categories:
		print(f"Overriding loot tables for {category}")
		override_loot_tables_recursivel(f"data/minecraft/loot_tables/{category}")

	# recipes
	print("Overriding recipes")
	whitelist = [
		r"armor_dye.json",
		r"banner_duplicate\.json",
		r"book_cloning\.json",
		r"firework_rocket\.json",
		r"firework_star\.json",
		r"firework_star_fade\.json",
		r"map_cloning\.json",
		r"map_extending\.json",
		r"shield_decoration\.json",
		r"[^_]+_armor_trim_smithing_template\.json",
	]
	recipe = os.listdir("data/minecraft/recipes")
	for recipe in recipe:
		if os.path.isfile(f"data/minecraft/recipes/{recipe}"):
			if any(re.match(pattern, recipe) for pattern in whitelist):
				print(f"Skipping {recipe}")
			else:
				override_recipe(f"data/minecraft/recipes/{recipe}")
		else:
			raise Exception("Recipe is a directory: " + recipe)

def override_advancement(path):
	with open(path, "w") as file:
		data = {
			"criteria": {
				"impossible": {
					"trigger": "minecraft:impossible"
				}
			}
		}
		file.write(json.dumps(data, indent=4))

def override_loot_table(path):
	with open(path, "w") as file:
		data = {
			"type": "minecraft:empty"
		}
		file.write(json.dumps(data, indent=4))

def override_recipe(path):
	with open(path, "w") as file:
		data = {
			"type": "minecraft:stonecutting",
			"ingredient": { "item": "minecraft:structure_void" },
			"result": {
				"id": "minecraft:structure_void",
			},
			"count": 1
		}
		file.write(json.dumps(data, indent=4))

if __name__ == "__main__":
	main()