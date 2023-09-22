import pygame
from image_load import monster_image_load
from pygame.sprite import Sprite

#monster is now a sub class of Sprite
class Monster(Sprite):
    def __init__(self,random_monster):
        #run the constructor method for the Sprite (super class)
        super().__init__()
        # self.x = 1000
        # self.y = 200
        self.anim_image = 0
        self.image_type = "WALK"
        self.stop_attacking_at = False
        self.is_attacking = False
        self.should_move = True
        self.image_types = random_monster['images']
        starter_image = self.image_types[self.image_type][self.anim_image]
        self.rect = starter_image.get_rect() 
        self.rect.x = self.x #init the rect at the correct image position
        self.rect.y = self.y

    def draw_monster(self, screen, tick):
        cur_image = self.image_types[self.image_type][self.anim_image]
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
        #update the x on teh rect of the monster, to self.x
        self.rect.x = self.x
        #blit draws the monster
        screen.blit(cur_image,(self.x,self.y))

    def stop_and_attack(self):
        #set our bool to True
        self.is_attacking = True
        self.should_move = False
        #start the animation for attack
        self.image_type = "ATTAK"
        #start the attack animation from the beginning
        self.anim_image = 0
    
    def move_on(self):
        #move on means, stopped attacking, start walking
        self.is_attacking = False
        self.should_move = True
        self.image_type = "WALK"
        self.anim_image = 0