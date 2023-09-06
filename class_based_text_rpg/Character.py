
class Character():
    #all classes start with an init dunder method
    def __init__(self,character_name,xp,level,gold,attack_power,defense,max_hp,hp,weapon,inventory):
        self.character_name = character_name
        self.xp = xp
        self.level = level
        self.gold = gold
        self.attack_power = attack_power
        self.defense = defense
        self.max_hp = max_hp
        self.hp = hp
        self.weapon = weapon
        self.inventory = inventory
