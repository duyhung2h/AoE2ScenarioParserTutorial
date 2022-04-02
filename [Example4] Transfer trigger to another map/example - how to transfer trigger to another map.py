from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

# File & Folder setup - Declare your scenario directory path
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
input_path = scenario_folder + "ScenarioParser - TransferTriggers.aoe2scenario"
transfer_path = scenario_folder + "ScenarioParser - TransferTriggers Transfer.aoe2scenario"
output_path = scenario_folder + "ScenarioParser - TransferTriggers Parser Result.aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)
transfer_scenario = AoE2DEScenario.from_file(transfer_path)


# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager
transfer_trigger_manager = transfer_scenario.trigger_manager

# target_trigger_manager.triggers = []  # Uncomment this in order to wipe all triggers from the map at start
# target_trigger_manager.variables = []  # Uncomment this in order to wipe all variables from the map at start


# put triggers ranging from index position_start to position_end, to position position_transfer in the target file
position_start = 0;
position_end = source_trigger_manager.triggers.__len__();
position_transfer = -1; #Leaving it out (or -1) is placing your triggers at the end

# Mark the start of trigger copying!
transfer_trigger_manager.add_trigger(name="---TRIGGER COPY START-----")

# transfer the triggers and variables
# (source_trigger_manager.triggers[position_start:position_end]) to get list of triggers from start to end
transfer_trigger_manager.import_triggers(triggers=source_trigger_manager.triggers[position_start:position_end], index=position_transfer);

# Final step: write a modified scenario class to a new scenario file
transfer_scenario.write_to_file(filename=output_path)