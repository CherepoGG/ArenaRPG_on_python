from weapons import Weapon

from armor import Armor

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

    def chance_item_drop(self, enemy):
        random_count = random.randint(-1, 101)
        if random_count == 0.5:
            random_count *= enemy.battle_difficulty

    def item_generate(self, enemy):
        if enemy.battle_difficulty == 1:
            random_count = random.randint(-1, 101)
            random.choice(Armor, weapon)
            if random_count >= 0.5 * enemy.battle_difficulty:
                weapon = Weapon('Топор Титана', 100, 'легендарное', 10000)
                armor = Armor('Шлем Титана', 'head', 50, 'легендарное', 50000)
                random.choice(armor, weapon)
            elif random_count >= 1 * enemy.battle_difficulty:
                weapon = Weapon('Топор рыцаря', 75, 'редкое', 7500)
                armor = Armor('Рыцарский шлем', 'head', 35, 'редкое', 35000)
                random.choice(armor, weapon)
            elif random_count >= 5 * enemy.battle_difficulty:
                weapon = Weapon('Топор наемника', 40, 'необычное', 4000)
                armor = Armor('Шлем наемника', 'head', 15, 'необычное', 15000)
                random.choice(armor, weapon)
            elif random_count >= 10 * enemy.battle_difficulty:
                weapon = Weapon('Топор дровосека', 15, 'обычное', 1500)
                armor = Armor('Кожаный шлем', 'head', 5, 'обычное', 5000)
                random.choice(armor, weapon)
        elif enemy.battle_difficulty == 2:
