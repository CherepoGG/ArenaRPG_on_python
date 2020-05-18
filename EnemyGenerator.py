from Enemy import Enemy


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
