class Character:
    def __init__(self, unitName, unitId, characterClass, coreUnitId, skill1Icon, skill2Icon, maxRange, projectileId, hp,
                 atk, meleeArmor, pierceArmor, potraitId):
        self.unitName = unitName
        self.unitId = unitId
        self.characterClass = characterClass
        self.coreUnitId = coreUnitId
        self.skill1Icon = skill1Icon
        self.skill2Icon = skill2Icon
        self.maxRange = maxRange
        self.projectileId = projectileId
        self.hp = hp
        self.atk = atk
        self.meleeArmor = meleeArmor
        self.pierceArmor = pierceArmor
        self.potraitId = potraitId

    def get_characters():
        return [
            Character('Charles', 439, "warrior", 136167, 281, 276, 0, 187, 50, 3, 3, 1, 162),
            Character('Coline', 1066, "rogue", 136180, 277, 278, 0, 187, 30, 5, 2, 2, 216),
            Character('Nemunas', 1069, "ranger", 169037, 279, 277, 4, 511, 30, 5, 0, 3, 314),
            Character('Dominiel', 430, "soulweaver", 136179, 276, 280, 3, 369, 40, 4, 1, 3, 52),
            Character('Corvus', 1683, "warrior", 168727, 281, 276, 0, 187, 40, 4, 3, 1, 368),
        ]
