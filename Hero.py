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

    def equip_item(self, item):
        if item.type == 'weapon':
            self.equipment.weapon = item
            self.inventory.delete_item(item)
        elif item.type == 'armor':
            if item.part == 'head':
                self.equipment.head = item
                self.inventory.delete_item(item)
            elif item.part == 'body':
                self.equipment.body = item
                self.inventory.delete_item(item)
            elif item.part == 'arms':
                self.equipment.arms = item
                self.inventory.delete_item(item)
            elif item.part == 'legs':
                self.equipment.legs = item
                self.inventory.delete_item(item)

    def remove_item(self, item):  # Будет кнопка, вызывающая эту функцию напротив каждого предмета экипировки
        if item.type == 'armor':
            if item == self.equipment.head:
                self.equipment.head = ''
                self.inventory.add_item(item)
            elif item == self.equipment.body:
                self.equipment.body = ''
                self.inventory.add_item(item)
            elif item == self.equipment.arms:
                self.equipment.arms = ''
                self.inventory.add_item(item)
            elif item == self.equipment.legs:
                self.equipment.legs = ''
                self.inventory.add_item(item)
        elif item == self.equipment.weapon:
            self.equipment.weapon = ''
            self.inventory.add_item(item)

    def calculate_damage_by_armor(self, body_part, damage):
        if body_part == 'head' and self.equipment.head:
            damage -= damage / 100 * self.equipment.head.defence
            print(damage)
            return damage
        elif body_part == 'body' and self.equipment.body:
            damage -= damage / 100 * self.equipment.body.defence
            print(damage)
            return damage
        elif body_part == 'arms' and self.equipment.arms:
            damage -= damage / 100 * self.equipment.arms.defence
            print(damage)
            return damage
        elif body_part == 'legs' and self.equipment.legs:
            damage -= damage / 100 * self.equipment.legs.defence
            print(damage)
            return damage
        return damage
