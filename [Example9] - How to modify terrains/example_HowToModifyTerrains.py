import os
import random
import sys

from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


'''
File & Folder setup
Copy the file name (click on the line and CTRL + C):

12warlords modified
12warlords 0v1v31

'''

input_scenario_nanme = input(
    'Please enter the scenario name (spare the .aoe2scenario extension): ')
try:
    scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"
    source_scenario = AoE2DEScenario.from_file(
        scenario_folder + input_scenario_nanme + ".aoe2scenario")
except FileNotFoundError:
    scenario_folder = resource_path("")
    print("\ncannot find main scenario folder. redirect to base dir: " + scenario_folder)

# Source scenario to work with
input_path = scenario_folder + input_scenario_nanme + ".aoe2scenario"
# Transfer scenario to extract triggers into
output_path = scenario_folder + input_scenario_nanme + \
              " Parser Result" + ".aoe2scenario"

''''''

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

''''''

# get all the terrains tiles (compiled in a list) in the map
originalTerrains = source_scenario.map_manager.terrain

'''
Find water bridge and change it to water shallow
'''

# # Allowed terrain
# allowed_terrains = [28, 1]
#
# # Terrain to randomly layer on
# random_terrains_layered_on = [1, 54, 59, 58, 23]
#
# for terrain in originalTerrains:
#     for allowed_terrain in allowed_terrains:
#         if terrain.terrain_id == allowed_terrain:
#             print("terrain.terrain_id == allowed_terrain: " + str(terrain.terrain_id) + ", layer: " + str(terrain.layer))
#             if terrain.layer > -1:
#                 newLayer = terrain.layer
#                 terrain.terrain_id = 1
#                 terrain.layer = newLayer
#             else:
#                 terrain.terrain_id = 1
#                 print("change layer")
#                 terrain.layer = random.choice(random_terrains_layered_on)

'''
Find water shallow and change it to water bridge
'''

# Allowed terrain
allowed_terrains = [28, 1]

# Terrain to randomly layer on
random_terrains_layered_on = [1, 54, 59, 58, 23]

for terrain in originalTerrains:
    for allowed_terrain in allowed_terrains:
        if terrain.terrain_id == allowed_terrain:
            print("terrain.terrain_id == allowed_terrain: " + str(terrain.terrain_id) + ", layer: " + str(terrain.layer))
            if terrain.layer > -1:
                newLayer = terrain.layer
                terrain.terrain_id = 28
                terrain.layer = newLayer
            else:
                terrain.terrain_id = 28
                print("change layer")
                terrain.layer = random.choice(random_terrains_layered_on)

# '''
# Find mud (unlayered) and change it to grass + mud layered in
# '''
#
# # Allowed terrain
# allowed_terrains = [76, 6, 7]
#
# # Terrain to randomly layer on
# random_terrains_core = [12, 0, 9, 100]
#
# # Terrain to randomly change into
# random_terrains_layered_on = [76, 77]
#
# for terrain in originalTerrains:
#     for allowed_terrain in allowed_terrains:
#         if terrain.terrain_id == allowed_terrain and terrain.layer == -1:
#             print("terrain.terrain_id == allowed_terrain: " + str(terrain.terrain_id) + ", layer: " + str(terrain.layer))
#             terrain.terrain_id = random.choice(random_terrains_core)
#             terrain.layer = random.choice(random_terrains_layered_on)


# '''
# Find water (1) and change it to ice (26)
# '''
#
# # Allowed terrain
# allowed_terrains = [1, 28, 26]
#
# # Terrain to randomly layer on
# random_terrains_layered_on = [1]
#
# for terrain in originalTerrains:
#     for allowed_terrain in allowed_terrains:
#         if terrain.terrain_id == allowed_terrain:
#             print(
#                 "terrain.terrain_id == allowed_terrain: " + str(terrain.terrain_id) + ", layer: " + str(terrain.layer))
#             terrain.terrain_id = 26
#             terrain.layer = random.choice(random_terrains_layered_on)

# '''
# Find land and layer snow (32, 73, 74) on them
# '''
#
# # Allowed terrain (ALL LANDS TERRAIN)
# allowed_terrains = [0, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 24, 25, 26, 27, 29, 30, 31, 32, 36,
#                     40, 41, 42, 45, 46, 48, 49, 50, 56, 60, 63, 64, 65, 66, 67, 70, 71, 72, 75, 76, 77, 78, 83, 88, 89,
#                     100, 101, 102, 104, 105, 106, 110, 111, 112]
#
# # Terrain to randomly layer on
# random_terrains_layered_on = [32, 73, 74]
#
# for terrain in originalTerrains:
#     for allowed_terrain in allowed_terrains:
#         if terrain.terrain_id == allowed_terrain:
#             print(
#                 "terrain.terrain_id == allowed_terrain: " + str(terrain.terrain_id) + ", layer: " + str(terrain.layer))
#             terrain.layer = random.choice(random_terrains_layered_on)


# '''
# !!! HOW THIS WORKS: (This is a script that will turn all river shores to be gravels)
# Scan all water in the map, after identify a water tile it will scan adjacent tiles.
# If the adjacent tiles happens to be water, ignore it. Otherwise, turn it into gravel.
# '''
#
# # Allowed terrain
# allowed_terrains = [22, 23, 1, 4, 15, 28, 57, 58, 95, 96, 97, 98, 99]
#
# # Terrain to randomly layer on
# random_terrains_added_in = [70, 108, 102]

source_scenario.map_manager.terrain = originalTerrains

# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)
