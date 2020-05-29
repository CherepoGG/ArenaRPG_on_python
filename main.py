import random

from Hero import Hero

from EnemyGenerator import EnemyGenerator

generate_enemy = EnemyGenerator()
player = Hero()
items_reward = []


def check_winner(player, enemy):
    if enemy.hp <= 0:
        print('Вы победили!')
        player.rewards.reward(player, enemy.exp_reward, enemy.gold_reward, items_reward, enemy.battle_difficulty)

    elif player.hp <= 0:
        print('Вы проиграли бой!')
        player.restore_hero()
        print('Воскрешение героя...')


body_parts = ['head', 'body', 'arms', 'legs']
enemy_difficult = ['light', 'medium', 'hard', 'boss']


def enemy_stage(enemy):
    enemy.atk = random.choice(body_parts)
    print(enemy.name, 'бьет в', enemy.atk)  # для теста
    enemy.defence = random.choice(body_parts)
    print(enemy.name, 'защищает', enemy.defence)  # для теста
    return enemy


def player_stage(player):
    player.atk = random.choice(body_parts)
    print(player.name, 'бьет в', player.atk)  # для теста
    player.defend = random.choice(body_parts)
    print(player.name, 'защищает', player.defend)  # для теста
    return player


def check_armor(enemy):
    enemy_damage = enemy.attack(player)
    if player.equipment.head != 'Не надето':
        enemy_damage / 100 * 25
    elif player.equipment.body != 'Не надето':
        enemy_damage = enemy.attack(player)
        enemy_damage / 100 * 50
    elif player.equipment.arms != 'Не надето':
        enemy_damage = enemy.attack(player)
        enemy_damage / 100 * 10
    elif player.equipment.legs != 'Не надето':
        enemy_damage = enemy.attack(player)
        enemy_damage / 100 * 15


def battle(player, enemy):
    while player.hp > 0 and enemy.hp > 0:
        player_stage(player)
        enemy_stage(enemy)
        if player.atk == enemy.defend:
            print('Противник заблокировал удар, направленный в', player.atk)
        else:
            check_armor(enemy)
            player.attack(enemy)
            print('Вы нанесли', enemy.name, player.damage, 'Урона по его', player.atk + '.', 'У', enemy.name,
                  'осталось', enemy.hp, 'здоровья')
        if enemy.atk == player.defend:
            print('Вы заблокировали удар, направленный в', enemy.atk)
        else:
            enemy.attack(player)
            print('Противник нанес вам', enemy.damage, 'урона по', enemy.atk + '.', 'У вас осталось', player.hp,
                  'здоровья')
    check_winner(player, enemy)


def choice_enemy():
    print('Выберите противника:')
    player_choice = enemy_difficult[0]
    print('Вы выбрали', player_choice)
    if player_choice == enemy_difficult[0]:
        enemy = generate_enemy.generate(player.lvl, generate_enemy.LIGHT)
        battle(player, enemy)
    elif player_choice == enemy_difficult[1]:
        enemy = generate_enemy.generate(player.lvl, generate_enemy.MEDIUM)
        battle(player, enemy)
    elif player_choice == enemy_difficult[2]:
        enemy = generate_enemy.generate(player.lvl, generate_enemy.HARD)
        battle(player, enemy)
    else:
        enemy = generate_enemy.generate(player.lvl, generate_enemy.BOSS)
        battle(player, enemy)


choice_enemy()
