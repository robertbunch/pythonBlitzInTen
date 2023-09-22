import pygame
from Monster import Monster
from image_load import monster_image_load
import random

class Troll(Monster):

    #Any variable defined IN a class, but NOT in 
    #a method, is a class variable. This is in contrast
    #with an instance variable. An instance variable
    #belongs specifically to an object. A class varaible
    #all objects of that class SHARE.
    #instance variables use self (in the class)
    troll_images = {
        "troll1": monster_image_load("1_TROLL"), #CLASS VARIABLE
        "troll2": monster_image_load("2_TROLL"),
        "troll3": monster_image_load("3_TROLL"),
    }

    def __init__(self):
        display_info = pygame.display.Info()
        self.y = random.randint(50,display_info.current_h - 250)
        self.x = display_info.current_w - 50

        troll_stats = [{
            "hp" : 10,
            "speed" : 3,
            "attack" : 2,
            "name" : "troll1",
            "images" : Troll.troll_images['troll1'],
        },
        {
            "hp" : 15,
            "speed" : 2.4,
            "attack" : 3,
            "name" : "troll2",
            "images" : Troll.troll_images['troll2']
        },
        {
            "hp" : 20,
            "speed" : 2,
            "attack" : 4,
            "name" : "troll3",
            "images" : Troll.troll_images['troll3']
        }]
        random_index = random.randint(0,2)
        random_troll = troll_stats[random_index]
        super().__init__(random_troll)