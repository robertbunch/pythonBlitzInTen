
class Character():
    #all classes start with an init dunder method
    def __init__(self,character_name,attack_power,defense,max_hp,hp,weapon):
        self.character_name = character_name
        self.attack_power = attack_power
        self.defense = defense
        self.max_hp = max_hp
        self.hp = hp
        self.weapon = weapon

    def take_damage(self):
        print("Placeholder for take damage")
