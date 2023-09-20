import pygame
#images from https://opengameart.org/content/ninja-adventure-free-sprite
class Player():
    def __init__(self,screen):
        self.screen = screen
        self.x = 200
        self.y = 200
        # anim_image is the number cooreponding to the number in the filename of the that image
        self.anim_image = 0

        self.image_types = {
            "Idle" : [],
            "Run" : [],
        }

        for image_type in self.image_types:
            for i in range(0,10):
                image_to_load = pygame.image.load(f"./images/ninja/{image_type}__00{i}.png")
                image_to_load = pygame.transform.scale_by(image_to_load,.35)
                self.image_types[image_type].append(image_to_load)
        #load the image from the hd
        self.image = pygame.image.load("./images/ninja/Idle__000.png")
        self.image = pygame.transform.scale_by(self.image,.35)
        #get the coords of the image
        self.rect = self.image.get_rect() 
    def draw_player(self,screen):
        screen.blit(self.image,(self.x,self.y))