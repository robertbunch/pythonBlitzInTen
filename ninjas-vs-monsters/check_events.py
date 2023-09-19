import pygame

def check_events():
    #check to see if if any events occured since
    #the last time through the game loop
    #call the event we are on (out of possibly many)
    #"event"
    event_data = {"game_on" : True}
    for event in pygame.event.get():
        #check to see what event it was...
        if(event.type == pygame.QUIT):
            print(event)
            event_data["game_on"] = False
    return event_data