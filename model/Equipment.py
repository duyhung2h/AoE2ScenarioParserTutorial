class Equipment:
    def __init__(self, unitName, fullname, unitId, statModify, equipmentType, equipmentCategory, rarity):
        self.unitName = unitName
        self.fullname = fullname
        self.unitId = unitId
        self.statModify = statModify
        self.equipmentType = equipmentType
        self.equipmentCategory = equipmentCategory
        self.rarity = rarity

    def get_equipment():
        return [
            Equipment('LA', "Leather Armor", 232, 1, "Armor", "meleeArmor", "GREEN"),  # Woad Raider
            Equipment('HA', "Hide Armor", 534, 2, "Armor", "meleeArmor", "BLUE"),  # Elite Woad Raider
            Equipment('TB', "Tattered Boots", 448, 10, "Boots", "n/a", "GREEN"),  # Scout Cav
            Equipment('LB', "Leather Boots", 546, 20, "Boots", "n/a", "BLUE"),  # Light Cav
            Equipment('HB', "Headband", 825, 10, "Headwear", "n/a", "GREEN"),  # Amazon Warrior
            Equipment('LC', "Leather Cap", 725, 20, "Headwear", "n/a", "BLUE"),  # Jaguar Warrior

            Equipment('PCA', "Plain Cloth Armor", 7, 1, "Armor", "pierceArmor", "GREEN"),  # Skirmisher
            Equipment('PA', "Padded Armor", 6, 2, "Armor", "pierceArmor", "BLUE"),  # Elite Skirmisher
        ]
