import sys
import os
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from component.unit_manager import SPTUnitManager


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# File & Folder setup
try:
    scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"
    source_scenario = AoE2DEScenario.from_file(
        scenario_folder + "ScenarioParser - ChangeMapSize.aoe2scenario")
except:
    scenario_folder = resource_path("")
    print("\ncannot find main scenario folder. redirect to base dir: " + scenario_folder)

# Source scenario to work with
input_path = scenario_folder + "ScenarioParser - ChangeMapSize.aoe2scenario"
# input_path = scenario_folder + "Tales of Tenebria version 0v11 S.aoe2scenario"
# Transfer scenario to extract triggers into
output_path = scenario_folder + \
              "ScenarioParser - ChangeMapSize Parser Result.aoe2scenario"
output_path2 = scenario_folder + \
               "ScenarioParser - ChangeMapSize Parser Result2.aoe2scenario"
# output_path2 = scenario_folder + \
# "Tales of Tenebria version 0v11 Parser Result2.aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare map manager to work with map
source_map_manager = source_scenario.map_manager

old_map_size = source_scenario.map_manager.map_size
print("Old map size: " + str(old_map_size))
correctMapSize = False
while not correctMapSize:
    try:
        new_map_size = int(input("Enter new map size (16-480): "))
        if new_map_size < 16 or new_map_size > 480:
            print("Map size must be in the range of (16-480)!")
        else:
            correctMapSize = True
    except:
        print("Map size must be of integer type!")
        correctMapSize = False
direction = "W"
print("        North")
print("          ^")
print("          |")
print("West <- Center -> East")
print("          |")
print("          V")
print("        South")
correctDirection = False
while not correctDirection:
    try:
        direction = input("Choose direction to expand map into: (N|S|E|W|C): ")
        if direction.upper() == "N" or direction.upper() == "S" or direction.upper() == "E" or direction.upper() == "W":
            correctDirection = True
        else:
            print("Direction must be (N|S|E|W|C)!")
    except:
        print("Direction must be of string type!")
        correctDirection = False

# Iteration 1------------------------------------------------------------------------------
# manager for iteration 1
spt_unit_manager = SPTUnitManager(
    scenario=source_scenario, direction=direction, old_map_size=old_map_size, new_map_size=new_map_size)

# move unit in iteration 1
spt_unit_manager.move_unit()

# move trigger in iteration 1
spt_unit_manager.move_triggers()

# Extend map iteration 1
spt_unit_manager.extend_map_iteration1()

# Commit initial terrain changes, then reverse that again
source_scenario = spt_unit_manager.scenario
source_scenario.write_to_file(output_path)

# Iteration 2 -----------------------------------------------------------------------------------
output_scenario = AoE2DEScenario.from_file(output_path)

# manager for iteration 2
spt_unit_manager2 = SPTUnitManager(
    scenario=output_scenario, direction=direction, old_map_size=old_map_size, new_map_size=new_map_size)

# Extend map iteration 2
spt_unit_manager2.extend_map_iteration2()

# Final step: write a modified scenario class to a new scenario file
output_scenario = spt_unit_manager2.scenario
# output_scenario.trigger_manager.triggers = []
output_scenario.write_to_file(output_path2)

print("final")
print('\033[91m' + "TEST YOUR MAP BY GOING TO MAIN MENU -> TEST BEFORE USING YOUR NEWLY CREATED MAP." + '\033[0m')
print(
    '\033[91m' + "REMOVE ANY UNIT THAT CLIPPED THROUGH MAP BORDERS DUE TO THEIR SIZES, IF THERE'S ANY, FOR THEM COULD POTENTIALLY CRASH THE MAP." + '\033[0m')

print(
    '\033[91m' + "Don't leave any player to have 0 unit in the map if the newly generated map is small - Scenario will crash if the map attempted to generate a `Town Center` for those said players, that could clips through map's borders." + '\033[0m')