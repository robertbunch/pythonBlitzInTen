import pygame
from update_screen import update_screen
from Background import Background
from Player import Player
from check_events import check_events
# from Monster import Monster
from Troll import Troll
from Ork import Ork
import random 
from Treasure import Treasure

clock = pygame.time.Clock()
# print("Pygame successfully imported!")
pygame.init() #initialize all the pygame stuff
#get the display info... Info is a class!
display_info = pygame.display.Info()
screen_size = (1920, 1080)
screen = pygame.display.set_mode(screen_size)
game_on = True #a boolean for our game loop
background = Background(screen, screen_size)
player = Player(screen)
# troll = Monster()
#a Group is a list-like thing in pygame
#it holds Sprites
monsters = pygame.sprite.Group() 
treasures = pygame.sprite.Group()
treasures.add(Treasure(display_info),Treasure(display_info),Treasure(display_info),Treasure(display_info),Treasure(display_info))
tick = 0
random_number = random.randint(0,1)
if(random_number == 0):
    monsters.add(Troll()) #start the game with a monster
else:
    monsters.add(Ork()) #start the game with a monster
#this is the main game loop... run until quit
while(game_on):
    tick += 1
    if(tick % 500 == 0):
        random_number = random.randint(0,1)
        #every 1000 ticks add a monster
        if(random_number == 0):
            monsters.add(Troll())
        else:
            monsters.add(Ork())
    #run check_events where we have moved all our event logic
    #check_events returns a dictionary, with a "game_on" key
    event_data = check_events(player,tick)
    game_on = event_data["game_on"]
    # screen.fill("red") #fill changes the color of the screen
    #run update_screen which is where we draw, and update stuff
    update_screen(screen = screen,player = player, background = background, tick = tick, display_info = display_info, monsters = monsters, treasures=treasures)
    clock.tick(60) #the number is the fps (frame per second)
    pygame.display.flip() #DRAW OUR STUFF