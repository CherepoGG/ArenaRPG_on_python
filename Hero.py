from Inventory import Inventory

from Equipment import Equipment

from Rewards import Rewards


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

    def restore_hero(self):  # TODO: можно использовать для будущего лазарета
        self.hp = self.max_hp

    rewards = Rewards()

    def equip_item(self, item):
        if item.type == 'weapon':
            self.equipment.weapon = item
            self.inventory.delete_item(item)
            print('Вы надели предмет:', item)
        elif item.type == 'armor':
            if item.part == 'head':
                self.equipment.head = item
                self.inventory.delete_item(item)
                print('Вы надели предмет:', item)
            elif item.part == 'body':
                self.equipment.body = item
                self.inventory.delete_item(item)
                print('Вы надели предмет:', item)
            elif item.part == 'arms':
                self.equipment.arms = item
                self.inventory.delete_item(item)
                print('Вы надели предмет:', item)
            elif item.part == 'legs':
                self.equipment.legs = item
                self.inventory.delete_item(item)
                print('Вы надели предмет:', item)

    def check_slot_equipment(self, current_item):
        if current_item.type == 'armor':
            if current_item.part == 'head':
                if self.equipment.head != '':
                    return self.equipment.head
                elif self.equipment.head == '':
                    return 0
            elif current_item.part == 'body':
                if self.equipment.body != '':
                    return self.equipment.body
                elif self.equipment.body == '':
                    return 0
            elif current_item.part == 'arms':
                if self.equipment.arms != '':
                    return self.equipment.arms
                elif self.equipment.arms == '':
                    return 0
            elif current_item.part == 'legs':
                if self.equipment.legs != '':
                    return self.equipment.legs
                elif self.equipment.legs == '':
                    return 0
        elif current_item.type == 'weapon':
            if self.equipment.weapon != '':
                return self.equipment.weapon
            elif self.equipment.weapon == '':
                return 0

    def equip_and_replace_equip(self, current_item):
        equipment_item = self.check_slot_equipment(current_item)
        if equipment_item == 0:
            self.equip_item(current_item)
        elif equipment_item != 0:
            self.remove_item(equipment_item)
            self.equip_item(current_item)

    def remove_item(self, item):
        if item.type == 'armor':
            if item == self.equipment.head:
                self.equipment.head = ''
                self.inventory.add_item(item)
                print('Вы сняли предмет:', item)
            elif item == self.equipment.body:
                self.equipment.body = ''
                self.inventory.add_item(item)
                print('Вы сняли предмет:', item)
            elif item == self.equipment.arms:
                self.equipment.arms = ''
                self.inventory.add_item(item)
                print('Вы сняли предмет:', item)
            elif item == self.equipment.legs:
                self.equipment.legs = ''
                self.inventory.add_item(item)
                print('Вы сняли предмет:', item)
        elif item == self.equipment.weapon:
            self.equipment.weapon = ''
            self.inventory.add_item(item)
            print('Вы сняли предмет:', item)

    def calculate_stats(self, stat):
        if stat == 'damage':
            damage = self.damage + self.equipment.weapon
            return damage
        elif stat == 'armor':
            head = 0
            body = 0
            arms = 0
            legs = 0
            if self.equipment.head:
                head = self.equipment.head.defence
            if self.equipment.body:
                body = self.equipment.body.defence
            if self.equipment.arms:
                arms = self.equipment.arms.defence
            if self.equipment.legs:
                legs = self.equipment.legs.defence
            return self.defence + head + body + arms + legs

    def calculate_damage_by_armor(self, body_part, damage):
        armor_stats = self.calculate_stats('armor')
        if body_part == 'head' and self.equipment.head:
            damage -= damage / 100 * armor_stats
            return damage
        elif body_part == 'body' and self.equipment.body:
            damage -= damage / 100 * armor_stats
            return damage
        elif body_part == 'arms' and self.equipment.arms:
            damage -= damage / 100 * armor_stats
            return damage
        elif body_part == 'legs' and self.equipment.legs:
            damage -= damage / 100 * armor_stats
            return damage
        return damage
