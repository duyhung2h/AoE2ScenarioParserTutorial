from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *

# File & Folder setup - Declare your scenario directory path
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
input_path = scenario_folder + "ScenarioParser - EditTriggers.aoe2scenario"
output_path = scenario_folder + "ScenarioParser - EditTriggers Parser Result.aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# Start writing your code here:
# copy the first trigger
triggerCopy = source_trigger_manager.copy_trigger(trigger_select=0)
triggerCopy.get_condition(0).timer = 10
triggerCopy.get_effect(0).source_player = 2
triggerCopy.get_effect(1).message = "<RED> An imposter king has arrived!"
triggerCopy.get_effect(2).source_player = 2

# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)
