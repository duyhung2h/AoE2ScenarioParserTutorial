from .Equipment import Equipment


class Weapon(Equipment):
    def __init__(self, weaponRange, weaponAttackSpeed, *args, **kwargs):
        super(Weapon, self).__init__(*args, **kwargs)
        self.weaponRange = weaponRange
        self.weaponAttackSpeed = weaponAttackSpeed

    def get_weapon():
        return [
            Weapon(0, 0, 'CC', "Crude Club", 74, 1, "Weapon", "sword", "GREEN"),  # Militia
            Weapon(0, 0, 'SC', "Spiked Club", 299, 2, "Weapon", "sword", "BLUE"),  # Bandit
            Weapon(10, 0, 'CB', "Crude Bow", 4, 1, "Weapon", "bow", "GREEN"),  # Archer
            Weapon(10, 20, 'SB', "Short Bow", 850, 1, "Weapon", "bow", "BLUE"),  # Amazon Archer
            Weapon(0, 0, 'WK', "Wooden Knife", 1123, 1, "Weapon", "dagger", "GREEN"),  # karambit warrior
            Weapon(0, 0, 'KK', "Kitchen Knife", 1125, 2, "Weapon", "dagger", "BLUE"),  # elite karambit warrior
            Weapon(0, 0, 'SS', "Shepherd's Stick", 185, 1, "Weapon", "staff", "GREEN"),  # Slinger
            Weapon(0, 0, 'OS', "Old Staff", 1023, 2, "Weapon", "staff", "BLUE"),  # Priest

            Weapon(100, -20, 'WoLD', "Wrath of Long Dong", 1574, 4, "Weapon", "sword", "ORANGE"),  # Sosso Guard
        ]
