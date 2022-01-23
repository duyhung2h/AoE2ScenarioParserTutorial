from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *
from AoE2ScenarioParser.objects.data_objects.trigger import Trigger

from model.Equipment import Equipment
from model.Weapon import Weapon
from model.EquipmentArea import EquipmentArea
from model.Character import Character

# File & Folder setup
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
input_path = scenario_folder + "Tales of Tenebria version 0v8.aoe2scenario"
output_path = scenario_folder + "Tales of Tenebria version 0v8 Parser Result.aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# target_trigger_manager.triggers = []  # Uncomment this in order to wipe all triggers from the map at start
# target_trigger_manager.variables = []  # Uncomment this in order to wipe all variables from the map at start


# put triggers ranging from index position_start to position_end, to position position_transfer in the target file
test_position_start = 0
test_position_end = 0
for triggerId in range(0, len(source_trigger_manager.triggers), 1):
    if source_trigger_manager.triggers[triggerId].name == "------------------testStartCheckShit":
        print(source_trigger_manager.triggers[triggerId].name)
        test_position_start = source_trigger_manager.triggers[triggerId].trigger_id + 1
        test_position_end = test_position_start + 4

# working with triggers
testTriggers = source_trigger_manager.triggers[test_position_start:test_position_end]

print(testTriggers[0].trigger_id)

print(testTriggers[0].conditions[1].object_type)
print("Charles id: " + str(testTriggers[0].conditions[0].unit_object))
print(testTriggers[0].conditions[1].object_type)
print(testTriggers[0].conditions[1].object_list)
print(testTriggers[0].conditions[1].quantity)
print(testTriggers[0].effects[1].trigger_id)
print("Clarissa id: " + str(testTriggers[3].conditions[0].unit_object))
print("Coline id: " + str(testTriggers[3].conditions[1].unit_object))
print("Dominiel id: " + str(testTriggers[3].conditions[2].unit_object))
print("Corvus id: " + str(testTriggers[3].conditions[3].unit_object))
print("Nemunas id: " + str(testTriggers[3].conditions[4].unit_object))

print("condition 1 object state: " + str(testTriggers[0].conditions[1].object_state))

print("area x1 condition 0 trigger 1: " + str(testTriggers[0].conditions[0].area_x1))
print("area x2 condition 0 trigger 1: " + str(testTriggers[0].conditions[0].area_x2))
print("area y1 condition 0 trigger 1: " + str(testTriggers[0].conditions[0].area_y1))
print("area y2 condition 0 trigger 1: " + str(testTriggers[0].conditions[0].area_y2))

print("tele x effect 0 trigger 1: " + str(testTriggers[0].effects[0].location_x))
print("tele y effect 0 trigger 1: " + str(testTriggers[0].effects[0].location_y))

print("tele x effect 2 trigger 1: " + str(testTriggers[0].effects[2].location_x))
print("tele y effect 2 trigger 1: " + str(testTriggers[0].effects[2].location_y))

print("tele x effect 3 trigger 1: " + str(testTriggers[0].effects[3].location_x))
print("tele y effect 3 trigger 1: " + str(testTriggers[0].effects[3].location_y))

print("tele x effect 4 trigger 1: " + str(testTriggers[0].effects[4].location_x))
print("tele y effect 4 trigger 1: " + str(testTriggers[0].effects[4].location_y))

print("area x1 effect 6 trigger 1: " + str(testTriggers[0].effects[6].area_x1))
print("area x2 effect 6 trigger 1: " + str(testTriggers[0].effects[6].area_x2))
print("area y1 effect 6 trigger 1: " + str(testTriggers[0].effects[6].area_y1))
print("area y2 effect 6 trigger 1: " + str(testTriggers[0].effects[6].area_y2))

print("tele x effect 6 trigger 1: " + str(testTriggers[0].effects[6].location_x))
print("tele y effect 6 trigger 1: " + str(testTriggers[0].effects[6].location_y))

print("modify attribute object attribute id (hitpoints): " + str(testTriggers[3].effects[0].object_attributes))
print("modify attribute object attribute id (movement speed): " + str(testTriggers[3].effects[1].object_attributes))
print("modify attribute object attribute id (attack): " + str(testTriggers[3].effects[2].object_attributes))
print("modify attribute object attribute id (armor): " + str(testTriggers[3].effects[3].object_attributes))
print("modify attribute object attribute id (shown attack): " + str(testTriggers[3].effects[4].object_attributes))
print("modify attribute object attribute id (shown range): " + str(testTriggers[3].effects[5].object_attributes))
print("modify attribute object attribute id (shown melee armor): " + str(testTriggers[3].effects[6].object_attributes))
print("modify attribute object attribute id (shown pierce armor): " + str(testTriggers[3].effects[7].object_attributes))
print("modify attribute object attribute id (attack reload time): " + str(testTriggers[3].effects[8].object_attributes))
print("modify attribute object attribute id (building icon override): " + str(
    testTriggers[3].effects[9].object_attributes))
