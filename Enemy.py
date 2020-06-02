class Enemy:
    def __init__(self):
        self.name = 'Враг'
        self.hp = 30
        self.lvl = 1
        self.damage = 10
        self.exp_reward = 10
        self.gold_reward = 0
        self.battle_difficulty = 1
        self.atk = ''
        self.defend = ''

    def attack(self, enemy, body_part):
        damage = enemy.calculate_damage_by_armor(body_part, self.damage)
        enemy.hp -= damage
        return damage
