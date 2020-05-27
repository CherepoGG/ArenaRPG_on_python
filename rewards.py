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

    def _add_gold(self, player, gold_reward):
        player.gold += gold_reward
        print('Получено золота:', gold_reward)

    def reward(self, player, exp_reward, gold_reward, item_reward):
        self._add_experience(player, exp_reward)
        self._add_gold(player, gold_reward)
        self._add_item(player, item_reward)
        print('Получен предмет:', item_reward)

    def item_generate(self, player, enemy):
        item = Item()
        random_count = random.randint(-1, 101)
        random_result = random.choice(Armor, Weapon)
        if random_count >= 0.5 * enemy.battle_difficulty:
            player.inventory.add_item(random_result(item.legendary, player.lvl))
        elif random_count >= 1 * enemy.battle_difficulty:
            player.inventory.add_item(random_result(item.rare, player.lvl))
        elif random_count >= 5 * enemy.battle_difficulty:
            player.inventory.add_item(random_result(item.magic, player.lvl))
        elif random_count >= 10 * enemy.battle_difficulty:
            player.inventory.add_item(random_result(item.common, player.lvl))
