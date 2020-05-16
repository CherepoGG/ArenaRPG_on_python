import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.max_hp = 50
        self.hp = self.max_hp
        self.lvl = 1
        self.exp = 0
        self._expForLvlUp = 30
        self.damage = 10
        self.atk = ""
        self.defence = ""

    def attack(self, enemy):
        enemy.hp -= self.damage

    def restore(self):
        self.hp = self.max_hp

    def _check_lvl_up(self):
        if self.exp >= self._expForLvlUp:
            self.exp -= self._expForLvlUp
            self.lvl += 1
            self._expForLvlUp = self._expForLvlUp * 2
            self.max_hp += 10
            self.hp = self.max_hp
            self.damage += 5
            print("Уровень повышен! Теперь ваш уровень:", self.lvl, "урон:", self.damage, "здоровье:", self.max_hp)

    def _add_experience(self, count):
        self.exp += count
        print("Получено опыта:", player.exp)
        self._check_lvl_up()

    def reward(self, exp_reward):
        self._add_experience(exp_reward)

    def restore_hero(self):
        self.hp = self.max_hp


class Enemy:
    def __init__(self):
        self.name = 'Враг'
        self.hp = 30
        self.lvl = 1
        self.damage = 10
        self.exp_reward = 10
        self.atk = ""
        self.defence = ""

    def attack(self, enemy):
        enemy.hp -= self.damage


class EnemyGenerator:
    LIGHT = 'light'
    MEDIUM = 'medium'
    HARD = 'hard'
    BOSS = 'boss'

    def generate(self, lvl, enemy_type):
        enemy = Enemy()
        if enemy_type == self.LIGHT:
            enemy.hp = 25 + (lvl * 5)
            enemy.lvl = lvl
            enemy.damage = 3 * lvl
            enemy.exp_reward = 10 * lvl
        elif enemy_type == self.MEDIUM:
            enemy.hp = 45 + (lvl * 5)
            enemy.lvl = lvl
            enemy.damage = 5 * lvl
            enemy.exp_reward = 15 * lvl
        elif enemy_type == self.HARD:
            enemy.hp = 65 + (lvl * 5)
            enemy.lvl = lvl
            enemy.damage = 7 * lvl
            enemy.exp_reward = 30 * lvl
        elif enemy_type == self.BOSS:
            enemy.hp = 95 + (lvl * 5)
            enemy.lvl = lvl
            enemy.damage = 10 * lvl
            enemy.exp_reward = 50 * lvl
        return enemy


generate_enemy = EnemyGenerator()
player = Hero("Richard")


def check_winner(player, enemy):
    if enemy.hp <= 0:
        print("Вы победили!")
        player.reward(enemy.exp_reward)
    elif player.hp <= 0:
        print("Вы проиграли бой!")
        player.restore_hero()
        print("Воскрешение героя...")


body_parts = ["head", "body", "arms", "legs"]


def enemy_stage(enemy):
    enemy.atk = random.choice(body_parts)
    print(enemy.name, "бьет в", enemy.atk)  # для теста
    enemy.defence = random.choice(body_parts)
    print(enemy.name, "защищает", enemy.defence)  # для теста
    return enemy


def player_stage(player):
    player.atk = random.choice(body_parts)
    print(player.name, "бьет в", player.atk)  # для теста
    player.defence = random.choice(body_parts)
    print(player.name, "защищает", player.defence)  # для теста
    return player


def battle(player, enemy):
    current_player = random.choice((player, enemy))
    while player.hp > 0 and enemy.hp > 0:
        player_stage(player)
        enemy_stage(enemy)
        if current_player == player:
            if player.atk == enemy.defence:
                print("Противник заблокировал удар, направленный в", player.atk)
            else:
                player.attack(enemy)
                print("Вы нанесли", enemy.name, player.damage, "Урона по его", player.atk, ". У", enemy.name,
                      "осталось", enemy.hp, "здоровья")
            current_player = enemy
        else:
            if enemy.atk == player.defence:
                print("Вы заблокировали удар, направленный в", enemy.atk)
            else:
                enemy.attack(player)
                print("Противник нанес вам", enemy.damage, "урона по", enemy.atk, ".У вас осталось", player.hp,
                      "здоровья")
            current_player = player
    check_winner(player, enemy)


enemy = generate_enemy.generate(player.lvl, generate_enemy.LIGHT)
battle(player, enemy)
