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

    def delete_item(self, item):
        for element in self.inventory:
            if element == item:
                index_item = self.inventory.index(item)
                self.inventory.pop(index_item)
