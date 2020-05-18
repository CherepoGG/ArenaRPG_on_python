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
