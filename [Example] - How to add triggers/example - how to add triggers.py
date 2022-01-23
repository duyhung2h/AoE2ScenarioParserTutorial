from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *


# File & Folder setup - Declare your scenario directory path
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
input_path = scenario_folder + "ScenarioParser - AddTriggers.aoe2scenario"
output_path = scenario_folder + "ScenarioParser - AddTriggers Parser Result.aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# Start writing your code here:
# a loop iteration: triggerId will start from 0, each iteration increase triggerId by 1, until triggerId reached 9999
for triggerId in range(0, 9999, 1):
    trigger1 = source_trigger_manager.add_trigger("Trigger #" + str(triggerId), enabled=True, looping=False)
    trigger1.new_condition.none()
    trigger1.new_effect.none()

# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)