print("modify attribute object attribute id (garrison capacity): " + str(testTriggers[3].effects[10].object_attributes))
print("modify attribute object attribute id (line of sight): " + str(testTriggers[3].effects[11].object_attributes))
print("modify attribute object attribute id (unit size x): " + str(testTriggers[3].effects[12].object_attributes))
print("modify attribute object attribute id (unit size y): " + str(testTriggers[3].effects[13].object_attributes))
print("modify attribute object attribute id (max range): " + str(testTriggers[3].effects[14].object_attributes))

print("Equipment spawn point X: " + str(testTriggers[3].effects[15].location_x))
print("Equipment spawn point Y: " + str(testTriggers[3].effects[15].location_y))

print("modify attribute operation (set): " + str(testTriggers[3].effects[0].operation))
print("modify attribute operation (add): " + str(testTriggers[3].effects[1].operation))
print("modify attribute operation (subtract): " + str(testTriggers[3].effects[2].operation))
print("modify attribute operation (multiply): " + str(testTriggers[3].effects[3].operation))
print("modify attribute operation (divide): " + str(testTriggers[3].effects[4].operation))

print("area x1 character menu trigger 4: " + str(testTriggers[3].conditions[5].area_x1))
print("area x2 character menu trigger 4: " + str(testTriggers[3].conditions[5].area_x2))
print("area y1 character menu trigger 4: " + str(testTriggers[3].conditions[5].area_y1))
print("area y2 character menu trigger 4: " + str(testTriggers[3].conditions[5].area_y2))

print("area inside equipment inventory trigger 4: x1=" + str(testTriggers[3].conditions[6].area_x1) +
      " x2=" + str(testTriggers[3].conditions[6].area_x2) +
      " y1=" + str(testTriggers[3].conditions[6].area_y1) +
      " y2=" + str(testTriggers[3].conditions[6].area_y2))
print("area check character death trigger 4: x1=" + str(testTriggers[3].conditions[7].area_x1) +
      " x2=" + str(testTriggers[3].conditions[7].area_x2) +
      " y1=" + str(testTriggers[3].conditions[7].area_y1) +
      " y2=" + str(testTriggers[3].conditions[7].area_y2))
print("area check core character control board trigger 4: x1=" + str(testTriggers[3].conditions[8].area_x1) +
      " x2=" + str(testTriggers[3].conditions[8].area_x2) +
      " y1=" + str(testTriggers[3].conditions[8].area_y1) +
      " y2=" + str(testTriggers[3].conditions[8].area_y2))

print("---------------------------------------")
print("trigger list with their id:")
for triggerId in range(0, len(source_trigger_manager.triggers), 1):
    print(source_trigger_manager.triggers[triggerId].name + ", ID: "
          + str(source_trigger_manager.triggers[triggerId].trigger_id))

# [x1, x2], [y1, y2]
listCharactersEquipmentArea = EquipmentArea.get_equipmentarea()
characterSlotArea = [
    [[449, 451], [466, 468]],
    [[449, 451], [470, 472]],
    [[465, 467], [466, 468]],
    [[465, 467], [470, 472]],
]
print(listCharactersEquipmentArea[0].weaponArea[0][0])  # x1
print(listCharactersEquipmentArea[0].weaponArea[1][0])  # y1
print(listCharactersEquipmentArea[0].weaponArea[0][1])  # x2
print(listCharactersEquipmentArea[0].weaponArea[1][1])  # y2

# unitName, unitId, characterClass, coreUnitId, skill1Icon, skill2Icon, maxRange, projectileId, hp, atk, meleeArmor, pierceArmor, potraitId
listCharacters = Character.get_characters()
listEquipments = []
listEquipments.extend(Equipment.get_equipment())
listEquipments.extend(Weapon.get_weapon())
print(vars(listEquipments[9]))

# remove past triggers
triggerStart = 0
triggerEnd = 0
for triggerId in range(0, len(source_trigger_manager.triggers), 1):
    if source_trigger_manager.triggers[triggerId].name == "ToT - enemies.py Start":
        print(source_trigger_manager.triggers[triggerId].name)
        triggerStart = triggerId
    if source_trigger_manager.triggers[triggerId].name == "ToT - enemies.py End":
        print(source_trigger_manager.triggers[triggerId].name)
        triggerEnd = triggerId
print(triggerStart, triggerEnd)
for triggerId in range(triggerStart - 1, int(triggerEnd), 1):
    source_trigger_manager.remove_trigger(
        trigger_select=TriggerSelect.index(source_trigger_manager.triggers[triggerStart].trigger_id))

# start adding triggers
triggerStart = source_trigger_manager.add_trigger("ToT - enemies.py Start")

triggerEnd = source_trigger_manager.add_trigger("ToT - enemies.py End")

# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)
