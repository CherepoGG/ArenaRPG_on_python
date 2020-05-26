from Inventory import Inventory

from Equipment import Equipment

from rewards import Rewards


class Hero:
    def __init__(self):
        self.name = 'Richard'
        self.max_hp = 50
        self.hp = self.max_hp
        self.lvl = 1
        self.exp = 0
        self._expForLvlUp = 30
        self.damage = 10
        self.defence = 0
        self.atk = ''
        self.defend = ''
        self.inventory = Inventory()
        self.equipment = Equipment()
        self.gold = 0

    def attack(self, enemy):
        enemy.hp -= self.damage

    def _check_lvl_up(self):
        if self.exp >= self._expForLvlUp:
            self.exp -= self._expForLvlUp
            self.lvl += 1
            self._expForLvlUp = self._expForLvlUp * 2
            self.max_hp += 10
            self.hp = self.max_hp
            self.damage += 5
            print('Уровень повышен! Теперь ваш уровень:', self.lvl, 'урон:', self.damage, 'здоровье:', self.max_hp)

    def restore_hero(self):
        self.hp = self.max_hp

    rewards = Rewards()
