from Hero import Hero


class InventoryHero(Hero):
    def __init__(self):
        super().__init__()
        self.inventory = [1, 2, 3]
