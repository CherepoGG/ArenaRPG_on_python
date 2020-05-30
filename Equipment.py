class Equipment:
    def __init__(self):
        self.head = 'Не надето'
        self.body = 'Не надето'
        self.arms = 'Не надето'
        self.legs = 'Не надето'
        self.weapon = 'Не надето'

    def equip_item(self, item, player, enemy_damage):
        if item.type == 'weapon':
            self.weapon = item
            player.inventory.delete_item(player)
            self.apply_stats_weapon(player, item.damage)
        elif item.type == 'armor':
            if item.part == 'head':
                self.head = item
                player.inventory.delete_item(player)
                self.apply_stats_armor(player, item.defence, enemy_damage)
            elif item.part == 'body':
                self.body = item
                player.inventory.delete_item(player)
                self.apply_stats_armor(player, item.defence, enemy_damage)
            elif item.part == 'arms':
                self.arms = item
                player.inventory.delete_item(player)
                self.apply_stats_armor(player, item.defence, enemy_damage)
            elif item.part == 'legs':
                self.legs = item
                player.inventory.delete_item(player)
                self.apply_stats_armor(player, item.defence, enemy_damage)

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

    def apply_stats_armor(self, player, item_stats, input_damage):
        if self.head != 'Не надето':
            player.defence += item_stats
            input_damage -= input_damage / 100 * 25
        elif self.body != 'Не надето':
            player.defence += item_stats
            input_damage -= input_damage / 100 * 50
        elif self.arms != 'Не надето':
            player.defence += item_stats
            input_damage -= input_damage / 100 * 10
        elif self.legs != 'Не надето':
            player.defence += item_stats
            input_damage -= input_damage / 100 * 15

    def apply_stats_weapon(self, player, item_stats):
        if self.weapon != 'Не надето':
            player.damage += item_stats
