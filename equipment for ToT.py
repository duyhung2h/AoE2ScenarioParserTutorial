from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *
from AoE2ScenarioParser.datasets.units import *
from AoE2ScenarioParser.datasets.buildings import *
from AoE2ScenarioParser.datasets.heroes import *
from AoE2ScenarioParser.datasets.other import *
from AoE2ScenarioParser.datasets.projectiles import *
from AoE2ScenarioParser.objects.data_objects.trigger import Trigger
from AoE2ScenarioParser.objects.data_objects.condition import Condition
from AoE2ScenarioParser.objects.data_objects.effect import Effect
from AoE2ScenarioParser.objects.support.new_condition import NewConditionSupport
from AoE2ScenarioParser.objects.support.new_effect import NewEffectSupport

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
print("area unequipment trigger 4: x1=" + str(testTriggers[3].conditions[9].area_x1) +
      " x2=" + str(testTriggers[3].conditions[9].area_x2) +
      " y1=" + str(testTriggers[3].conditions[9].area_y1) +
      " y2=" + str(testTriggers[3].conditions[9].area_y2))

print("--------Variables-------------------------------")
unit_manager = source_scenario.unit_manager
# print(unit_manager.units)
variables = source_scenario.trigger_manager.variables
for variableNum in range(0, len(variables), 1):
    print("ID: " + str(variables[variableNum].variable_id) + " - " + variables[variableNum].name)
print("---------------------------------------")
# for a in range(0, len(UnitInfo), 1):
# print(UnitInfo[a].ID)
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
    if source_trigger_manager.triggers[triggerId].name == "equipment for ToT.py Start":
        print(source_trigger_manager.triggers[triggerId].name)
        triggerStart = triggerId
    if source_trigger_manager.triggers[triggerId].name == "equipment for ToT.py End":
        print(source_trigger_manager.triggers[triggerId].name)
        triggerEnd = triggerId
print(triggerStart, triggerEnd)
for triggerId in range(triggerStart - 1, int(triggerEnd), 1):
    source_trigger_manager.remove_trigger(
        trigger_select=TriggerSelect.index(source_trigger_manager.triggers[triggerStart].trigger_id))

# start adding triggers
triggerStart = source_trigger_manager.add_trigger("equipment for ToT.py Start")
triggerTestCreateEquipment = source_trigger_manager.add_trigger("testCreateEquipment", enabled=True, looping=False)
triggerTestCreateEquipment.new_condition.timer(timer=9)
for a in range(0, len(listEquipments), 1):
    triggerTestCreateEquipment.new_effect.create_object(location_x=458, location_y=475,
                                                        source_player=1, object_list_unit_id=listEquipments[a].unitId)
# modify equipment stats
triggerModifyEquipment = source_trigger_manager.add_trigger("modifyEquipmentStats", enabled=True, looping=False)
triggerModifyEquipment.new_condition.timer(timer=19)
weaponNameId = 1002200
for a in range(0, len(listEquipments), 1):
    triggerModifyEquipment.new_effect.modify_attribute(object_attributes=ObjectAttribute.MOVEMENT_SPEED,
                                                       operation=Operation.SET, source_player=1,
                                                       quantity=5, object_list_unit_id=listEquipments[a].unitId)
    triggerModifyEquipment.new_effect.modify_attribute(object_attributes=ObjectAttribute.OBJECT_NAME_ID,
                                                       operation=Operation.SET, source_player=1,
                                                       quantity=1002000 + a,
                                                       object_list_unit_id=listEquipments[a].unitId)
    if listEquipments[a].equipmentType == "Weapon":
        triggerModifyEquipment.new_effect.modify_attribute(object_attributes=ObjectAttribute.OBJECT_NAME_ID,
                                                           operation=Operation.SET, source_player=1,
                                                           quantity=weaponNameId,
                                                           object_list_unit_id=listEquipments[a].unitId)
        weaponNameId = weaponNameId + 1
    triggerModifyEquipment.new_effect.modify_attribute(object_attributes=ObjectAttribute.MINIMUM_RANGE,
                                                       operation=Operation.SET, source_player=3,
                                                       quantity=17,
                                                       object_list_unit_id=listEquipments[a].unitId)
    # Choose icon id
    iconId = -1
    if listEquipments[a].equipmentType == "Weapon":
        if listEquipments[a].equipmentCategory == "dagger":
            iconId = 278
        if listEquipments[a].equipmentCategory == "bow":
            iconId = 279
        if listEquipments[a].equipmentCategory == "staff":
            iconId = 280
        if listEquipments[a].equipmentCategory == "sword":
            iconId = 281
    elif listEquipments[a].equipmentType == "Headwear":
        iconId = 275
    elif listEquipments[a].equipmentType == "Armor":
        iconId = 276
    elif listEquipments[a].equipmentType == "Boots":
        iconId = 277
    triggerModifyEquipment.new_effect.modify_attribute(object_attributes=ObjectAttribute.ICON_ID,
                                                       operation=Operation.SET, source_player=1,
                                                       quantity=iconId, object_list_unit_id=listEquipments[a].unitId)
    triggerModifyEquipment.new_effect.modify_attribute(object_attributes=ObjectAttribute.UNIT_SIZE_X,
                                                       operation=Operation.SET, source_player=1,
                                                       quantity=1, object_list_unit_id=listEquipments[a].unitId)
    triggerModifyEquipment.new_effect.modify_attribute(object_attributes=ObjectAttribute.UNIT_SIZE_Y,
                                                       operation=Operation.SET, source_player=1,
                                                       quantity=1, object_list_unit_id=listEquipments[a].unitId)
    triggerModifyEquipment.new_effect.modify_attribute(object_attributes=ObjectAttribute.UNIT_SIZE_X,
                                                       operation=Operation.DIVIDE, source_player=1,
                                                       quantity=100, object_list_unit_id=listEquipments[a].unitId)
    triggerModifyEquipment.new_effect.modify_attribute(object_attributes=ObjectAttribute.UNIT_SIZE_Y,
                                                       operation=Operation.DIVIDE, source_player=1,
                                                       quantity=100, object_list_unit_id=listEquipments[a].unitId)
    amountOfSuffix = 0
    if listEquipments[a].rarity == "BLUE":
        amountOfSuffix = 1
    elif listEquipments[a].rarity == "PURPLE":
        amountOfSuffix = 2
    elif listEquipments[a].rarity == "ORANGE":
        amountOfSuffix = 3
    triggerModifyEquipment.new_effect.modify_attribute(object_attributes=ObjectAttribute.GARRISON_CAPACITY,
                                                       operation=Operation.SET, source_player=1,
                                                       quantity=amountOfSuffix,
                                                       object_list_unit_id=listEquipments[a].unitId)
    triggerModifyEquipment.new_effect.none()

