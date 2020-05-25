class Armor:
    def __init__(self, name, armor_type, defence):
        self.name = name
        self.type = armor_type
        self.defence = defence


leather_helmet = Armor('Кожаный шлем', 'head', 1)

iron_helmet = Armor('Железный шлем', 'head', 2)

steel_helmet = Armor('Железный шлем', 'head', 3)
