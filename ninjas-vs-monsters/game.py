import pygame
# print("Pygame successfully imported!")
pygame.init() #initialize all the pygame stuff
#get the display info... Info is a class!
display_info = pygame.display.Info()
screen_size = (display_info.current_w, display_info.current_h)
screen = pygame.display.set_mode(screen_size)
game_on = True
while(game_on):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            print(event)
            game_on = False