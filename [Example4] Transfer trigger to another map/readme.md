# How to transfer trigger to another map
This is a tutorial on how to transfer trigger to another map: Copy triggers from `source_scenario` and add them to `transfer_scenario` trigger list, then write a new file named "ScenarioParser - TransferTriggers Parser Result.aoe2scenario"
## Step by step
```
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
```
### 1. Create your scenario
Use the scenario provided in the example folder:
 - Source scenario called `ScenarioParser - TransferTriggers.aoe2scenario`, or change the `input_path` to your scenario name.
 - Transfer scenario called `ScenarioParser - TransferTriggers Transfer.aoe2scenario`, or change the `transfer_path` to your scenario name.
### 2. Copy triggers from `source_scenario` and add them to `transfer_scenario` trigger 

![image](https://user-images.githubusercontent.com/40296674/161375045-7dc42fab-d0f6-445d-b164-af747fee9b4a.png)

To transfer trigger between scenarioes, unlike other examples, in this one you need 2 scenarioes: `source_scenario` that contains triggers needed to be transferred and `transfer_scenario` which is the map to be getting the newly copied and transferred triggers.

You can simply choose a range to copy the triggers, or leave the variables `position_start`, `position_end` and `position_transfer` unchanged to copy all the triggers from start to end and paste them at the end of the transfer map. 

```
    position_start = 0;
    position_end = source_trigger_manager.triggers.__len__();
    position_transfer = -1; #Leaving it out (or -1) is placing your triggers at the end
```

To wipe all the `transfer_scenario` triggers or variables at first simply uncomment these two lines below `shortcut in PyCharm: CTRL + /`(ill-advised)

```
    # target_trigger_manager.triggers = []  # Uncomment this in order to wipe all triggers from the map at start
    # target_trigger_manager.variables = []  # Uncomment this in order to wipe all variables from the map at start
```

And so, simply transfer the triggers by using `import_triggers` from your transfer map's `trigger_manager`:

```
    transfer_trigger_manager.import_triggers(triggers=source_trigger_manager.triggers[position_start:position_end], index=position_transfer);
```



There are a lot more examples, and this is just one of them. Check the main library to [learn more](https://github.com/KSneijders/AoE2ScenarioParser)

