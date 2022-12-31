import os
import sys
import random

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
12warlords 0v1v8
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

originalTerrains = source_scenario.map_manager.terrain

'''
Find water bridge and change it to water shallow
'''

# Allowed terrain
allowed_terrains = [28, 1]

# Terrain to randomly change into
random_terrains_added_in = [1, 4, 54, 59, 90, 58]

for terrain in originalTerrains:
    for allowed_terrain in allowed_terrains:
        if terrain.terrain_id == allowed_terrain:
            print("terrain.terrain_id == allowed_terrain: " + str(terrain.terrain_id) + ", layer: " + str(terrain.layer))
            terrain.terrain_id = 1
            terrain.layer = random.choice(random_terrains_added_in)

'''
!!! HOW THIS WORKS: (This is a script that will turn all river shores to be gravels)
Scan all water in the map, after identify a water tile it will scan adjacent tiles.
If the adjacent tiles happens to be water, ignore it. Otherwise, turn it into gravel.
'''

# Allowed terrain
allowed_terrains = [22, 23, 1, 4, 15, 28, 57, 58, 95, 96, 97, 98, 99]

# Terrain to randomly change into
random_terrains_added_in = [70, 108, 102]

source_scenario.map_manager.terrain = originalTerrains

# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)
