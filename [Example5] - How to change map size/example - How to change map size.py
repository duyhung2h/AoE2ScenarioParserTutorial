import math
from typing import List

import sys
from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
# from itertools import islice
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
# print(new_map_size)
# scenario.map_manager.map_size = 210;
# scenario.map_manager.map_size = 120;
# print(scenario.unit_manager.get_all_units())
# triggers = source_scenario.trigger_manager.triggers
# terrains = source_scenario.map_manager.terrain
# newTerrains = List[TerrainTile]

spt_unit_manager = SPTUnitManager(
    scenario=source_scenario, direction=direction, old_map_size=old_map_size, new_map_size=new_map_size)
spt_unit_manager.move_unit()

# for unit in source_scenario.unit_manager.get_all_units():
#     if direction == "E":
#         if unit.x > new_map_size or unit.y > new_map_size:
#             print("Out of bound unit removed!" + str(unit))
#             source_scenario.unit_manager.remove_unit(unit=unit)
#         else:
#             print()
#     if direction == "W":
#         if unit.x < (old_map_size - new_map_size) or unit.y < (old_map_size - new_map_size):
#             print("Out of bound unit removed!" + str(unit))
#             source_scenario.unit_manager.remove_unit(unit=unit)
#         else:
#             print()
#             unit.x = unit.x + (new_map_size - old_map_size)
#             unit.y = unit.y + (new_map_size - old_map_size)
#     if direction == "N":
#         if unit.x < -(new_map_size - old_map_size) or unit.y > new_map_size:
#             print()
#             # print("Out of bound unit removed!" + str(unit))
#             # scenario.unit_manager.remove_unit(unit=unit)
#         else:
#             unit.y = unit.y + (new_map_size - old_map_size)

spt_unit_manager.move_triggers()

# if direction == "W" or direction == "N":
#     for trigger in triggers:
#         for effect in trigger.effects:
#             if effect.location_x > -1:
#                 if direction != "N":
#                     effect.location_x = int(
#                         effect.location_x + (new_map_size - old_map_size))
#                 effect.location_y = int(
#                     effect.location_y + (new_map_size - old_map_size))
#             if effect.area_x1 > -1:
#                 if direction != "N":
#                     effect.area_x1 = int(
#                         effect.area_x1 + (new_map_size - old_map_size))
#                     effect.area_x2 = int(
#                         effect.area_x2 + (new_map_size - old_map_size))
#                 effect.area_y1 = int(
#                     effect.area_y1 + (new_map_size - old_map_size))
#                 effect.area_y2 = int(
#                     effect.area_y2 + (new_map_size - old_map_size))
#         for condition in trigger.conditions:
#             if condition.area_x1 > -1:
#                 if direction != "N":
#                     condition.area_x1 = int(
#                         condition.area_x1 + (new_map_size - old_map_size))
#                     condition.area_x2 = int(
#                         condition.area_x2 + (new_map_size - old_map_size))
#                 condition.area_y1 = int(
#                     condition.area_y1 + (new_map_size - old_map_size))
#                 condition.area_y2 = int(
#                     condition.area_y2 + (new_map_size - old_map_size))


# change map size to inputted new map size
# scenario.map_manager.map_size = new_map_size;


# to_be_removed = set(um.get_units_in_area(new_size, 0, old_size, old_size))
# to_be_removed.update(um.get_units_in_area(0, new_size, old_size, old_size))
# for u in to_be_removed:
#     um.remove_unit(unit=u)


spt_unit_manager.extend_map_iteration1()
source_scenario = spt_unit_manager.scenario

# if direction == "W":
#     terrains.reverse()


# if direction != "N":
#     source_scenario.map_manager.map_size = new_map_size
#     terrains.reverse()

# if direction == "N" and new_map_size > old_map_size:
#     source_scenario.map_manager.map_size = new_map_size
# if direction == "N" and new_map_size < old_map_size:
#     source_scenario.map_manager.map_size = old_map_size+(old_map_size-new_map_size)

# northernTerrains = []
# if direction == "N" and new_map_size < old_map_size:
#     print(terrains[0])
#     northernTerrains = terrains.copy()
#     # terrain = terrains[(old_map_size-new_map_size)*old_map_size:][:new_map_size*new_map_size]
#     print(northernTerrains[0])
#     print(len(northernTerrains))
#     print(new_map_size*new_map_size)

#     source_scenario.map_manager.map_size = 0
#     source_scenario.map_manager.map_size = new_map_size
#     input()

# Commit initial terrain changes, then reverse that again
source_scenario.write_to_file(output_path)
source_scenario2 = AoE2DEScenario.from_file(input_path)
output_scenario = AoE2DEScenario.from_file(output_path)



spt_unit_manager2 = SPTUnitManager(
    scenario=output_scenario, direction=direction, old_map_size=old_map_size, new_map_size=new_map_size)


# output_terrains = output_scenario.map_manager.terrain
# terrains = source_scenario2.map_manager.terrain


# print("terrain length: " + str(output_terrains.__len__()))

spt_unit_manager2.extend_map_iteration2()
output_scenario = spt_unit_manager.scenario

# if direction == "W":
#     output_scenario.map_manager.terrain.reverse()
# if direction == "N" and new_map_size > old_map_size:
#     for terrainId in range(0, (new_map_size-old_map_size)*new_map_size, 1):
#         print("transfer")
#         output_terrains.insert(
#             0, output_terrains.pop(output_terrains.__len__()-1))
# if direction == "N" and new_map_size < old_map_size:
#     for terrainId in range(0, math.sqrt((old_map_size + (old_map_size-new_map_size))), 1):
#         print("transfer")
#         output_terrains.insert(
#             0, output_terrains.pop(output_terrains.__len__()-1))



# if direction == "N" and new_map_size < old_map_size:
#     print(len(output_terrains))

#     print(output_terrains[0])
#     # output_terrains = []
#     print(terrains[0])
#     output_terrains = []
#     # output_terrains = terrains[(old_map_size-new_map_size)*old_map_size:][:new_map_size*new_map_size].copy()
#     output_terrains = terrains[:new_map_size*new_map_size]

#     # print(len(terrains[:new_map_size * new_map_size]))
#     print(terrains[0])
#     print(output_terrains[0])
#     input()
#     # output_scenario.map_manager.map_size = new_map_size;

# Final step: write a modified scenario class to a new scenario file
output_scenario.write_to_file(output_path2)

print("final")
