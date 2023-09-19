import pygame
clock = pygame.time.Clock()
# print("Pygame successfully imported!")
pygame.init() #initialize all the pygame stuff
#get the display info... Info is a class!
display_info = pygame.display.Info()
screen_size = (display_info.current_w, display_info.current_h)
screen = pygame.display.set_mode(screen_size)
game_on = True #a boolean for our game loop
#this is the main game loop... run until quit
while(game_on):
    #check to see if if any events occured since
    #the last time through the game loop
    #call the event we are on (out of possibly many)
    #"event"
    for event in pygame.event.get():
        #check to see what event it was...
        if(event.type == pygame.QUIT):
            print(event)
            game_on = False
    # screen.fill("red") #fill changes the color of the screen
    #grab our image off the hard drive and load it into pygame
    background_image = pygame.image.load('./images/background4.png')
    background_rect = background_image.get_rect()
    print(background_rect)
    #blit = block image transfer
    #blit takes 2 args: 
    #1. what to draw
    #2. where to draw it (x,y coords which we get from get_rect)
    screen.blit(background_image,background_rect)
    clock.tick(60) #the number is the fps (frame per second)
    pygame.display.flip() #DRAW OUR STUFF