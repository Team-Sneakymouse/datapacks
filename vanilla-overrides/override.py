import os
import json
import shutil
import re

# before running:
# 1. delete "advancement", "loot_table", and "recipe" directories in "data/minecraft"
# 2. paste the "advancement", "loot_table", and "recipe" directories from the vanilla jar into "data/minecraft"
# 3. run this script
def process_advancements(directory):
	for entry in os.listdir(directory):
		path = os.path.join(directory, entry)
		if os.path.isfile(path):
			override_advancement(path)
		elif os.path.isdir(path):
			print(f"Entering directory: {path}")
			process_advancements(path)

def process_loot_tables(directory):
	for entry in os.listdir(directory):
		path = os.path.join(directory, entry)
		if os.path.isfile(path):
			override_loot_table(path)
		elif os.path.isdir(path):
			print(f"Entering directory: {path}")
			process_loot_tables(path)


def main():
	# advancements
	process_advancements("data/minecraft/advancement")

	# loot_tables
	process_loot_tables("data/minecraft/loot_table")

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
	recipe = os.listdir("data/minecraft/recipe")
	for recipe in recipe:
		if os.path.isfile(f"data/minecraft/recipe/{recipe}"):
			if any(re.match(pattern, recipe) for pattern in whitelist):
				print(f"Skipping {recipe}")
			else:
				override_recipe(f"data/minecraft/recipe/{recipe}")
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
			"ingredient": "minecraft:structure_void",
			"result": {
                "id": "minecraft:structure_void",
                "count": 1
            }
		}
		file.write(json.dumps(data, indent=4))

if __name__ == "__main__":
	main()