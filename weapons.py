class BaseWeapons:
    def __init__(self):
        self.type_weapon = ['chopping', 'cutting', 'blunt', 'the_pole']  # рубящее, режущее, дробящее, древковое
        self.name = ''
        self.damage = 0
        self.type = ''


class WeaponInfo(BaseWeapons):

    def chopping_stats(self, weapon):
        if weapon == 'Топор':
            self.type = self.type_weapon[0]
            self.name = 'Топор'
            self.damage = 4
        if weapon == 'Меч':
            self.type_weapon = self.type_weapon[1]
            self.name = 'Меч'
            self.damage = 6
        if weapon == 'Молот':
            self.type_weapon = self.type_weapon[2]
            self.name = 'Молот'
            self.damage = 8
        if weapon == 'Копье':
            self.type_weapon = self.type_weapon[3]
            self.name = 'Копье'
            self.damage = 10
        return self.name
