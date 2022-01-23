from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *

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
position_start = 415
position_end = 419
# Leaving it out (or -1) is placing your triggers at the end
position_transfer = -1

# working with triggers
triggers = source_trigger_manager.triggers[position_start:position_end]


# [x1, x2], [y1, y2]
listCharactersEquipmentArea = [
    EquipmentArea([[43, 45], [476, 478]], [[47, 49], [476, 478]], [[51, 53], [476, 478]], [[55, 57], [476, 478]]),
    EquipmentArea([[23, 25], [476, 478]], [[27, 29], [476, 478]], [[31, 33], [476, 478]], [[35, 37], [476, 478]]),
    EquipmentArea([[3, 5], [476, 478]], [[7, 9], [476, 478]], [[11, 13], [476, 478]], [[15, 17], [476, 478]]),
    EquipmentArea([[43, 45], [468, 470]], [[47, 49], [468, 470]], [[51, 53], [468, 470]], [[55, 57], [468, 470]]),
    EquipmentArea([[23, 25], [468, 470]], [[27, 29], [468, 470]], [[31, 33], [468, 470]], [[35, 37], [468, 470]]),
    EquipmentArea([[3, 5], [468, 470]], [[7, 9], [468, 470]], [[11, 13], [468, 470]], [[15, 17], [468, 470]]),
]
print(listCharactersEquipmentArea[0].weaponArea[0][0])  # x1
print(listCharactersEquipmentArea[0].weaponArea[1][0])  # y1
print(listCharactersEquipmentArea[0].weaponArea[0][1])  # x2
print(listCharactersEquipmentArea[0].weaponArea[1][1])  # y2
listCharacters = [
    Character('Charles', 439, "warrior", 136167),
    Character('Coline', 1066, "rogue", 136180),
    Character('Nemunas', 1069, "ranger", 169037),
    Character('Dominiel', 430, "soulweaver", 136179),
    Character('Corvus', 1683, "warrior", 168727),
]
listEquipments = [
    Equipment('LA', "Leather Armor", 232, 1, "Armor", "meleeArmor", "GREEN"),  # Woad Raider
    Equipment('HA', "Hide Armor", 534, 2, "Armor", "meleeArmor", "BLUE"),  # Elite Woad Raider
    Equipment('TB', "Tattered Boots", 448, 10, "Boots", "n/a", "GREEN"),  # Scout Cav
    Equipment('LB', "Leather Boots", 546, 20, "Boots", "n/a", "BLUE"),  # Light Cav
    Equipment('HB', "Headband", 825, 10, "Headwear", "n/a", "GREEN"),  # Amazon Warrior
    Equipment('LC', "Leather Cap", 725, 20, "Headwear", "n/a", "BLUE"),  # Jaguar Warrior

    Weapon(0, 0, 'CC', "Crude Club", 74, 1, "Weapon", "sword", "GREEN"),    # Militia
    Weapon(0, 0, 'SC', "Spiked Club", 299, 2, "Weapon", "sword", "BLUE"),   # Bandit
    Weapon(10, 0, 'CB', "Crude Bow", 4, 1, "Weapon", "bow", "GREEN"),    # Archer
    Weapon(10, 20, 'SB', "Short Bow", 850, 1, "Weapon", "bow", "BLUE"),  # Amazon Archer

    Weapon(100, -20, 'WoLD', "Wrath of Long Dong", 1574, 4, "Weapon", "sword", "ORANGE"),   # Sosso Guard

    Weapon(0, 0, 'SS', "Shepherd's Stick", 185, 1, "Weapon", "staff", "GREEN"),    # Slinger
    Weapon(0, 0, 'OS', "Old Staff", 1023, 2, "Weapon", "staff", "BLUE"),  # Priest

    Equipment('PCA', "Plain Cloth Armor", 7, 1, "Armor", "pierceArmor", "GREEN"),  # Skirmisher
    Equipment('PA', "Padded Armor", 6, 2, "Armor", "pierceArmor", "BLUE"),  # Elite Skirmisher
]
print(vars(listEquipments[9]))

