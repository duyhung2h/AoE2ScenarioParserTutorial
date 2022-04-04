import math
from typing import Union

# from unit_manager import SPTUnitManager
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario


class SPTUnitManager:
    def __init__(self, scenario, direction, old_map_size, new_map_size):
        self.scenario = scenario
        self.direction = direction
        self.old_map_size = old_map_size
        self.new_map_size = new_map_size

    def new_unit(self,
                 scenario: Union[AoE2DEScenario, None] = None,
                 direction: Union[str, None] = None,
                 old_map_size: Union[int, None] = None,
                 new_map_size: Union[int, None] = None,
                 ) -> None:
        return self(
            scenario=scenario,
            direction=direction,
            old_map_size=old_map_size,
            new_map_size=new_map_size,
        )

    def move_unit(self):
        for unit in self.scenario.unit_manager.get_all_units():
            if self.direction == "E":
                if unit.x > self.new_map_size or unit.y > self.new_map_size:
                    print("Out of bound unit removed!" + str(unit))
                    self.scenario.unit_manager.remove_unit(unit=unit)
                else:
                    print()
            if self.direction == "W":
                if unit.x < (self.old_map_size - self.new_map_size) or unit.y < (self.old_map_size - self.new_map_size):
                    print("Out of bound unit removed!" + str(unit))
                    self.scenario.unit_manager.remove_unit(unit=unit)
                else:
                    print()
                    unit.x = unit.x + (self.new_map_size - self.old_map_size)
                    unit.y = unit.y + (self.new_map_size - self.old_map_size)
            if self.direction == "N":
                if unit.x < -(self.new_map_size - self.old_map_size) or unit.y > self.new_map_size:
                    print()
                    # print("Out of bound unit removed!" + str(unit))
                    # self.scenario.unit_manager.remove_unit(unit=unit)
                else:
                    unit.y = unit.y + (self.new_map_size - self.old_map_size)
    def move_triggers(self):
        if self.direction == "W" or self.direction == "N" or self.direction == "S":
            for trigger in self.scenario.trigger_manager.triggers:
                for effect in trigger.effects:
                    if effect.location_x > -1:
                        if self.direction != "N":
                            effect.location_x = int(
                                effect.location_x + (self.new_map_size - self.old_map_size))
                        effect.location_y = int(
                            effect.location_y + (self.new_map_size - self.old_map_size))
                    if effect.area_x1 > -1:
                        if self.direction != "N":
                            effect.area_x1 = int(
                                effect.area_x1 + (self.new_map_size - self.old_map_size))
                            effect.area_x2 = int(
                                effect.area_x2 + (self.new_map_size - self.old_map_size))
                        effect.area_y1 = int(
                            effect.area_y1 + (self.new_map_size - self.old_map_size))
                        effect.area_y2 = int(
                            effect.area_y2 + (self.new_map_size - self.old_map_size))
                for condition in trigger.conditions:
                    if condition.area_x1 > -1:
                        if self.direction != "N":
                            condition.area_x1 = int(
                                condition.area_x1 + (self.new_map_size - self.old_map_size))
                            condition.area_x2 = int(
                                condition.area_x2 + (self.new_map_size - self.old_map_size))
                        condition.area_y1 = int(
                            condition.area_y1 + (self.new_map_size - self.old_map_size))
                        condition.area_y2 = int(
                            condition.area_y2 + (self.new_map_size - self.old_map_size))
    def extend_map_iteration1(self):
        if self.direction == "W" or self.direction == "S":
            self.scenario.map_manager.terrain.reverse()
        if self.direction != "N":
            self.source_scenario.map_manager.map_size = self.new_map_size
            self.scenario.map_manager.terrain.reverse()
        if self.direction == "N" and self.new_map_size > self.old_map_size:
            self.source_scenario.map_manager.map_size = self.new_map_size
        if self.direction == "N" and self.new_map_size < self.old_map_size:
            self.source_scenario.map_manager.map_size = self.old_map_size+(self.old_map_size-self.new_map_size)
    def extend_map_iteration2(self):
        if self.direction == "W":
            self.scenario.map_manager.terrain.reverse()
        if self.direction == "N" and self.new_map_size > self.old_map_size:
            for terrainId in range(0, (self.new_map_size-self.old_map_size)*self.new_map_size, 1):
                print("transfer")
                self.scenario.map_manager.terrain.insert(
                    0, self.scenario.map_manager.terrain.pop(self.scenario.map_manager.terrain.__len__()-1))
        if self.direction == "N" and self.new_map_size < self.old_map_size:
            for terrainId in range(0, math.sqrt((self.old_map_size + (self.old_map_size-self.new_map_size))), 1):
                print("transfer")
                self.scenario.map_manager.terrain.insert(
                    0, self.scenario.map_manager.terrain.pop(self.scenario.map_manager.terrain.__len__()-1))