import pygame
from Monster import Monster
from image_load import monster_image_load
import random

class Ork(Monster):
    ork_images = {
        "ork1": monster_image_load("1_ORK","ork"), #CLASS VARIABLE
        "ork2": monster_image_load("2_ORK","ork"),
        "ork3": monster_image_load("3_ORK","ork"),
    }

    def __init__(self):
        display_info = pygame.display.Info()
        self.y = random.randint(50,display_info.current_h - 250)
        self.x = display_info.current_w - 50

        ork_stats = [{
            "hp" : 20,
            "speed" : 1.2,
            "attack" : 3,
            "name" : "ork1",
            "images" : Ork.ork_images['ork1'],
        },
        {
            "hp" : 25,
            "speed" : 1,
            "attack" : 3,
            "name" : "ork2",
            "images" : Ork.ork_images['ork2'],
        },
        {
            "hp" : 15,
            "speed" : 1,
            "attack" : 4,
            "name" : "ork3",
            "images" : Ork.ork_images['ork3'],
        }]
        random_index = random.randint(0,2)
        random_ork = ork_stats[random_index]
        super().__init__(random_ork)