# run for each character
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
                                                      + listCharacters[a].unitName, enabled=1, looping=1)
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
        trigger1.new_effect.activate_trigger(trigger_id=trigger1.trigger_id + 1)
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
                prefixStatMessage = prefixStatMessage + "\nPrefix stat: [" + str(100 + listEquipments[b].weaponRange) + "% attack range]"
            if listEquipments[b].weaponAttackSpeed != 0:
                prefixStatMessage = prefixStatMessage + "\nPrefix stat: [" + str(100 + listEquipments[b].weaponAttackSpeed) + "% attack speed]"
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
                                                 message="<" + listEquipments[b].rarity + "><" + listEquipments[b].fullname + "> Equipped to " + listCharacters[a].unitName + "! \n\n"
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
                                                 quantity=100,
                                                 operation=5)
            trigger1.new_effect.modify_attribute(source_player=1, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100 + listEquipments[b].statModify,
                                                 operation=4)
            trigger1.new_effect.none()
            trigger1.new_effect.modify_attribute(source_player=5, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100,
                                                 operation=5)
            trigger1.new_effect.modify_attribute(source_player=5, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100 + listEquipments[b].statModify,
                                                 operation=4)
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
            trigger1.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.MOVEMENT_SPEED,  # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100 + listEquipments[b].statModify,
                                                 operation=4)
            trigger1.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.MOVEMENT_SPEED,  # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100,
                                                 operation=5)
            trigger1.new_effect.none()
            trigger1.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.MOVEMENT_SPEED,  # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100 + listEquipments[b].statModify,
                                                 operation=4)
            trigger1.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.MOVEMENT_SPEED,  # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100,
                                                 operation=5)

        # add second trigger
        trigger2 = source_trigger_manager.add_trigger("Ueqing" + listEquipments[b].unitName + "-"
                                                      + listCharacters[a].unitName, enabled=0)
        trigger2.new_condition.timer(timer=2)
        trigger2.new_effect.activate_trigger(trigger_id=trigger2.trigger_id + 1)
        # add third trigger
        trigger3 = source_trigger_manager.add_trigger("Ueq" + listEquipments[b].equipmentType
                                                      + listEquipments[b].unitName + "-"
                                                      + listCharacters[a].unitName, enabled=0)
        # Condition 0
        trigger3.new_condition.timer(timer=2)
        # Condition 1: check if equipment is teleported back to inventory
        trigger3.new_condition.own_fewer_objects(source_player=3,
                                                 area_x1=equipArea[0][0], area_x2=equipArea[0][1],
                                                 area_y1=equipArea[1][0], area_y2=equipArea[1][1],
                                                 quantity=0, object_list=listEquipments[b].unitId)
        # Effect 0
        trigger3.new_effect.send_chat(source_player=1,
                                      message="<" + listEquipments[b].rarity + "><" + listEquipments[b].fullname + "> Unequipped from " + listCharacters[a].unitName + "!")
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
                                                 quantity=100 + listEquipments[b].statModify,
                                                 operation=Operation.DIVIDE)
            trigger3.new_effect.modify_attribute(source_player=1, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100,
                                                 operation=Operation.MULTIPLY)
            trigger3.new_effect.none()
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100 + listEquipments[b].statModify,
                                                 operation=Operation.DIVIDE)
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=0,  # hitpoints
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100,
                                                 operation=Operation.MULTIPLY)
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
            trigger3.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.MOVEMENT_SPEED,  # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100 + listEquipments[b].statModify,
                                                 operation=Operation.DIVIDE)
            trigger3.new_effect.modify_attribute(source_player=1, object_attributes=ObjectAttribute.MOVEMENT_SPEED,  # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100,
                                                 operation=Operation.MULTIPLY)
            trigger3.new_effect.none()
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.MOVEMENT_SPEED,  # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100 + listEquipments[b].statModify,
                                                 operation=Operation.DIVIDE)
            trigger3.new_effect.modify_attribute(source_player=5, object_attributes=ObjectAttribute.MOVEMENT_SPEED,  # movement speed
                                                 object_list_unit_id=listCharacters[a].unitId,
                                                 quantity=100,
                                                 operation=Operation.MULTIPLY)
        trigger3.new_effect.none()
        # add fourth trigger
        trigger4 = source_trigger_manager.add_trigger("------------")


# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)
