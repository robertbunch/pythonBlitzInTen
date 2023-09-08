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

    def battle_victory(self,vanquished_foe):
        # print("Check to see if hero has leveled up")
        print(f"Well done, magnificant {self.character_name}, thou hast slain the impudent {vanquished_foe.character_name}.")
        #the hero won, so grant the hero some gold and xp
        self.gold += vanquished_foe.gold_drop
        self.xp += vanquished_foe.xp_drop
        print(f"Thou has gained {vanquished_foe.gold_drop} gold and {vanquished_foe.xp_drop} experience.")
        print(f"Thou now hasts total of {self.gold} gold and {self.xp} experience.")
        