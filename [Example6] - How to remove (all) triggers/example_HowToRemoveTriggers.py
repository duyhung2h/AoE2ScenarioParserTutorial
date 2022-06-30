import sys
import os
import time
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


'''
File & Folder setup
Copy the file name (click on the line and CTRL + C):

ScenarioParser - RemoveTriggers
Tales of Tenebria version 0v18
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

# Uncomment this in order to wipe all triggers from the map at start
saved_triggers = source_scenario.trigger_manager.triggers
# target_trigger_manager.variables = []  # Uncomment this in order to wipe all variables from the map at start

'''
mark triggers ranging from index "position_start" to "position_end",

to remove triggers designated from position "position_start" to "position_end".
'''
position_start = len(saved_triggers) - 600
position_end = len(saved_triggers) - 0
# len(source_trigger_manager); #or a custom position


# remove triggers
# target_trigger_manager.import_triggers(source_trigger_manager.triggers[position_start:position_end], -1)
source_trigger_manager.triggers = saved_triggers[30:position_end]
# source_trigger_manager.triggers = saved_triggers[30:90]
# source_trigger_manager.triggers = saved_triggers[90:120]
# source_trigger_manager.triggers = saved_triggers[0:40] + saved_triggers[500:600] # co trigger nao do lam crash khi bo no di, giua 200 va 320
# giua 440 va 450: co trigger count team members: crash game in 40 seconds
# giua 450 va 500: co trigger(s) lam lag game
# source_trigger_manager.triggers = source_trigger_manager.triggers + saved_triggers[400:position_end-17]
source_trigger_manager.add_trigger("99999999999999999999999999999999999999999")
# source_trigger_manager.triggers = source_trigger_manager.triggers + saved_triggers[1000:position_end] # start tung la 400

# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)