# run for each character
triggerSeparator = source_trigger_manager.add_trigger("--checkSwitchCharLocation------")
for a in range(0, len(listCharacters), 1):
    triggerCharacterSwitch1 = source_trigger_manager.add_trigger("switchTo" + listCharacters[a].unitName + "Click",
                                                                 enabled=True, looping=True)
    triggerCharacterSwitch1.new_condition.bring_object_to_area(area_x1=449, area_x2=467,
                                                               area_y1=466, area_y2=472,
                                                               unit_object=listCharacters[a].coreUnitId)
    triggerCharacterSwitch1.new_condition.capture_object(source_player=1,
                                                         unit_object=listCharacters[a].coreUnitId)
    triggerCharacterSwitch1.new_condition.object_selected(unit_object=listCharacters[a].coreUnitId)
    triggerCharacterSwitch2 = source_trigger_manager.add_trigger("switchTo" + listCharacters[a].unitName, enabled=False)
    triggerCharacterSwitch1.new_effect.activate_trigger(trigger_id=triggerCharacterSwitch2.trigger_id)
    switchToTriggerId = triggerCharacterSwitch2.trigger_id
    triggerCharacterSwitch2.new_effect.send_chat(
        message="<AQUA>Main character switched to: " + listCharacters[a].unitName,
        source_player=1)
    for arrowId in range(0, 5, 1):
        triggerCharacterSwitch2.new_effect.remove_object(source_player=1, object_list_unit_id=317 + arrowId)
        triggerCharacterSwitch2.new_effect.remove_object(source_player=3, object_list_unit_id=317 + arrowId)
    # triggerCharacterSwitch2.new_effect.change_ownership(source_player=1, target_player=5,
    #                                                     object_type=ObjectType.MILITARY)
    # triggerCharacterSwitch2.new_effect.change_ownership(source_player=5, target_player=1,
    #                                                     object_type=ObjectType.MILITARY,
    #                                                     area_x1=440, area_x2=479,
    #                                                     area_y1=459, area_y2=479)
    triggerCharacterSwitch2.new_effect.modify_attribute(source_player=3,
                                                        object_attributes=ObjectAttribute.OBJECT_NAME_ID,
                                                        operation=Operation.SET, quantity=1001000 + (a * 2),
                                                        object_list_unit_id=97)
    triggerCharacterSwitch2.new_effect.modify_attribute(source_player=3,
                                                        object_attributes=ObjectAttribute.OBJECT_NAME_ID,
                                                        operation=Operation.SET, quantity=1001001 + (a * 2),
                                                        object_list_unit_id=312)
    triggerCharacterSwitch2.new_effect.none()
    triggerCharacterSwitch2.new_effect.modify_attribute(source_player=3, object_attributes=ObjectAttribute.ICON_ID,
                                                        operation=Operation.SET, quantity=listCharacters[a].skill1Icon,
                                                        object_list_unit_id=97)
    triggerCharacterSwitch2.new_effect.modify_attribute(source_player=3, object_attributes=ObjectAttribute.ICON_ID,
                                                        operation=Operation.SET, quantity=listCharacters[a].skill2Icon,
                                                        object_list_unit_id=312)
    triggerCharacterSwitch2.new_effect.none()
    triggerCharacterSwitch2.new_effect.change_ownership(area_x1=449, area_x2=451,
                                                        area_y1=466, area_y2=472,
                                                        source_player=3, target_player=1)
    triggerCharacterSwitch2.new_effect.change_ownership(area_x1=465, area_x2=467,
                                                        area_y1=466, area_y2=472,
                                                        source_player=3, target_player=1)
    triggerCharacterSwitch2.new_effect.change_ownership(area_x1=449, area_x2=451,
                                                        area_y1=466, area_y2=472,
                                                        source_player=1, target_player=3,
                                                        object_list_unit_id=listCharacters[a].unitId)
    triggerCharacterSwitch2.new_effect.change_ownership(area_x1=465, area_x2=467,
                                                        area_y1=466, area_y2=472,
                                                        source_player=1, target_player=3,
                                                        object_list_unit_id=listCharacters[a].unitId)
    triggerCharacterSwitch2.new_effect.change_ownership(area_x1=449, area_x2=451,
                                                        area_y1=466, area_y2=472,
                                                        source_player=1, target_player=4)
    triggerCharacterSwitch2.new_effect.change_ownership(area_x1=465, area_x2=467,
                                                        area_y1=466, area_y2=472,
                                                        source_player=1, target_player=4)
    triggerCharacterSwitch2.new_effect.none()
    for b in range(0, len(listCharacters), 1):
        triggerCharacterSwitch2.new_effect.replace_object(source_player=1, target_player=5,
                                                          object_list_unit_id=listCharacters[b].unitId,
                                                          object_list_unit_id_2=600)
        triggerCharacterSwitch2.new_effect.replace_object(source_player=5, target_player=5,
                                                          object_list_unit_id=600,
                                                          object_list_unit_id_2=listCharacters[b].unitId)
    triggerCharacterSwitch2.new_effect.replace_object(source_player=5, target_player=1,
                                                      object_list_unit_id=listCharacters[a].unitId,
                                                      object_list_unit_id_2=listCharacters[a].unitId)
    triggerCharacterSwitch2.new_effect.none()
    triggerCharacterSwitch2.new_effect.change_ownership(area_x1=449, area_x2=451,
                                                        area_y1=466, area_y2=472,
                                                        source_player=4, target_player=1)
    triggerCharacterSwitch2.new_effect.change_ownership(area_x1=465, area_x2=467,
                                                        area_y1=466, area_y2=472,
                                                        source_player=4, target_player=1)
    triggerCharacterSwitch2.new_effect.none()
    # for arrowId in range(0, 5, 1):
    #     triggerCharacterSwitch2.new_effect.create_garrisoned_object(source_player=1,
    #                                                                 object_list_unit_id=listCharacters[a].unitId,
    #                                                                 object_list_unit_id_2=317 + arrowId)
    #     triggerCharacterSwitch2.new_effect.replace_object(source_player=1, target_player=3,
    #                                                       object_list_unit_id=317 + arrowId,
    #                                                       object_list_unit_id_2=317 + arrowId)
    triggerCharacterSwitch2.new_effect.none()

    for b in range(0, len(characterSlotArea), 1):
        triggerCharacterSwitchLocation1 = source_trigger_manager.add_trigger(
            listCharacters[a].unitName + "CheckPotraitLoc" + str(b + 1),
            enabled=True, looping=True)
        triggerCharacterSwitchLocation1.new_condition.timer(timer=1)
        triggerCharacterSwitchLocation1.new_condition.bring_object_to_area(unit_object=listCharacters[a].coreUnitId,
                                                                           area_x1=characterSlotArea[b][0][0],
                                                                           area_x2=characterSlotArea[b][0][1],
                                                                           area_y1=characterSlotArea[b][1][0],
                                                                           area_y2=characterSlotArea[b][1][1])
        triggerCharacterSwitchLocation1.new_condition.own_fewer_objects(quantity=0, object_list=(317 + b),
                                                                        source_player=3)
        triggerCharacterSwitchLocation1.new_condition.objects_in_area(area_x1=characterSlotArea[b][0][0],
                                                                      area_x2=characterSlotArea[b][0][1],
                                                                      area_y1=characterSlotArea[b][1][0],
                                                                      area_y2=characterSlotArea[b][1][1],
                                                                      quantity=1, source_player=1,
                                                                      object_list=listCharacters[a].unitId,
                                                                      object_state=ObjectState.ALIVE)
        triggerCharacterSwitchLocation1.new_effect.modify_attribute(source_player=3,
                                                                    object_attributes=ObjectAttribute.OBJECT_NAME_ID,
                                                                    operation=Operation.SET,
                                                                    object_list_unit_id=(317 + b),
                                                                    quantity=1003100 + (a * 100))
        triggerCharacterSwitchLocation1.new_effect.modify_attribute(source_player=3,
                                                                    object_attributes=ObjectAttribute.ICON_ID,
                                                                    operation=Operation.SET,
                                                                    object_list_unit_id=(317 + b),
                                                                    quantity=listCharacters[a].potraitId)
        # create switch button inside character
        for c in range(0, len(listCharacters), 1):
            triggerCharacterSwitchLocation1.new_effect.create_garrisoned_object(
                object_list_unit_id=listCharacters[c].unitId,
                object_list_unit_id_2=(317 + b),
                source_player=1)
        triggerCharacterSwitchLocation1.new_effect.replace_object(object_list_unit_id=(317 + b),
                                                                  object_list_unit_id_2=(317 + b),
                                                                  source_player=1, target_player=3)
        triggerCharacterSwitchLocation2 = source_trigger_manager.add_trigger(
            listCharacters[a].unitName + "CheckSCLoc" + str(b + 1),
            enabled=True, looping=True)
        triggerCharacterSwitchLocation2.new_condition.objects_in_area(area_x1=454, area_x2=456,
                                                                      area_y1=462, area_y2=464,
                                                                      object_list=(317 + b),
                                                                      quantity=1, object_state=ObjectState.ALIVE,
                                                                      source_player=3)
        triggerCharacterSwitchLocation2.new_condition.bring_object_to_area(area_x1=characterSlotArea[b][0][0],
                                                                           area_x2=characterSlotArea[b][0][1],
                                                                           area_y1=characterSlotArea[b][1][0],
                                                                           area_y2=characterSlotArea[b][1][1],
                                                                           unit_object=listCharacters[a].coreUnitId)
        triggerCharacterSwitchLocation2.new_condition.capture_object(unit_object=listCharacters[a].coreUnitId,
                                                                     source_player=6,
                                                                     inverted=True)
        triggerCharacterSwitchLocation2.new_effect.remove_object(area_x1=455, area_x2=455,
                                                                 area_y1=463, area_y2=463,
                                                                 source_player=3, object_state=ObjectState.ALIVE,
                                                                 object_list_unit_id=(317 + b))
        triggerCharacterSwitchLocation2.new_effect.modify_attribute(object_list_unit_id=(317 + b), source_player=3,
                                                                    object_attributes=ObjectAttribute.HIT_POINTS,
                                                                    quantity=0, operation=Operation.SET)
        # triggerCharacterSwitchLocation2.new_effect.send_chat(message="test: clicked button " + str(317 + b),
        #                                                      source_player=1)
        triggerCharacterSwitchLocation2.new_effect.activate_trigger(trigger_id=switchToTriggerId)
        triggerCharacterSwitchLocation3 = source_trigger_manager.add_trigger("-----------------")

