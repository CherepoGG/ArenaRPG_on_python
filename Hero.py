from Inventory import Inventory

from EquipmentHero import Equipment


class Hero:
    def __init__(self):
        self.name = 'Richard'
        self.max_hp = 50
        self.hp = self.max_hp
        self.lvl = 1
        self.exp = 0
        self._expForLvlUp = 30
        self.damage = 10
        self.atk = ''
        self.defend = ''
        self.inventory = Inventory()
        self.equipment = Equipment()

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

    def _add_experience(self, count):
        self.exp += count
        print('Получено опыта:', self.exp)
        self._check_lvl_up()

    def _add_item(self, item):
        self.inventory.add_item(item)

    # def _delete_item(self):
    #     self.inventory.delete_item()

    def reward(self, exp_reward, item):
        self._add_experience(exp_reward)
        self._add_item(item)
        print('Получен предмет:', item)

    def equip_item(self, item, player):
        if item.type == 'weapon':
            self.equipment.weapon = item
            self.inventory.delete_item(player)
        elif item.type == 'armor':
            self.equipment.armor = item
            self.inventory.delete_item(player)

    def remove_item(self, item):  # Будет кнопка, вызывающая эту функцию напротив каждого предмета экипировки
        if item == self.equipment.armor:
            self.equipment.armor = 'Не надето'
            self.inventory.inventory.append(item)
        elif item == self.equipment.weapon:
            self.equipment.weapon = 'Не надето'
            self.inventory.inventory.append(item)

    def restore_hero(self):
        self.hp = self.max_hp
