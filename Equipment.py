class Equipment:
    def __init__(self):
        self.armor = 'Не надето'
        self.weapon = 'Не надето'

    def equip_item(self, item, player):
        if item.type == 'weapon':
            self.weapon = item
            player.inventory.inventory.delete_item(player)
            self.apply_stats(player, item.damage)
        elif item.type == 'armor':
            self.armor = item
            player.inventory.inventory.delete_item(player)
            self.apply_stats(player, item.defence)

    def remove_item(self, item, player):  # Будет кнопка, вызывающая эту функцию напротив каждого предмета экипировки
        if item == self.armor:
            self.armor = 'Не надето'
            player.inventory.inventory.append(item)
        elif item == self.weapon:
            self.weapon = 'Не надето'
            player.inventory.inventory.append(item)

    def apply_stats(self, player, item_stats):
        if self.armor != 'Не надето':
            player.defence += item_stats
        elif self.weapon != 'Не надето':
            player.damage += item_stats
