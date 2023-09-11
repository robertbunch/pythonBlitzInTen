
from Monster import Monster
class Zombie(Monster):

    def __init__(self):
        self.character_name = "Zombie"
        self.xp_drop = 2
        self.gold_drop = 5
        self.attack_power = 5
        self.defense = 2
        self.max_hp = 7
        self.hp = 9
        self.weapon = "fists"
        #super() is the same as calling the Monster class
        super().__init__(self.character_name, self.xp_drop, self.gold_drop, 
                         self.attack_power,self.defense,
                         self.max_hp,self.hp,self.weapon)


    def special_power(self):
        print("Zombie is enraged")
