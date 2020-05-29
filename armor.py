from item import Item


class Armor(Item):
    def __init__(self, part, quality, lvl):
        self.name = 'броня'
        self.type = 'armor'
        self.part = part
        self.defence = 1 * lvl * quality
        self.quality = quality
        self.cost = 5 * lvl * quality
