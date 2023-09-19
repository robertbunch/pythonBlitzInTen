import pygame
#images from https://opengameart.org/content/ninja-adventure-free-sprite
class Player():
    def __init__(self,screen):
        self.screen = screen
        self.x = 200
        self.y = 200
        #load the image from the hd
        self.image = pygame.image.load("./images/ninja/Idle__000.png")
        self.image = pygame.transform.scale_by(self.image,.35)
        #get the coords of the image
        self.rect = self.image.get_rect() 
    def draw_player(self,screen):
        screen.blit(self.image,(self.x,self.y))