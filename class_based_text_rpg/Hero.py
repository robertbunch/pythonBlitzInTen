from Character import Character

class Hero(Character):
    def __init__(self, character_name, xp, level, gold, 
                 attack_power,defense,max_hp,hp,weapon,
                 inventory,game_settings):
        self.xp = xp
        self.level = level
        self.gold = gold
        self.inventory = inventory
        self.game_settings = game_settings
        #we call super, which is the Character class. And we call it's init method
        #we only pass the things the Character class init method needs
        super().__init__(character_name,attack_power,defense,max_hp,hp,weapon)

    def battle_victory(self,vanquished_foe):
        # print("Check to see if hero has leveled up")
        print(f"Well done, magnificant {self.character_name}, {self.game_settings.colors['red']}thou hast slain the impudent {vanquished_foe.character_name}{self.game_settings.colors['normal']}.")
        #the hero won, so grant the hero some gold and xp
        self.gold += vanquished_foe.gold_drop
        self.xp += vanquished_foe.xp_drop
        print(f"Thou has gained {vanquished_foe.gold_drop} gold and {vanquished_foe.xp_drop} experience.")
        print(f"Thou now hasts total of {self.gold} gold and {self.xp} experience.")
        #check to see if the hero has made a new level
        new_level_data = self.game_settings.levels[self.level + 1]
        if(self.xp >= new_level_data["threshold"]):
            #hero has leveled up!
            self.level += 1 #increase hero level
            self.attack_power += new_level_data["attack_increase"]
            self.defense += new_level_data["defense_increase"]
            self.max_hp += new_level_data["hp_increase"]
            #reset current hp to max_hp
            self.hp = self.max_hp
            print(f"Well done, brave {self.character_name}! {self.game_settings.colors['green']}Thou has reached a new level of {self.level}{self.game_settings.colors['normal']}.")
            print(f"Thine hp is now {self.hp}, thine attack is now {self.attack_power} and thine defense is {self.defense}.")
    def set_weapon(self,weapon):
        self.weapon = weapon
        if(weapon == "Magic Sword"):
            self.attack_power = self.attack_power * 1.15
            