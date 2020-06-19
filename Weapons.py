from Item import Item


class Weapon(Item):
    def __init__(self, quality, lvl):
        self.name = 'оружие'
        self.type = 'weapon'
        self.damage = 5 * lvl * quality
        self.quality = quality
        self.cost = 10 * lvl * quality
