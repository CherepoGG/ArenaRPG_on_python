class Inventory:
    def __init__(self):
        self.inventory = []
        self.limit = 10
        self.current_limit = 0

    def add_item(self, item):
        if self.current_limit <= self.limit - 1:
            self.current_limit += 1
            self.inventory.append(item)
        else:
            print("Ваш инвентарь полон")

    def delete_item(self, player):
        for element in self.inventory:
            if element == player.equipment.weapon:
                self.inventory.pop(self.inventory.index(element))
            elif element == player.equipment.head:
                self.inventory.pop(self.inventory.index(element))
            elif element == player.equipment.body:
                self.inventory.pop(self.inventory.index(element))
            elif element == player.equipment.arms:
                self.inventory.pop(self.inventory.index(element))
            elif element == player.equipment.legs:
                self.inventory.pop(self.inventory.index(element))
