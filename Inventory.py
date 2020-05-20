class InventoryHero:
    def __init__(self):
        self.inventory = []
        self.limit = 10

    def add_object(self, subject):
        if self.limit <= 9:
            self.inventory.append(subject)
        else:
            print("Ваш инвентарь полон")

    def delete_object(self, subject):
        self.inventory.pop(subject)
