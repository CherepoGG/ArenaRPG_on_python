class Armor:
    def __init__(self):
        self.name = 'Броня'
        self.type = 'armor'
        self.defence = 2


# class ArmorInfo(BaseArmor):
#     helmet = 'helmet'
#     chest = 'chest'
#     arms = 'arms'
#     legs = 'legs'
#     base_armor = BaseArmor()
#
#     def helmet_stats(self, base_armor):
#         if base_armor.class_equipent_part == 'light':
#             self.part_armor = self.equipment_part[0]
#             self.name = 'Кожаный шлем'
#             self.defend = 2
    #     elif base_armor.class_equipent_part == 'middle':
    #         self.part_armor = self.equipment_part[0]
    #         self.name = 'Железный шлем'
    #         self.defend = 4
    #     elif base_armor.class_equipent_part == 'heavy':
    #         self.part_armor = self.equipment_part[0]
    #         self.name = 'стальной шлем'
    #         self.defend = 6
    #
    # def chest_stats(self, base_armor):
    #     if base_armor.equipment_part == 'light':
    #         self.part_armor = self.equipment_part[1]
    #         self.name = 'Кожаный нагрудник'
    #         self.defend = 4
    #     elif base_armor.class_equipent_part == 'middle':
    #         self.part_armor = self.equipment_part[1]
    #         self.name = 'Железный нагрудник'
    #         self.defend = 8
    #     elif base_armor.class_equipent_part == 'heavy':
    #         self.part_armor = self.equipment_part[1]
    #         self.name = 'Стальной нагрудник'
    #         self.defend = 12
    #
    # def arms_stats(self, base_armor):
    #     if base_armor.class_equipent_part == 'light':
    #         self.part_armor = self.equipment_part[2]
    #         self.name = 'Кожаные наручи'
    #         self.defend = 1
    #     elif base_armor.class_equipent_part == 'middle':
    #         self.part_armor = self.equipment_part[2]
    #         self.name = 'Железные наручи'
    #         self.defend = 2
    #     elif base_armor.class_equipent_part == 'heavy':
    #         self.part_armor = self.equipment_part[2]
    #         self.name = 'Стальные наручи'
    #         self.defend = 3
    #
    # def legs_stats(self, base_armor):
    #     if base_armor.class_equipent_part == 'light':
    #         self.part_armor = self.equipment_part[3]
    #         self.name = 'Кожаные поножи'
    #         self.defend = 2
    #     elif base_armor.class_equipent_part == 'middle':
    #         self.part_armor = self.equipment_part[3]
    #         self.name = 'Железные поножи'
    #         self.defend = 4
    #     elif base_armor.class_equipent_part == 'heavy':
    #         self.part_armor = self.equipment_part[3]
    #         self.name = 'Стальные поножи'
    #         self.defend = 6
