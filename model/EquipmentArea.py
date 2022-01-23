class EquipmentArea:
    def __init__(self, bootsArea, armorArea, headwearArea, weaponArea):
        self.bootsArea = bootsArea
        self.armorArea = armorArea
        self.headwearArea = headwearArea
        self.weaponArea = weaponArea

    def get_equipmentarea():
        return [
            EquipmentArea([[43, 45], [476, 478]], [[47, 49], [476, 478]], [[51, 53], [476, 478]],
                          [[55, 57], [476, 478]]),
            EquipmentArea([[23, 25], [476, 478]], [[27, 29], [476, 478]], [[31, 33], [476, 478]],
                          [[35, 37], [476, 478]]),
            EquipmentArea([[3, 5], [476, 478]], [[7, 9], [476, 478]], [[11, 13], [476, 478]], [[15, 17], [476, 478]]),
            EquipmentArea([[43, 45], [468, 470]], [[47, 49], [468, 470]], [[51, 53], [468, 470]],
                          [[55, 57], [468, 470]]),
            EquipmentArea([[23, 25], [468, 470]], [[27, 29], [468, 470]], [[31, 33], [468, 470]],
                          [[35, 37], [468, 470]]),
            EquipmentArea([[3, 5], [468, 470]], [[7, 9], [468, 470]], [[11, 13], [468, 470]], [[15, 17], [468, 470]]),
        ]
