import pygame

class Background():
    def __init__(self,screen,screen_size):
        self.screen = screen
        #grab our image off the hard drive and load it into pygame
        self.background_image = pygame.image.load('./images/background4.png')
        #change the size of the image
        #scale method! scale takes 2 args:
        #1. what to scale
        # 2.tuple of the new coords
        self.background_image = pygame.transform.scale(self.background_image,screen_size)
        self.background_rect = self.background_image.get_rect()
        # print(background_rect)

    def draw_bg(self,screen):
        #blit = block image transfer
        #blit takes 2 args: 
        #1. what to draw
        #2. where to draw it (x,y coords which we get from get_rect)
        screen.blit(self.background_image,self.background_rect)