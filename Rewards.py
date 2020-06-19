from Weapons import Weapon

from Armor import Armor

from Item import Item

import random


class Rewards:
    def _add_experience(self, player, count):
        player.exp += count
        print('Получено опыта:', player.exp)
        player._check_lvl_up()

    def _add_item(self, player, item):
        player.inventory.add_item(item)
        print('Получен предмет:', item)

    def _add_gold(self, player, gold_reward):
        player.gold += gold_reward
        print('Получено золота:', gold_reward)

    def reward(self, player, exp_reward, gold_reward, battle_difficulty):
        self._add_experience(player, exp_reward)
        self._add_gold(player, gold_reward)
        item_reward = self.item_generate(player, battle_difficulty)
        if item_reward:
            self._add_item(player, item_reward)

    def item_generate(self, player, battle_difficulty):
        item = Item()
        random_count = random.uniform(0.0, 100.0)
        part_armor = ['head', 'body', 'arms', 'legs']
        print(random_count)  # testing
        items = [Armor, Weapon]
        random_item = random.choice(items)
        print('генерир. шмот:', random_item)  # testing
        if random_item == Armor:
            random_part_armor = random.choice(part_armor)
            if random_count <= 0.5 * battle_difficulty:
                item_reward = random_item(random_part_armor, item.legendary, player.lvl)
                return item_reward
            elif random_count <= 1 * battle_difficulty:
                item_reward = random_item(random_part_armor, item.rare, player.lvl)
                return item_reward
            elif random_count <= 5 * battle_difficulty:
                item_reward = random_item(random_part_armor, item.magic, player.lvl)
                return item_reward
            elif random_count <= 10 * battle_difficulty:
                item_reward = random_item(random_part_armor, item.common, player.lvl)
                return item_reward
        else:
            if random_count <= 0.5 * battle_difficulty:
                item_reward = random_item(item.legendary, player.lvl)
                return item_reward
            elif random_count <= 1 * battle_difficulty:
                item_reward = random_item(item.rare, player.lvl)
                return item_reward
            elif random_count <= 5 * battle_difficulty:
                item_reward = random_item(item.magic, player.lvl)
                return item_reward
            elif random_count <= 10 * battle_difficulty:
                item_reward = random_item(item.common, player.lvl)
                return item_reward

    def give_armor(self, player, part_armor, quality):  # TODO: TESTING
        if quality == 1:
            quality = Item.common
        elif quality == 2:
            quality = Item.magic
        elif quality == 3:
            quality = Item.rare
        elif quality == 4:
            quality = Item.legendary
        if part_armor == 'head':
            head = Armor('head', quality, player.lvl)
            self._add_item(player, head)
        elif part_armor == 'body':
            body = Armor('body', quality, player.lvl)
            self._add_item(player, body)
        elif part_armor == 'arms':
            arms = Armor('arms', quality, player.lvl)
            self._add_item(player, arms)
        elif part_armor == 'legs':
            legs = Armor('legs', quality, player.lvl)
            self._add_item(player, legs)

    def give_weapon(self, player):  # TODO: TESTING
        weapon = Weapon('common', Item.common)
        self._add_item(player, weapon)
