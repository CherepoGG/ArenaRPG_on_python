from Inventory import InventoryHero


class Hero:
    def __init__(self):
        self.name = 'Richard'
        self.max_hp = 50
        self.hp = self.max_hp
        self.lvl = 1
        self.exp = 0
        self._expForLvlUp = 30
        self.damage = 10
        self.atk = ""
        self.defence = ""
        self.inventory = InventoryHero()

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
            print("Уровень повышен! Теперь ваш уровень:", self.lvl, "урон:", self.damage, "здоровье:", self.max_hp)

    def _add_experience(self, count):
        self.exp += count
        print("Получено опыта:", self.exp)
        self._check_lvl_up()

    def reward(self, exp_reward):
        self._add_experience(exp_reward)

    def restore_hero(self):
        self.hp = self.max_hp
