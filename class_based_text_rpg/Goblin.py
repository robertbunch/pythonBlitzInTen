
from Monster import Monster
class Goblin(Monster):
    def __init__(self):
        self.character_name = "Goblin"
        self.xp_drop = 1
        self.gold_drop = 5
        self.attack_power = 3
        self.defense = 3
        self.max_hp = 7
        self.hp = 7
        self.weapon = "fists"
        #super() is the same as calling the Monster class
        super().__init__(self.character_name, self.xp_drop, self.gold_drop, 
                         self.attack_power,self.defense,
                         self.max_hp,self.hp,self.weapon)


    def special_power(self):
        print("Goblin calls for help")
