
class Character():
    #all classes start with an init dunder method
    def __init__(self,character_name,attack_power,defense,max_hp,hp,weapon):
        self.character_name = character_name
        self.attack_power = attack_power
        self.defense = defense
        self.max_hp = max_hp
        self.hp = hp
        self.weapon = weapon

    def take_damage(self,other_char_obj):
        #hero_power_hit = take the hero's attack_power - monster's defense
        #reduce the monster's hp by hero_power_hit
        power_hit = other_char_obj.attack_power - self.defense
        self.hp -= power_hit
        return power_hit