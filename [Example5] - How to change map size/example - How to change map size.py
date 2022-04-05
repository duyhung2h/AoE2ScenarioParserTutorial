import sys
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from component.unit_manager import SPTUnitManager

# File & Folder setup
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
input_path = scenario_folder + "ScenarioParser - ChangeMapSize.aoe2scenario"
# Transfer scenario to extract triggers into
output_path = scenario_folder + \
    "ScenarioParser - ChangeMapSize Parser Result.aoe2scenario"
output_path2 = scenario_folder + \
    "ScenarioParser - ChangeMapSize Parser Result2.aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare map manager to work with map
source_map_manager = source_scenario.map_manager

old_map_size = source_scenario.map_manager.map_size
print("Old map size: " + str(old_map_size))
try:
    new_map_size = int(input("Enter new map size: "))
except:
    print("Map size must be of integer type and not larger than 255!")
    sys.exit()
direction = "W"
print("        North")
print("          ^")
print("          |")
print("West <- Center -> East")
print("          |")
print("          V")
print("        South")
direction = input("Choose direction to expand map into: (N|S|E|W|C): ")
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
output_scenario.write_to_file(output_path2)

print("final")