# run for each character
triggerModifyCharacters = source_trigger_manager.add_trigger("modifyCharactersStat")
triggerModifyCharacters.new_condition.timer(timer=2)
for a in range(0, len(listCharacters), 1):
    triggerModifyCharacters.new_effect.modify_attribute(object_attributes=ObjectAttribute.MINIMUM_RANGE,
                                                        operation=Operation.SET, source_player=3,
                                                        quantity=17,
                                                        object_list_unit_id=listCharacters[a].unitId)
    # shown range
    triggerModifyCharacters.new_effect.modify_attribute(object_attributes=ObjectAttribute.SHOWN_RANGE,
                                                        operation=Operation.SET, source_player=1,
                                                        quantity=listCharacters[a].maxRange,
                                                        object_list_unit_id=listCharacters[a].unitId)
    triggerModifyCharacters.new_effect.modify_attribute(object_attributes=ObjectAttribute.SHOWN_RANGE,
                                                        operation=Operation.SET, source_player=5,
                                                        quantity=listCharacters[a].maxRange,
                                                        object_list_unit_id=listCharacters[a].unitId)
    if listCharacters[a].maxRange == 0:
        triggerModifyCharacters.new_effect.modify_attribute(source_player=1,
                                                            object_attributes=ObjectAttribute.MAX_RANGE,
                                                            operation=Operation.SET,
                                                            object_list_unit_id=listCharacters[a].unitId,
                                                            quantity=1)
        triggerModifyCharacters.new_effect.modify_attribute(source_player=5,
                                                            object_attributes=ObjectAttribute.MAX_RANGE,
                                                            operation=Operation.SET,
                                                            object_list_unit_id=listCharacters[a].unitId,
                                                            quantity=1)
        triggerModifyCharacters.new_effect.modify_attribute(source_player=1,
                                                            object_attributes=ObjectAttribute.MAX_RANGE,
                                                            operation=Operation.DIVIDE,
                                                            object_list_unit_id=listCharacters[a].unitId,
                                                            quantity=2)
        triggerModifyCharacters.new_effect.modify_attribute(source_player=5,
                                                            object_attributes=ObjectAttribute.MAX_RANGE,
                                                            operation=Operation.DIVIDE,
                                                            object_list_unit_id=listCharacters[a].unitId,
                                                            quantity=2)
    # atk reload time
    triggerModifyCharacters.new_effect.modify_attribute(source_player=1,
                                                        object_attributes=ObjectAttribute.ATTACK_RELOAD_TIME,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=2)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=5,
                                                        object_attributes=ObjectAttribute.ATTACK_RELOAD_TIME,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=2)
    # range
    triggerModifyCharacters.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.MAX_RANGE,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=listCharacters[a].maxRange)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.MAX_RANGE,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=listCharacters[a].maxRange)
    # hp
    triggerModifyCharacters.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.HIT_POINTS,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=listCharacters[a].hp)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.HIT_POINTS,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=listCharacters[a].hp)
    # atk
    triggerModifyCharacters.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.ATTACK,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        armour_attack_quantity=listCharacters[a].atk + (256 * 3),
                                                        armour_attack_class=0)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.ATTACK,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        armour_attack_quantity=listCharacters[a].atk + (256 * 3),
                                                        armour_attack_class=0)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.ATTACK,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        armour_attack_quantity=listCharacters[a].atk + (256 * 4),
                                                        armour_attack_class=0)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.ATTACK,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        armour_attack_quantity=listCharacters[a].atk + (256 * 4),
                                                        armour_attack_class=0)
    # shown atk
    triggerModifyCharacters.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.SHOWN_ATTACK,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=listCharacters[a].atk)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.SHOWN_ATTACK,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=listCharacters[a].atk)
    # garrison capacity
    triggerModifyCharacters.new_effect.modify_attribute(source_player=1,
                                                        object_attributes=ObjectAttribute.GARRISON_CAPACITY,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=10)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=5,
                                                        object_attributes=ObjectAttribute.GARRISON_CAPACITY,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=10)
    # shown armor melee
    triggerModifyCharacters.new_effect.modify_attribute(source_player=1,
                                                        object_attributes=ObjectAttribute.SHOWN_MELEE_ARMOR,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=listCharacters[a].meleeArmor)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=5,
                                                        object_attributes=ObjectAttribute.SHOWN_MELEE_ARMOR,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=listCharacters[a].meleeArmor)
    # shown armor pierce
    triggerModifyCharacters.new_effect.modify_attribute(source_player=1,
                                                        object_attributes=ObjectAttribute.SHOWN_PIERCE_ARMOR,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=listCharacters[a].pierceArmor)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=5,
                                                        object_attributes=ObjectAttribute.SHOWN_PIERCE_ARMOR,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=listCharacters[a].pierceArmor)
    # armor
    triggerModifyCharacters.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.ARMOR,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        armour_attack_quantity=listCharacters[a].pierceArmor + (
                                                                256 * 3),
                                                        armour_attack_class=0)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.ARMOR,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        armour_attack_quantity=listCharacters[a].pierceArmor + (
                                                                256 * 3),
                                                        armour_attack_class=0)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.ARMOR,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        armour_attack_quantity=listCharacters[a].meleeArmor + (256 * 4),
                                                        armour_attack_class=0)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.ARMOR,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        armour_attack_quantity=listCharacters[a].meleeArmor + (256 * 4),
                                                        armour_attack_class=0)
    # shown armor pierce
    triggerModifyCharacters.new_effect.modify_attribute(source_player=1,
                                                        object_attributes=ObjectAttribute.OBJECT_NAME_ID,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=1003101 + (a * 100))
    triggerModifyCharacters.new_effect.modify_attribute(source_player=5,
                                                        object_attributes=ObjectAttribute.OBJECT_NAME_ID,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=1003101 + (a * 100))
    # dead unit id
    triggerModifyCharacters.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.DEAD_UNIT_ID,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=601)
    triggerModifyCharacters.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.DEAD_UNIT_ID,
                                                        operation=Operation.SET,
                                                        object_list_unit_id=listCharacters[a].unitId,
                                                        quantity=601)
    triggerModifyCharacters.new_effect.none()

