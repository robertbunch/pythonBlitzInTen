
from Character import Character

class Monster(Character):
    def __init__(self, character_name, xp_drop, gold_drop, attack_power,defense,max_hp,hp,weapon):
        self.xp_drop = xp_drop
        self.gold_drop = gold_drop
        super().__init__(character_name,attack_power,defense,max_hp,hp,weapon)

    def growl():
        print(f"The monster has holwed in anger")