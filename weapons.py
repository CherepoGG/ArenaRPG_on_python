class BaseWeapons:
    def __init__(self):
        self.type_weapon = ['chopping', 'cutting', 'blunt', 'the_pole']  # рубящее, режущее, дробящее, древковое
        self.name = ''
        self.damage = 0
        self.type = ''


class WeaponInfo(BaseWeapons):
    base_weapons = BaseWeapons()

    def chopping_stats(self, base_weapons):
        if base_weapons.type_weapons == self.type_weapon[0]:
            self.type = self.type_weapon[0]
            self.name = 'Топор'
            self.damage = 4
        elif base_weapons.type_weapons == self.type_weapon[1]:
            self.type_weapon = self.type_weapon[1]
            self.name = 'Меч'
            self.damage = 6
        elif base_weapons.type_weapons == self.type_weapon[2]:
            self.type_weapon = self.type_weapon[2]
            self.name = 'Молот'
            self.damage = 8
        elif base_weapons.type_weapons == self.type_weapon[3]:
            self.type_weapon = self.type_weapon[3]
            self.name = 'Копье'
            self.damage = 10