triggerSeparator = source_trigger_manager.add_trigger("---TeleToSlotIfInParty------")
# check if character is in the party -> teleport them into the party panel
for a in range(0, len(listCharacters), 1):
    # check p1
    triggerCheckCharacterJoinedPartyP5 = source_trigger_manager.add_trigger("if" + listCharacters[a].unitName
                                                                            + "InPartyP5",
                                                                            enabled=True, looping=True)
    triggerCheckCharacterJoinedPartyP5.new_condition.own_objects(source_player=5, quantity=1,
                                                                 object_list=listCharacters[a].unitId)
    # triggerCheckCharacterJoinedPartyP5.new_condition.bring_object_to_area(unit_object=listCharacters[a].coreUnitId,
    #                                                                       area_x1=449, area_x2=467,
    #                                                                       area_y1=466, area_y2=476,
    #                                                                       inverted=True)
    # triggerCheckCharacterJoinedPartyP5.new_condition.bring_object_to_area(unit_object=listCharacters[a].coreUnitId,
    #                                                                       area_x1=458, area_x2=460,
    #                                                                       area_y1=459, area_y2=461,
    #                                                                       inverted=True)
    triggerCheckCharacterJoinedPartyP5.new_condition.capture_object(unit_object=listCharacters[a].coreUnitId,
                                                                    source_player=1)
    triggerCheckCharacterJoinedPartyP5.new_condition.own_fewer_objects(source_player=1, quantity=0,
                                                                       object_list=listCharacters[a].unitId,
                                                                       area_x1=449, area_x2=467,
                                                                       area_y1=466, area_y2=476)
    triggerCheckCharacterJoinedPartyP5.new_condition.own_fewer_objects(source_player=1, quantity=0,
                                                                       object_list=listCharacters[a].unitId,
                                                                       area_x1=458, area_x2=460,
                                                                       area_y1=459, area_y2=461)
    triggerCheckCharacterJoinedPartyP5.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                  location_x=450, location_y=467)
    triggerCheckCharacterJoinedPartyP5.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                  location_x=450, location_y=471)
    triggerCheckCharacterJoinedPartyP5.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                  location_x=466, location_y=467)
    triggerCheckCharacterJoinedPartyP5.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                  location_x=466, location_y=471)
    # check p5
    triggerCheckCharacterJoinedPartyP1 = source_trigger_manager.add_trigger("if" + listCharacters[a].unitName
                                                                            + "InPartyP1",
                                                                            enabled=True, looping=True)
    triggerCheckCharacterJoinedPartyP1.new_condition.own_objects(source_player=1, quantity=1,
                                                                 object_list=listCharacters[a].unitId)
    # triggerCheckCharacterJoinedPartyP1.new_condition.bring_object_to_area(unit_object=listCharacters[a].coreUnitId,
    #                                                                       area_x1=449, area_x2=467,
    #                                                                       area_y1=466, area_y2=476,
    #                                                                       inverted=True)
    # triggerCheckCharacterJoinedPartyP1.new_condition.bring_object_to_area(unit_object=listCharacters[a].coreUnitId,
    #                                                                       area_x1=458, area_x2=460,
    #                                                                       area_y1=459, area_y2=461,
    #                                                                       inverted=True)
    triggerCheckCharacterJoinedPartyP1.new_condition.capture_object(unit_object=listCharacters[a].coreUnitId,
                                                                    source_player=3)
    triggerCheckCharacterJoinedPartyP1.new_condition.own_fewer_objects(source_player=3, quantity=0,
                                                                       object_list=listCharacters[a].unitId,
                                                                       area_x1=449, area_x2=467,
                                                                       area_y1=466, area_y2=476)
    triggerCheckCharacterJoinedPartyP1.new_condition.own_fewer_objects(source_player=3, quantity=0,
                                                                       object_list=listCharacters[a].unitId,
                                                                       area_x1=458, area_x2=460,
                                                                       area_y1=459, area_y2=461)
    triggerCheckCharacterJoinedPartyP1.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                  location_x=450, location_y=467)
    triggerCheckCharacterJoinedPartyP1.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                  location_x=450, location_y=471)
    triggerCheckCharacterJoinedPartyP1.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                  location_x=466, location_y=467)
    triggerCheckCharacterJoinedPartyP1.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                  location_x=466, location_y=471)
    # check core unit in control board, p1
    triggerCheckCharacterJoinedPartyCBP1 = source_trigger_manager.add_trigger("if" + listCharacters[a].unitName
                                                                              + "InCtrlBrdP1",
                                                                              enabled=True, looping=True)
    triggerCheckCharacterJoinedPartyCBP1.new_condition.own_objects(object_list=listCharacters[a].unitId,
                                                                   source_player=1, quantity=1)
    triggerCheckCharacterJoinedPartyCBP1.new_condition.objects_in_area(quantity=1, object_list=listCharacters[a].unitId,
                                                                       source_player=1, inverted=True,
                                                                       area_x1=61, area_x2=69,
                                                                       area_y1=432, area_y2=479),
    triggerCheckCharacterJoinedPartyCBP1.new_condition.bring_object_to_area(unit_object=listCharacters[a].coreUnitId,
                                                                            area_x1=61, area_x2=69,
                                                                            area_y1=432, area_y2=479)
    triggerCheckCharacterJoinedPartyCBP1.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                    location_x=450, location_y=467)
    triggerCheckCharacterJoinedPartyCBP1.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                    location_x=450, location_y=471)
    triggerCheckCharacterJoinedPartyCBP1.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                    location_x=466, location_y=467)
    triggerCheckCharacterJoinedPartyCBP1.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                    location_x=466, location_y=471)
    # check core unit in control board, p5
    triggerCheckCharacterJoinedPartyCBP5 = source_trigger_manager.add_trigger("if" + listCharacters[a].unitName
                                                                              + "InCtrlBrdP5",
                                                                              enabled=True, looping=True)
    triggerCheckCharacterJoinedPartyCBP5.new_condition.own_objects(object_list=listCharacters[a].unitId,
                                                                   source_player=5, quantity=1)
    triggerCheckCharacterJoinedPartyCBP5.new_condition.objects_in_area(quantity=1, object_list=listCharacters[a].unitId,
                                                                       source_player=5, inverted=True,
                                                                       area_x1=61, area_x2=69,
                                                                       area_y1=432, area_y2=479)
    triggerCheckCharacterJoinedPartyCBP5.new_condition.bring_object_to_area(unit_object=listCharacters[a].coreUnitId,
                                                                            area_x1=61, area_x2=69,
                                                                            area_y1=432, area_y2=479)
    triggerCheckCharacterJoinedPartyCBP5.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                    location_x=450, location_y=467)
    triggerCheckCharacterJoinedPartyCBP5.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                    location_x=450, location_y=471)
    triggerCheckCharacterJoinedPartyCBP5.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                    location_x=466, location_y=467)
    triggerCheckCharacterJoinedPartyCBP5.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                                    location_x=466, location_y=471)
