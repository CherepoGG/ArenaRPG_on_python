from weapons import Weapon

from armor import Armor

from item import Item

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

    def reward(self, player, exp_reward, gold_reward, item_reward, battle_difficulty):
        self._add_experience(player, exp_reward)
        self._add_gold(player, gold_reward)
        item_reward = self.item_generate(player, battle_difficulty)
        if item_reward:
            self._add_item(player, item_reward)

    def item_generate(self, player, battle_difficulty):
        item = Item()
        random_count = random.uniform(0.0, 100.0)
        print(random_count)
        items = [Armor(item.common, player.lvl), Weapon(item.common, player.lvl)]
        random_item = random.choice(items)
        print('генерир. шмот:', random_item)
        if random_count <= 0.5 * battle_difficulty:
            item_reward = random_item
            return item_reward
        elif random_count <= 1 * battle_difficulty:
            item_reward = random_item
            return item_reward
        elif random_count <= 5 * battle_difficulty:
            item_reward = random_item
            return item_reward
        elif random_count <= 100 * battle_difficulty:
            item_reward = random_item
            return item_reward
