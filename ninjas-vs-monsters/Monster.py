import pygame
from image_load import monster_image_load
from pygame.sprite import Sprite

#monster is now a sub class of Sprite
class Monster(Sprite):

    #Any variable defined IN a class, but NOT in 
    #a method, is a class variable. This is in contrast
    #with an instance variable. An instance variable
    #belongs specifically to an object. A class varaible
    #all objects of that class SHARE.
    #instance variables use self (in the class)
    image_types = monster_image_load("1_TROLL") #CLASS VARIABLE

    def __init__(self):
        #run the constructor method for the Sprite (super class)
        super().__init__()
        self.x = 1000
        self.y = 200
        self.anim_image = 0
        self.image_type = "WALK"
        self.stop_attacking_at = False
        self.is_attacking = False
        self.should_move = True

    def draw_monster(self, screen, tick):
        cur_image = Monster.image_types[self.image_type][self.anim_image]
        if(self.should_move):
            #the monster only moves left... flip image
            #only time we flip
            self.x -= 3
            cur_image = pygame.transform.flip(cur_image,True,False)
            if(tick % 5 == 0):
                #anim_image only changes every 5 ticks
                self.anim_image += 1
                if(self.anim_image == 7):
                    #we only have 0-9 images, so 10 is too far
                    self.anim_image = 0

        #blit draws the monster
        screen.blit(cur_image,(self.x,self.y))

