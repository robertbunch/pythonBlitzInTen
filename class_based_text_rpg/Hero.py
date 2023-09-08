from Character import Character

class Hero(Character):
    def __init__(self, character_name, xp, level, gold, attack_power,defense,max_hp,hp,weapon,inventory):
        self.xp = xp
        self.level = level
        self.gold = gold
        self.inventory = inventory
        #we call super, which is the Character class. And we call it's init method
        #we only pass the things the Character class init method needs
        super().__init__(character_name,attack_power,defense,max_hp,hp,weapon)

    def check_level_up(self):
        print("Check to see if hero has leveled up")
        