import pygame
from update_screen import update_screen
from Background import Background
from Player import Player
from check_events import check_events

clock = pygame.time.Clock()
# print("Pygame successfully imported!")
pygame.init() #initialize all the pygame stuff
#get the display info... Info is a class!
display_info = pygame.display.Info()
screen_size = (display_info.current_w, display_info.current_h)
screen = pygame.display.set_mode(screen_size)
game_on = True #a boolean for our game loop
background = Background(screen, screen_size)
player = Player(screen)
tick = 0
#this is the main game loop... run until quit
while(game_on):
    tick += 1
    #run check_events where we have moved all our event logic
    #check_events returns a dictionary, with a "game_on" key
    event_data = check_events(player)
    game_on = event_data["game_on"]
    # screen.fill("red") #fill changes the color of the screen
    #run update_screen which is where we draw, and update stuff
    update_screen(screen = screen,player = player, background = background, tick = tick)
    clock.tick(60) #the number is the fps (frame per second)
    pygame.display.flip() #DRAW OUR STUFF