import random

from Monster import Monster
class Dragon(Monster):
    def __init__(self):
        self.character_name = "Dragon"
        self.xp_drop = 100
        self.gold_drop = 500
        self.attack_power = random.randint(100,150)
        self.defense = 60
        self.max_hp = 700
        self.hp = random.randint(500,700)
        self.weapon = "Dragon Claws"
        #super() is the same as calling the Monster class
        super().__init__(self.character_name, self.xp_drop, self.gold_drop, 
                         self.attack_power,self.defense,
                         self.max_hp,self.hp,self.weapon)


    def special_power(self):
        print("Goblin calls for help")
