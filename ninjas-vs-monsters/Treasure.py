import pygame

class Treasure(pygame.sprite.Sprite):
    def __init__(self):
        print("Treasure")
        super().__init__() #this makes the constructor run in the super class
    def draw_me(self, screen):
        print("Treasure here")