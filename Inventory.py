class Inventory:
    def __init__(self):
        self.inventory = []
        self.limit = 10
        self.current_limit = 0

    def add_item(self, item):
        if self.current_limit <= self.limit - 1:
            self.current_limit += 1
            for i in item:
                self.inventory.append(i)
        else:
            print("Ваш инвентарь полон")

    def delete_item(self, player):
        for element in self.inventory:
            if element == player.equipment.weapon:
                self.inventory.pop(self.inventory.index(element))
            elif element == player.equipment.armor:
                self.inventory.pop(self.inventory.index(element))
