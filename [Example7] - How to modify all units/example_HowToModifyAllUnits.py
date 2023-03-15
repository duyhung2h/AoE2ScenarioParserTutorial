import sys
import os
import time
from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *
from buildings import BuildingInfo
from buildings_rubble import BuildingRubbleInfo
from AoE2ScenarioParser.datasets.units import UnitInfo


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


'''
File & Folder setup
Copy the file name (click on the line and CTRL + C):

ScenarioParser - ModifyAllUnits
Tales of Tenebria version 0v18v32
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

# Trigger name
trigger_name = "||example_HowToModifyAllUnits.py||"

triggerStart = -1
triggerEnd = -1
# remove past triggers
for triggerId in range(0, len(source_trigger_manager.triggers), 1):
    # select old modify trigger and remove it
    if source_trigger_manager.triggers[triggerId].name == trigger_name + "start":
        triggerStart = triggerId
    if source_trigger_manager.triggers[triggerId].name == trigger_name + "end":
        triggerEnd = triggerId
print(triggerStart, triggerEnd)
print(source_trigger_manager.triggers[triggerStart])
print(source_trigger_manager.triggers[triggerEnd])

# start deletion
# source_trigger_manager.triggers = source_trigger_manager.triggers[:triggerStart]+source_trigger_manager.triggers[triggerEnd+1:]
# for trigger in source_trigger_manager.triggers[:triggerStart]+source_trigger_manager.triggers[triggerEnd+1:]:
#     print(trigger.name)
if triggerStart > -1:
    for triggerId in range(int(triggerStart), int(triggerEnd + 1), 1):
        print(source_trigger_manager.triggers[triggerStart].name)
        source_trigger_manager.remove_trigger(
            trigger_select=TriggerSelect.index(source_trigger_manager.triggers[triggerStart].trigger_id))
    print("deletion done")

# modify unit from id 0-1800
source_trigger_manager.add_trigger(trigger_name + "start")
# for modify_trigger_id in range(0, 1800, 1):
#     modify_trigger = source_trigger_manager.add_trigger(trigger_name+str(modify_trigger_id))
#     modify_trigger.new_condition.timer(timer=modify_trigger_id)
#     for unitId in range(0, 1, 1):
#         modify_trigger.new_effect.modify_attribute(quantity=1, operation=Operation.SET, source_player=3,
#                                                    object_list_unit_id=modify_trigger_id,
#                                                    object_attributes=ObjectAttribute.FOG_VISIBILITY)

# modify unit from an unit id list
key = 0

'''
# modify buildings
source_trigger_manager.add_trigger("===BUILDINGS===")
for playerId in range(3, 4, 1):
    key = key + 1
    modify_trigger = source_trigger_manager.add_trigger(trigger_name + str(key))
    modify_trigger.new_condition.timer(timer=key)
    for building in BuildingInfo:
        if building.IS_GAIA_ONLY is False:
            modify_trigger.new_effect.modify_attribute(quantity=1, operation=Operation.SET, source_player=playerId,
                                                       object_list_unit_id=building.ID,
                                                       object_attributes=ObjectAttribute.FOG_VISIBILITY)
# modify units
source_trigger_manager.add_trigger("===UNITS===")
for playerId in range(6, 7, 1):
    key = key + 1
    modify_trigger = source_trigger_manager.add_trigger(trigger_name + str(key))
    modify_trigger.new_condition.timer(timer=key)
    for unit in UnitInfo:
        if unit.IS_GAIA_ONLY is False:
            print(unit.ID)
            modify_trigger.new_effect.modify_attribute(quantity=1, operation=Operation.SET, source_player=playerId,
                                                       object_list_unit_id=unit.ID,
                                                       object_attributes=ObjectAttribute.FOG_VISIBILITY)
source_trigger_manager.add_trigger("===UNITSP4===")
for playerId in range(4, 5, 1):
    key = key + 1
    P4_CinemaENABLE = source_trigger_manager.add_trigger(trigger_name + "P4_CinemaENABLE", enabled=True)
    # P2_CinemaDISABLE = source_trigger_manager.add_trigger(trigger_name + "P2_CinemaDISABLE", enabled=False)
    P4_CinemaENABLE.new_condition.variable_value(variable=36, quantity=1)
    for unit in UnitInfo:
        if unit.IS_GAIA_ONLY is False:
            print(unit.ID)
            P4_CinemaENABLE.new_effect.modify_attribute(quantity=1, operation=Operation.SET, source_player=playerId,
                                                        object_list_unit_id=unit.ID,
                                                        object_attributes=ObjectAttribute.FOG_VISIBILITY)
'''

# modify building rubbles (GAIA)
'''
source_trigger_manager.add_trigger("===GAIABUILDINGSRUBBLES===")
for playerId in range(0, 1, 1):
    key = key + 1
    modify_trigger = source_trigger_manager.add_trigger(trigger_name + str(key))
    modify_trigger.new_condition.timer(timer=key)
    for building in BuildingRubbleInfo:
        if building.IS_GAIA_ONLY is False:
            modify_trigger.new_effect.modify_attribute(quantity=1, operation=Operation.SET, source_player=playerId,
                                                       object_list_unit_id=building.ID,
                                                       object_attributes=ObjectAttribute.FOG_VISIBILITY)
'''

# modify all units unit size X and Y, divide them by 100 (P3)
source_trigger_manager.add_trigger("===P3MODIFYUNITS_SIZE===")
for playerId in range(3, 4, 1):
    key = key + 1
    modify_trigger = source_trigger_manager.add_trigger(trigger_name + str(key))
    modify_trigger.new_condition.timer(timer=key)
    for unit in UnitInfo:
        if unit.IS_GAIA_ONLY is False:
            print(unit.ID)
            modify_trigger.new_effect.modify_attribute(quantity=100, operation=Operation.DIVIDE, source_player=playerId,
                                                       object_list_unit_id=unit.ID,
                                                       object_attributes=ObjectAttribute.UNIT_SIZE_X)
            modify_trigger.new_effect.modify_attribute(quantity=100, operation=Operation.DIVIDE, source_player=playerId,
                                                       object_list_unit_id=unit.ID,
                                                       object_attributes=ObjectAttribute.UNIT_SIZE_Y)

source_trigger_manager.add_trigger(trigger_name + "end")

# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)
