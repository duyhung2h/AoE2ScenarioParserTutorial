import sys
import os
import time
from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
import re
from AoE2ScenarioParser.datasets.trigger_lists import *
from AoE2ScenarioParser.datasets.conditions import ConditionId
from AoE2ScenarioParser.datasets.effects import EffectId
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
Tales of Tenebria version 0v18v54
Tales of Tenebria version 0v18v3 Parser Result
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

# print out highest trigger id
highest_trigger_id = len(source_trigger_manager.triggers) - 1
print("higest trigger id: " + str(highest_trigger_id))

searching_trigger = False
searching_trigger = True # (comment this line out if it's unneeded) search a trigger by its name
'''
Copy the trigger name (click on the line and CTRL + C):

1236
0--CINEMATIC MAIN------------------------------
1394
--AMBIENCE: LARRAU---------------
1510
-----Scene 5---------------
'''
if searching_trigger:
    searching_trigger_name = input("Enter trigger name that you want to search its index: ")
    for trigger in source_trigger_manager.triggers:
        if trigger.name == searching_trigger_name:
            print(trigger.trigger_id)

# fetch list of triggers
fetched_trigger_list = []

triggerStart = 0
triggerEnd = 0
# type in range of trigger index
while(True):
    try:
        triggerStart = int(input("Enter first trigger index: "))
        if triggerStart < 0:
            raise BufferError
        if triggerStart > highest_trigger_id:
            raise BrokenPipeError
        triggerEnd = int(input("Enter last trigger index: "))
        if triggerEnd < 0:
            raise BufferError
        if triggerEnd > highest_trigger_id:
            raise BrokenPipeError
        break
    except ValueError:
        print("index must be of integer value!")
    except BrokenPipeError:
        print("first/last trigger index cannot be higher than highest trigger id!")
    except BufferError:
        print("first/last trigger index cannot be lower than 0!")

fetched_trigger_list = source_trigger_manager.triggers[triggerStart: triggerEnd]
# print(fetched_trigger_list)
# print(source_trigger_manager.triggers[triggerStart])
# print(source_trigger_manager.triggers[triggerEnd])

# start modifying trigger (write your own code)
# example: modify all triggers that marked with [ ] at the top of their name

'''
for trigger in fetched_trigger_list:
    regex = "(\[\w\]).+"
    if re.search(regex, trigger.name):
        print(str(trigger.trigger_id) + ": " + trigger.name)
        # Get existing conditions (check if it existed)
        add_condition = True
        for condition in trigger.conditions:
            print("condition name: " + str(condition.condition_type) + " | quantity: " + str(condition.quantity) + " | variable: " + str(condition.variable))
            if condition.condition_type == ConditionId.VARIABLE_VALUE and condition.variable == 36:
                if condition.quantity == 0:
                    add_condition = False
        # add condition
        if add_condition:
            trigger.new_condition.variable_value(variable=36, quantity=0)
        # trigger.new_effect()
'''

# example: Find all trigger with short description

'''
for trigger in fetched_trigger_list:
    if trigger.short_description != "":
        print(str(trigger.trigger_id) + ": " + trigger.name)
        print("Trigger short description:" + trigger.short_description)
'''

# example: Find all trigger with activate trigger to a certain id


for trigger in fetched_trigger_list:
    for effect in trigger.effects:
        if effect.effect_type == EffectId.ACTIVATE_TRIGGER:
            if effect.trigger_id == 1614:  # insert id here
                print("ID: " + str(trigger.trigger_id) + ", Trigger name: " + trigger.name)


# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)
