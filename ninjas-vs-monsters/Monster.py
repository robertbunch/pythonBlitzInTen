import pygame
from image_load import monster_image_load

class Monster():
    def __init__(self):
        self.x = 1000
        self.y = 200
        self.anim_image = 0
        self.image_type = "WALK"
        self.stop_attacking_at = False
        self.is_attacking = False
        self.should_move = True

        self.image_types = monster_image_load("1_TROLL")

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

        #blit draws the monster
        screen.blit(cur_image,(self.x,self.y))

