import pygame
#images from https://opengameart.org/content/ninja-adventure-free-sprite
class Player():
    def __init__(self,screen):
        self.screen = screen
        #load the image from the hd
        self.image = pygame.image.load("./images/ninja/Idle__000.png")
        #get the coords of the image
        self.rect = self.image.get_rect() 
    def move_player(self,screen):
        screen.blit(self.image,self.rect)