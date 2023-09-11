
from Monster import Monster

class Troll(Monster):
    def __init__(self):
        self.character_name = "Troll"
        self.xp_drop = 15
        self.gold_drop = 20
        self.attack_power = 35
        self.defense = 13
        self.max_hp = 45
        self.hp = 45
        self.weapon = "Troll Hammer"
        #super() is the same as calling the Monster class
        super().__init__(self.character_name, self.xp_drop, self.gold_drop, 
                         self.attack_power,self.defense,
                         self.max_hp,self.hp,self.weapon)