triggerSeparator = source_trigger_manager.add_trigger("---CheckCharacherDeath------")
# check if character is killed
for a in range(0, len(listCharacters), 1):
    triggerCheckCharacterDeath = source_trigger_manager.add_trigger(listCharacters[a].unitName + "IsDead",
                                                                    looping=True, enabled=True)
    triggerCheckCharacterDeath.new_condition.bring_object_to_area(unit_object=listCharacters[a].coreUnitId,
                                                                  area_x1=462, area_x2=464,
                                                                  area_y1=462, area_y2=464)
    triggerCheckCharacterDeath.new_condition.capture_object(unit_object=listCharacters[a].coreUnitId, source_player=6)
    triggerCheckCharacterDeath.new_condition.timer(timer=5)
    triggerCheckCharacterDeath.new_effect.display_instructions(instruction_panel_position=2,
                                                               sound_name="ToT - " + listCharacters[
                                                                   a].unitName + "VoiceLines_Death",
                                                               display_time=10, source_player=1,
                                                               object_list_unit_id=listCharacters[a].unitId,
                                                               message="", string_id=1003131 + (a * 100))
    triggerCheckCharacterDeath.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                          location_x=450, location_y=467)
    triggerCheckCharacterDeath.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                          location_x=450, location_y=471)
    triggerCheckCharacterDeath.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                          location_x=466, location_y=467)
    triggerCheckCharacterDeath.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                          location_x=466, location_y=471)

triggerSeparator = source_trigger_manager.add_trigger("---CheckCantEquip------")
# check if character can equip an item
for a in range(0, len(listCharacters), 1):
    triggerCheckCantEquip = source_trigger_manager.add_trigger(listCharacters[a].unitName + "CantEquipThis",
                                                               enabled=True, looping=True)
    triggerCheckCantEquip.new_condition.bring_object_to_area(unit_object=listCharacters[a].coreUnitId,
                                                             area_x1=453, area_x2=463, area_y1=466, area_y2=476)
    triggerCheckCantEquip.new_effect.display_instructions(instruction_panel_position=2, sound_name="Play_error",
                                                          display_time=10, source_player=1,
                                                          object_list_unit_id=listCharacters[a].unitId,
                                                          message="<PURPLE> I can't use that.")
    triggerCheckCantEquip.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                     location_x=450, location_y=467)
    triggerCheckCantEquip.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                     location_x=450, location_y=471)
    triggerCheckCantEquip.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                     location_x=466, location_y=467)
    triggerCheckCantEquip.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                                     location_x=466, location_y=471)
# check level flag
triggerSeparator = source_trigger_manager.add_trigger("---ChecklLevelFlag------")
for a in range(0, len(listCharacters), 1):
    triggerCheckLevelFlag = source_trigger_manager.add_trigger(listCharacters[a].unitName + "CantEquipThis",
                                                               enabled=True, looping=True)
# go to inventory menu
triggerSeparator = source_trigger_manager.add_trigger("------------------")
listMiscMenuButton = [321, 360]
for a in range(0, len(listMiscMenuButton), 1):
    triggerGoToInventory = source_trigger_manager.add_trigger("createMSC" + str(a + 1) + "InsideChar",
                                                              enabled=True, looping=True)
    triggerGoToInventory.new_condition.own_fewer_objects(quantity=0, object_list=listMiscMenuButton[a], source_player=3)
    for b in range(0, len(listCharacters), 1):
        triggerGoToInventory.new_effect.create_garrisoned_object(object_list_unit_id=listCharacters[b].unitId,
                                                                 object_list_unit_id_2=listMiscMenuButton[a],
                                                                 source_player=1)
    triggerGoToInventory.new_effect.replace_object(object_list_unit_id=listMiscMenuButton[a],
                                                   object_list_unit_id_2=listMiscMenuButton[a],
                                                   source_player=1, target_player=3)
