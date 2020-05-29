class Equipment:
    def __init__(self):
        self.head = 'Не надето'
        self.body = 'Не надето'
        self.arms = 'Не надето'
        self.legs = 'Не надето'
        self.weapon = 'Не надето'

    def equip_item(self, item, player):
        if item.type == 'weapon':
            self.weapon = item
            player.inventory.delete_item(player)
            self.apply_stats(player, item.damage)
        elif item.type == 'armor':
            if item.part == 'head':
                self.head = item
                player.inventory.delete_item(player)
                self.apply_stats(player, item.defence)
            elif item.part == 'body':
                self.body = item
                player.inventory.delete_item(player)
                self.apply_stats(player, item.defence)
            elif item.part == 'arms':
                self.arms = item
                player.inventory.delete_item(player)
                self.apply_stats(player, item.defence)
            elif item.part == 'legs':
                self.legs = item
                player.inventory.delete_item(player)
                self.apply_stats(player, item.defence)

    def remove_item(self, item, player):  # Будет кнопка, вызывающая эту функцию напротив каждого предмета экипировки
        if item.type == 'armor':
            if item == self.head:
                self.head = 'Не надето'
                player.inventory.inventory.append(item)
            elif item == self.body:
                self.body = 'Не надето'
                player.inventory.inventory.append(item)
            elif item == self.arms:
                self.arms = 'Не надето'
                player.inventory.inventory.append(item)
            elif item == self.legs:
                self.legs = 'Не надето'
                player.inventory.inventory.append(item)
        elif item == self.weapon:
            self.weapon = 'Не надето'
            player.inventory.inventory.append(item)

    def apply_stats(self, player, item_stats):
        if self.head != 'Не надето':
            player.defence += item_stats
        elif self.body != 'Не надето':
            player.defence += item_stats
        elif self.arms != 'Не надето':
            player.defence += item_stats
        elif self.legs != 'Не надето':
            player.defence += item_stats
        elif self.weapon != 'Не надето':
            player.damage += item_stats
