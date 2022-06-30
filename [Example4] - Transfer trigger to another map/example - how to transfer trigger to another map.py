import sys
import os
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


'''
File & Folder setup
Copy the file name (click on the line and CTRL + C):

ScenarioParser - RemoveTriggers
Tales of Tenebria version 0v16
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
# New scenario so it wouldn't overwrite the old one
output_path = scenario_folder + input_scenario_nanme + \
    " Parser Result" + ".aoe2scenario"
# Transfer scenario to extract triggers into
transfer_path = scenario_folder + input_scenario_nanme + " Transfer.aoe2scenario"
''''''

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)
transfer_scenario = AoE2DEScenario.from_file(transfer_path)


# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager
transfer_trigger_manager = transfer_scenario.trigger_manager

# target_trigger_manager.triggers = []  # Uncomment this in order to wipe all triggers from the map at start
# target_trigger_manager.variables = []  # Uncomment this in order to wipe all variables from the map at start


# put triggers ranging from index position_start to position_end, to position position_transfer in the target file
position_start = 492;
# position_end = source_trigger_manager.triggers.__len__();
position_end = 510;
position_transfer = 505; #Leaving it out (or -1) is placing your triggers at the end

# Mark the start of trigger copying!
triggersNew = []
# transfer_trigger_manager.add_trigger(name="---TRIGGER COPY START-----")
triggersNew.append(source_trigger_manager.triggers[position_start:position_end])
# transfer_trigger_manager.add_trigger(name="---TRIGGER COPY START-----")

# transfer the triggers and variables
# (source_trigger_manager.triggers[position_start:position_end]) to get list of triggers from start to end
transfer_trigger_manager.import_triggers(triggers=triggersNew, index=position_transfer);

# Final step: write a modified scenario class to a new scenario file
transfer_scenario.write_to_file(filename=output_path)