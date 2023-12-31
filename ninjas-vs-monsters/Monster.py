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
        self.speed = random_monster['speed']
        self.hp = random_monster['hp']
        self.attack = random_monster['attack']

    def draw_monster(self, screen, tick):
        cur_image = self.image_types[self.image_type][self.anim_image]
        cur_image_height = cur_image.get_height()
        if(self.should_move):
            #the monster only moves left... flip image
            #only time we flip
            self.x -= self.speed
        cur_image = pygame.transform.flip(cur_image,True,False)
        if(tick % 5 == 0):
            #anim_image only changes every 5 ticks
            self.anim_image += 1
            if(self.anim_image == 7):
                #we only have 0-9 images, so 10 is too far
                self.anim_image = 0
        #update the x on teh rect of the monster, to self.x
        self.rect.x = self.x
        # self.rect.y is what pygame uses to determine where to collide
        #self.y is where we manage his location, blit we can send either
        self.rect.y = self.y - cur_image_height
        #blit draws the monster
        screen.blit(cur_image,(self.x,self.rect.y))

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

    def take_damage(self, player,player_score_button):
        #reduce monster health
        self.hp -= player.attack_power
        #check how much health monster has left
        if(self.hp <= 0):
            self.image_type = "DIE"
            self.anim_image = 0 #reset anim image to 0
            #0, change animation to dead
            #0, remove him from the group
            #0, player kill_counter += 1
            player.score += 1
            player_score_button.update_text(f"Monsters Taken Down: {player.score}")
        else:
            #monster has at least 1 health
            #1+, animate goes to hurt
            self.image_type = "HURT"
            self.anim_image = 0 #reset anim image to 0