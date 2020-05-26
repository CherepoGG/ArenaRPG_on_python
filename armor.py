class Armor:
    def __init__(self, name, part, defence, quality, cost):
        self.name = name
        self.type = 'armor'
        self.part = part
        self.defence = defence
        self.quality = quality
        self.cost = cost

    def up_stats(self, player):
        if self.quality == 'обычное':
            self.defence = 1 * player.lvl
            self.cost = 5 * player.lvl
        elif self.quality == 'необычное':
            self.defence = 2 * player.lvl
            self.cost = 10 * player.lvl
        elif self.quality == 'редкое':
            self.defence = 3 * player.lvl
            self.cost = 15 * player.lvl
        elif self.quality == 'легендарное':
            self.defence = 5 * player.lvl
            self.cost = 50 * player.lvl