# run for each character
triggerSeparator = source_trigger_manager.add_trigger("---Equipments------")
for a in range(0, len(listCharacters), 1):
    print(listCharacters[a].unitName)
    # get equipment area
    centerBootsAreaX = int((listCharactersEquipmentArea[a].bootsArea[0][0]
                            + listCharactersEquipmentArea[a].bootsArea[0][1]) / 2)
    centerBootsAreaY = int((listCharactersEquipmentArea[a].bootsArea[1][0]
                            + listCharactersEquipmentArea[a].bootsArea[1][1]) / 2)

    centerArmorAreaX = int((listCharactersEquipmentArea[a].armorArea[0][0]
                            + listCharactersEquipmentArea[a].armorArea[0][1]) / 2)
    centerArmorAreaY = int((listCharactersEquipmentArea[a].armorArea[1][0]
                            + listCharactersEquipmentArea[a].armorArea[1][1]) / 2)

    centerHeadwearAreaX = int((listCharactersEquipmentArea[a].headwearArea[0][0]
                               + listCharactersEquipmentArea[a].headwearArea[0][1]) / 2)
    centerHeadwearAreaY = int((listCharactersEquipmentArea[a].headwearArea[1][0]
                               + listCharactersEquipmentArea[a].headwearArea[1][1]) / 2)

    centerWeaponAreaX = int((listCharactersEquipmentArea[a].weaponArea[0][0]
                             + listCharactersEquipmentArea[a].weaponArea[0][1]) / 2)
    centerWeaponAreaY = int((listCharactersEquipmentArea[a].weaponArea[1][0]
                             + listCharactersEquipmentArea[a].weaponArea[1][1]) / 2)
    print(centerBootsAreaX, centerBootsAreaY, centerWeaponAreaX, centerWeaponAreaY)

    # run for each equipment
    for b in range(0, len(listEquipments), 1):
        print(listEquipments[b].fullname)
        # check if equipment is a weapon - what kind of equipment is it? Does it match the character's class?
        if listEquipments[b].equipmentType == "Weapon":
            isWeaponMatched = False
            if listEquipments[b].equipmentCategory == "bow" and listCharacters[a].characterClass == "ranger":
                print(listCharacters[a].unitName + " is a ranger!")
                isWeaponMatched = True
            elif listEquipments[b].equipmentCategory == "sword" and listCharacters[a].characterClass == "warrior":
                print(listCharacters[a].unitName + " is a warrior!")
                isWeaponMatched = True
            elif listEquipments[b].equipmentCategory == "dagger" and listCharacters[a].characterClass == "rogue":
                print(listCharacters[a].unitName + " is a rogue!")
                isWeaponMatched = True
            elif listEquipments[b].equipmentCategory == "staff" and listCharacters[a].characterClass == "soulweaver":
                print(listCharacters[a].unitName + " is a soulweaver!")
                isWeaponMatched = True
            if not isWeaponMatched:
                continue

        # add first trigger
        trigger1 = source_trigger_manager.add_trigger("Eq" + listEquipments[b].equipmentType
                                                      + listEquipments[b].unitName + "-"
                                                      + listCharacters[a].unitName, enabled=True, looping=True)
        # condition 0 - check if character unit got teleported to equipment check area
        trigger1.new_condition.bring_object_to_area(unit_object=listCharacters[a].coreUnitId,
                                                    area_x1=458, area_y1=459,
                                                    area_x2=460, area_y2=461)
        # condition 1 - check if equipment unit got teleported to equipment check area
        trigger1.new_condition.objects_in_area(area_x1=458, area_y1=459,
                                               area_x2=460, area_y2=461,
                                               quantity=1, object_state=2,
                                               source_player=1, object_list=listEquipments[b].unitId)
        # effect 0
        # trigger1.new_effect.activate_trigger(trigger_id=trigger1.trigger_id + 1)
        # effect 1 - 4 teleport character core unit back to team equipment area
        trigger1.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                            location_x=450, location_y=467)
        trigger1.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                            location_x=450, location_y=471)
        trigger1.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                            location_x=466, location_y=467)
        trigger1.new_effect.teleport_object(selected_object_ids=[listCharacters[a].coreUnitId],
                                            location_x=466, location_y=471)
        # effect 5 - 6 teleport equipment to equip area, unequip already equipped items
        centerAreaX = -1
        centerAreaY = -1
        equipArea = [[], []]
        if listEquipments[b].equipmentType == "Boots":
            centerAreaX = centerBootsAreaX
            centerAreaY = centerBootsAreaY
            equipArea = listCharactersEquipmentArea[a].bootsArea
        elif listEquipments[b].equipmentType == "Armor":
            centerAreaX = centerArmorAreaX
            centerAreaY = centerArmorAreaY
            equipArea = listCharactersEquipmentArea[a].armorArea
        elif listEquipments[b].equipmentType == "Headwear":
            centerAreaX = centerHeadwearAreaX
            centerAreaY = centerHeadwearAreaY
            equipArea = listCharactersEquipmentArea[a].headwearArea
        elif listEquipments[b].equipmentType == "Weapon":
            centerAreaX = centerWeaponAreaX
            centerAreaY = centerWeaponAreaY
            equipArea = listCharactersEquipmentArea[a].weaponArea

        # [x1, x2], [y1, y2]
        trigger1.new_effect.teleport_object(source_player=3,
                                            area_x1=equipArea[0][0], area_x2=equipArea[0][1],
                                            area_y1=equipArea[1][0], area_y2=equipArea[1][1],
                                            location_x=454, location_y=475)

        trigger1.new_effect.teleport_object(source_player=1,
                                            area_x1=458, area_y1=459,
                                            area_x2=460, area_y2=461,
                                            location_x=centerAreaX, location_y=centerAreaY,
                                            object_list_unit_id=listEquipments[b].unitId)
        # effect 7 display instruction equipping
        playSoundName = ""
        mainStatMessage = ""
        prefixStatMessage = ""
        if listEquipments[b].equipmentType == "Weapon":
            playSoundName = "ToT - EquipWeapons"
            mainStatMessage = "+" + str(listEquipments[b].statModify) + " attack"
            if listEquipments[b].weaponRange != 0:
                prefixStatMessage = prefixStatMessage + "\nPrefix stat: [" + str(
                    100 + listEquipments[b].weaponRange) + "% attack range]"
            if listEquipments[b].weaponAttackSpeed != 0:
                prefixStatMessage = prefixStatMessage + "\nPrefix stat: [" + str(
                    100 + listEquipments[b].weaponAttackSpeed) + "% attack speed]"
        elif listEquipments[b].equipmentType == "Headwear":
            playSoundName = "ToT - EquipHelm"
            mainStatMessage = "+" + str(listEquipments[b].statModify) + "% health"
        elif listEquipments[b].equipmentType == "Armor":
            playSoundName = "ToT - EquipArmor"
            armorTypeMessage = ""
            if listEquipments[b].equipmentCategory == "meleeArmor":
                armorTypeMessage = "melee armor"
            if listEquipments[b].equipmentCategory == "pierceArmor":
                armorTypeMessage = "pierce armor"
            mainStatMessage = "+" + str(listEquipments[b].statModify) + " " + armorTypeMessage
        elif listEquipments[b].equipmentType == "Boots":
            playSoundName = "ToT - EquipBoots"
            mainStatMessage = "+" + str(listEquipments[b].statModify) + "% movement speed"

        trigger1.new_effect.display_instructions(source_player=1, object_list_unit_id=listEquipments[b].unitId,
                                                 display_time=10,
                                                 sound_name=playSoundName,
                                                 instruction_panel_position=0,
                                                 message="<" + listEquipments[b].rarity + "><" + listEquipments[
                                                     b].fullname + "> Equipped to " + listCharacters[
                                                             a].unitName + "! \n\n"
                                                         + "Main stat: [" + mainStatMessage + "]" + prefixStatMessage
                                                 )
        # final effects: modify unit
        if listEquipments[b].equipmentType == "Weapon":
            # modify weapon bonus attack
            trigger1.new_effect.modify_attribute(source_player=1, object_attributes=9,  # attack
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 armour_attack_class=0,
                                                 armour_attack_quantity=256 * 3 + listEquipments[b].statModify,
                                                 operation=2)
            trigger1.new_effect.modify_attribute(source_player=5, object_attributes=9,  # attack
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 armour_attack_class=0,
                                                 armour_attack_quantity=256 * 3 + listEquipments[b].statModify,
                                                 operation=2)
            trigger1.new_effect.none()
            trigger1.new_effect.modify_attribute(source_player=1, object_attributes=9,  # attack
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 armour_attack_class=0,
                                                 armour_attack_quantity=256 * 4 + listEquipments[b].statModify,
                                                 operation=2)
            trigger1.new_effect.modify_attribute(source_player=5, object_attributes=9,  # attack
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 armour_attack_class=0,
                                                 armour_attack_quantity=256 * 4 + listEquipments[b].statModify,
                                                 operation=2)
            trigger1.new_effect.none()
            # modify shown attack
            trigger1.new_effect.modify_attribute(source_player=1, object_attributes=46,  # shown attack
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=listEquipments[b].statModify,
                                                 operation=2)
            trigger1.new_effect.modify_attribute(source_player=5, object_attributes=46,  # shown attack
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=listEquipments[b].statModify,
                                                 operation=2)
            # modify weapon range
            if listEquipments[b].weaponRange != 0:
                trigger1.new_effect.modify_attribute(source_player=1, object_attributes=12,  # max range
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100,
                                                     operation=5)
                trigger1.new_effect.modify_attribute(source_player=1, object_attributes=12,  # max range
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100 + listEquipments[b].weaponRange,
                                                     operation=4)
                trigger1.new_effect.none()
                trigger1.new_effect.modify_attribute(source_player=5, object_attributes=12,  # max range
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100,
                                                     operation=5)
                trigger1.new_effect.modify_attribute(source_player=5, object_attributes=12,  # max range
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100 + listEquipments[b].weaponRange,
                                                     operation=4)
            # modify weapon attack speed
            if listEquipments[b].weaponAttackSpeed != 0:
                trigger1.new_effect.modify_attribute(source_player=1, object_attributes=10,  # attack reload time
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100 + listEquipments[b].weaponAttackSpeed,
                                                     operation=5)
                trigger1.new_effect.modify_attribute(source_player=1, object_attributes=10,  # attack reload time
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100,
                                                     operation=4)
                trigger1.new_effect.none()
                trigger1.new_effect.modify_attribute(source_player=5, object_attributes=10,  # attack reload time
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100 + listEquipments[b].weaponAttackSpeed,
                                                     operation=5)
                trigger1.new_effect.modify_attribute(source_player=5, object_attributes=10,  # attack reload time
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100,
                                                     operation=4)
        # modify headwear hitpoints
        if listEquipments[b].equipmentType == "Headwear":
            trigger1.new_effect.modify_attribute(source_player=1, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=10 + int(listEquipments[b].statModify / 10),
                                                 operation=Operation.MULTIPLY)
            trigger1.new_effect.modify_attribute(source_player=1, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=10,
                                                 operation=Operation.DIVIDE)
            trigger1.new_effect.none()
            trigger1.new_effect.modify_attribute(source_player=5, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=10 + int(listEquipments[b].statModify / 10),
                                                 operation=Operation.MULTIPLY)
            trigger1.new_effect.modify_attribute(source_player=5, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=10,
                                                 operation=Operation.DIVIDE)
        # modify armor melee/pierce armor
        if listEquipments[b].equipmentType == "Armor":
            armorType = 0
            shownArmor = -1
            if listEquipments[b].equipmentCategory == "meleeArmor":
                armorType = 4
                shownArmor = 48
            if listEquipments[b].equipmentCategory == "pierceArmor":
                armorType = 3
                shownArmor = 49
            # modify armor
            trigger1.new_effect.modify_attribute(source_player=1, object_attributes=8,  # armor
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 armour_attack_quantity=256 * armorType + listEquipments[b].statModify,
                                                 armour_attack_class=0, operation=2)
            trigger1.new_effect.modify_attribute(source_player=5, object_attributes=8,  # armor
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 armour_attack_quantity=256 * armorType + listEquipments[b].statModify,
                                                 armour_attack_class=0, operation=2)
            # modify shown armor
            trigger1.new_effect.none()
            trigger1.new_effect.modify_attribute(source_player=1, object_attributes=shownArmor,  # shown armor
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=listEquipments[b].statModify, operation=2)
            trigger1.new_effect.modify_attribute(source_player=5, object_attributes=shownArmor,  # shown armor
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=listEquipments[b].statModify, operation=2)
        # modify boots movement speed
        if listEquipments[b].equipmentType == "Boots":
            trigger1.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.MOVEMENT_SPEED,
                                                 # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100 + listEquipments[b].statModify,
                                                 operation=4)
            trigger1.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.MOVEMENT_SPEED,
                                                 # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100,
                                                 operation=5)
            trigger1.new_effect.none()
            trigger1.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.MOVEMENT_SPEED,
                                                 # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100 + listEquipments[b].statModify,
                                                 operation=4)
            trigger1.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.MOVEMENT_SPEED,
                                                 # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100,
                                                 operation=5)
        print("trigger 1 created")
        # add second trigger
        trigger2 = source_trigger_manager.add_trigger("Ueqing" + listEquipments[b].unitName + "-"
                                                      + listCharacters[a].unitName, enabled=0)
        trigger2.new_condition.timer(timer=2)
        trigger2.new_effect.activate_trigger(trigger_id=trigger2.trigger_id + 1)
        # add third trigger
        trigger3 = source_trigger_manager.add_trigger("Ueq" + listEquipments[b].equipmentType
                                                      + listEquipments[b].unitName + "-"
                                                      + listCharacters[a].unitName, enabled=0)
        print("trigger 3 created")
        # Condition 0
        trigger3.new_condition.timer(timer=2)
        # Condition 1: check if equipment is teleported back to inventory
        trigger3.new_condition.own_fewer_objects(source_player=3,
                                                 area_x1=equipArea[0][0], area_x2=equipArea[0][1],
                                                 area_y1=equipArea[1][0], area_y2=equipArea[1][1],
                                                 quantity=0, object_list=listEquipments[b].unitId)
        # condition 2: check if unequip unit is in the area
        trigger3.new_condition.objects_in_area(quantity=1, object_list=listEquipments[b].unitId, source_player=3,
                                               area_x1=453, area_x2=455,
                                               area_y1=474, area_y2=476)
        # Effect 0
        trigger3.new_effect.send_chat(source_player=1,
                                      message="<" + listEquipments[b].rarity + "><" + listEquipments[
                                          b].fullname + "> Unequipped from " + listCharacters[a].unitName + "!")
        # Effect 1 replace unit back to P1
        trigger3.new_effect.replace_object(object_list_unit_id=listEquipments[b].unitId,
                                           object_list_unit_id_2=listEquipments[b].unitId,
                                           source_player=3, target_player=1,
                                           area_x1=453, area_x2=455,
                                           area_y1=474, area_y2=476)
        # Effect: modify attribute back to base stat
        if listEquipments[b].equipmentType == "Weapon":
            # modify weapon bonus attack
            trigger3.new_effect.modify_attribute(source_player=1, object_attributes=9,  # attack
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 armour_attack_class=0,
                                                 armour_attack_quantity=256 * 3 + listEquipments[b].statModify,
                                                 operation=Operation.SUBTRACT)
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=9,  # attack
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 armour_attack_class=0,
                                                 armour_attack_quantity=256 * 3 + listEquipments[b].statModify,
                                                 operation=Operation.SUBTRACT)
            trigger3.new_effect.none()
            trigger3.new_effect.modify_attribute(source_player=1, object_attributes=9,  # attack
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 armour_attack_class=0,
                                                 armour_attack_quantity=256 * 4 + listEquipments[b].statModify,
                                                 operation=Operation.SUBTRACT)
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=9,  # attack
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 armour_attack_class=0,
                                                 armour_attack_quantity=256 * 4 + listEquipments[b].statModify,
                                                 operation=Operation.SUBTRACT)
            trigger3.new_effect.none()
            # modify shown attack
            trigger3.new_effect.modify_attribute(source_player=1, object_attributes=46,  # shown attack
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=listEquipments[b].statModify,
                                                 operation=Operation.SUBTRACT)
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=46,  # shown attack
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=listEquipments[b].statModify,
                                                 operation=Operation.SUBTRACT)
            # modify weapon range
            if listEquipments[b].weaponRange != 0:
                trigger3.new_effect.modify_attribute(source_player=1, object_attributes=12,  # max range
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100 + listEquipments[b].weaponRange,
                                                     operation=Operation.DIVIDE)
                trigger3.new_effect.modify_attribute(source_player=1, object_attributes=12,  # max range
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100,
                                                     operation=Operation.MULTIPLY)
                trigger3.new_effect.none()
                trigger3.new_effect.modify_attribute(source_player=5, object_attributes=12,  # max range
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100 + listEquipments[b].weaponRange,
                                                     operation=Operation.DIVIDE)
                trigger3.new_effect.modify_attribute(source_player=5, object_attributes=12,  # max range
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100,
                                                     operation=Operation.MULTIPLY)
            # modify weapon attack speed
            if listEquipments[b].weaponAttackSpeed != 0:
                trigger3.new_effect.modify_attribute(source_player=1, object_attributes=10,  # attack reload time
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100 + listEquipments[b].weaponAttackSpeed,
                                                     operation=Operation.MULTIPLY)
                trigger3.new_effect.modify_attribute(source_player=1, object_attributes=10,  # attack reload time
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100,
                                                     operation=Operation.DIVIDE)
                trigger3.new_effect.none()
                trigger3.new_effect.modify_attribute(source_player=5, object_attributes=10,  # attack reload time
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100 + listEquipments[b].weaponAttackSpeed,
                                                     operation=Operation.MULTIPLY)
                trigger3.new_effect.modify_attribute(source_player=5, object_attributes=10,  # attack reload time
                                                     object_list_unit_id=listCharacters[a].unitId,
                                                     quantity=100,
                                                     operation=Operation.DIVIDE)
        # modify headwear hitpoints
        if listEquipments[b].equipmentType == "Headwear":
            trigger3.new_effect.modify_attribute(source_player=1, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=10,
                                                 operation=Operation.MULTIPLY)
            trigger3.new_effect.modify_attribute(source_player=1, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=10 + int(listEquipments[b].statModify / 10),
                                                 operation=Operation.DIVIDE)
            trigger3.new_effect.none()
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=10,
                                                 operation=Operation.MULTIPLY)
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=10 + int(listEquipments[b].statModify / 10),
                                                 operation=Operation.DIVIDE)
            trigger3.new_effect.none()
            trigger3.new_effect.modify_attribute(source_player=1, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=1,
                                                 operation=Operation.ADD)
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=1,
                                                 operation=Operation.ADD)
        # modify armor melee/pierce armor
        if listEquipments[b].equipmentType == "Armor":
            armorType = 0
            shownArmor = -1
            if listEquipments[b].equipmentCategory == "meleeArmor":
                armorType = 4
                shownArmor = 48
            if listEquipments[b].equipmentCategory == "pierceArmor":
                armorType = 3
                shownArmor = 49
            # modify armor
            trigger3.new_effect.modify_attribute(source_player=1, object_attributes=8,  # armor
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 armour_attack_quantity=256 * armorType + listEquipments[b].statModify,
                                                 armour_attack_class=0, operation=Operation.SUBTRACT)
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=8,  # armor
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 armour_attack_quantity=256 * armorType + listEquipments[b].statModify,
                                                 armour_attack_class=0, operation=Operation.SUBTRACT)
            trigger3.new_effect.none()
            # modify shown armor
            trigger3.new_effect.modify_attribute(source_player=1, object_attributes=shownArmor,  # shown armor
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=listEquipments[b].statModify, operation=Operation.SUBTRACT)
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=shownArmor,  # shown armor
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=listEquipments[b].statModify, operation=Operation.SUBTRACT)
        # modify boots movement speed
        if listEquipments[b].equipmentType == "Boots":
            trigger3.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.MOVEMENT_SPEED,
                                                 # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100 + listEquipments[b].statModify,
                                                 operation=Operation.DIVIDE)
            trigger3.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.MOVEMENT_SPEED,
                                                 # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100,
                                                 operation=Operation.MULTIPLY)
            trigger3.new_effect.none()
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.MOVEMENT_SPEED,
                                                 # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100 + listEquipments[b].statModify,
                                                 operation=Operation.DIVIDE)
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.MOVEMENT_SPEED,
                                                 # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100,
                                                 operation=Operation.MULTIPLY)
        trigger3.new_effect.none()
        # temporarily changing ownership for characters in the equipment area,
        # then replace existing unit, then change them back again
        # p1
        trigger1P1 = source_trigger_manager.copy_trigger(trigger_select=trigger1.trigger_id)
        trigger1P1.name = "Eq" + listEquipments[b].equipmentType + listEquipments[b].unitName + "-" + listCharacters[
            a].unitName + "P1"
        trigger1P1.new_condition = NewConditionSupport(trigger1P1)
        trigger1P1.new_effect = NewEffectSupport(trigger1P1)
        trigger1P1.new_condition.capture_object(unit_object=listCharacters[a].coreUnitId, source_player=3)
        trigger1P1.new_effect.activate_trigger(trigger_id=trigger2.trigger_id)
        trigger1P1.new_effect.replace_object(object_list_unit_id=listCharacters[a].unitId,
                                             source_player=1, target_player=1,
                                             object_list_unit_id_2=602)
        trigger1P1.new_effect.replace_object(object_list_unit_id=602,
                                             source_player=1, target_player=1,
                                             object_list_unit_id_2=listCharacters[a].unitId)
        # p5
        trigger1P5 = source_trigger_manager.copy_trigger(trigger_select=trigger1.trigger_id, )
        trigger1P5.name = "Eq" + listEquipments[b].equipmentType + listEquipments[b].unitName + "-" + listCharacters[
            a].unitName + "P5"
        trigger1P5.new_condition = NewConditionSupport(trigger1P5)
        trigger1P5.new_effect = NewEffectSupport(trigger1P5)
        trigger1P5.new_condition.capture_object(unit_object=listCharacters[a].coreUnitId, source_player=1)
        trigger1P5.new_effect.activate_trigger(trigger_id=trigger2.trigger_id)
        trigger1P5.new_effect.replace_object(object_list_unit_id=listCharacters[a].unitId,
                                             source_player=5, target_player=5,
                                             object_list_unit_id_2=602)
        trigger1P5.new_effect.replace_object(object_list_unit_id=602,
                                             source_player=5, target_player=5,
                                             object_list_unit_id_2=listCharacters[a].unitId)
        source_trigger_manager.remove_trigger(trigger_select=trigger1.trigger_id)
        # add fourth trigger
        trigger4 = source_trigger_manager.add_trigger("------------")

triggerEnd = source_trigger_manager.add_trigger("equipment for ToT.py End")

# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)
