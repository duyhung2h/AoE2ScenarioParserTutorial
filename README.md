# AoE2ScenarioParserTutorial
These are examples scripts that you can use for AoE2ScenarioParser, made by duyhung2h. Follow and subscribe to my channel for more Scenario Tricks!
## Step by step

### 1. Create the scenario
Create an empty scenario in the editor and save it as "YourScenarioFilename"
### 2. Setup the project
Create a new project or file (in PyCharm). Or easiest, open the `example - Template.py` in this repository in PyCharm, the example code is shown below:
```
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *


# File & Folder setup - Declare your scenario directory path
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
input_path = scenario_folder + "YourScenarioFilename.aoe2scenario"
output_path = scenario_folder + "YourScenarioFilename Parser Result.aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# Start writing your code here:
# ...
# ...


# Final step: write a modified scenario class to a new scenario file
source_scenario.write_to_file(output_path)
```

Your scenario `YourScenarioFilename.aoe2scenario` will be read by the parser provided that you have given a proper link to your scenario folder. Watch the video for more info. 
After that, it will save and write as a new file in the final step of the parser.

I will explain how this script works by introducing it in proper steps:

First, you need to. After installing the parser successfully, you need to declare imports to use the parser:
```
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
```
Also, it is recommended to pair with an additional dataset library import that you can use for many different things, such as importing unit IDs, etc. These are essential to producing a scenario. Read more about them [here](https://ksneijders.github.io/AoE2ScenarioParser/cheatsheets/datasets/).
```
from AoE2ScenarioParser.datasets.trigger_lists import *
```
After you're done with import, now you can properly read your scenario file! You need to assign a string to your 
```
# File & Folder setup - Declare your scenario directory path
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
input_path = scenario_folder + "YourScenarioFilename.aoe2scenario"
output_path = scenario_folder + "YourScenarioFilename Parser Result.aoe2scenario"
```

To work with your scenario trigger, first you declare your trigger manager like so (already provided in `example - Template.py`):
```

```
