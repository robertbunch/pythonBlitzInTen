import pygame
import random #use random to randomize our treasure type, also position

class Treasure(pygame.sprite.Sprite):
    treasure_pile = pygame.image.load('./images/treasures.png')
    treasure_vase = pygame.image.load('./images/treasures_vase.png')
    treasure_pile = pygame.transform.scale_by(treasure_pile,.3)
    treasure_vase = pygame.transform.scale_by(treasure_vase,.3)
    treasures = [treasure_pile,treasure_vase]
    def __init__(self):
        random_treasure = Treasure.treasures[random.randint(0,1)]
        self.image = random_treasure
        self.rect = self.image.get_rect()
        self.x = 200
        self.y = 500
        self.rect.x = self.x #self.rect is for pygame, self.x is for us
        self.rect.y = self.y

        super().__init__() #this makes the constructor run in the super class
    def draw_me(self, screen):
        screen.blit(self.image,(self.x,self.y))