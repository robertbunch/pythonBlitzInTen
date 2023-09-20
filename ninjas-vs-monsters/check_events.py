import pygame

def check_events(player):
    #check to see if if any events occured since
    #the last time through the game loop
    #call the event we are on (out of possibly many)
    #"event"
    event_data = {"game_on" : True}
    for event in pygame.event.get():
        # print(event)
        #check to see what event it was...
        if(event.type == pygame.QUIT):
            event_data["game_on"] = False
        elif(event.type == pygame.KEYDOWN):
            # the user pressed a key!
            # print(event.key)
            if(event.key == pygame.K_DOWN):
                # The user pressed the down arrow!
                print("User hit the down arrow")
                # move the player object in the 
                # positive y direction
                player.y += 10
            elif(event.key == pygame.K_UP):
                # The user pressed the up arrow!
                print("User hit the up arrow")
                # we want to move the player y position negative
                player.y -= 10
            elif(event.key == pygame.K_RIGHT):
                # The user pressed the up arrow!
                print("User hit the right arrow")
                player.x += 10
            elif(event.key == pygame.K_LEFT):
                # The user pressed the up arrow!  
                print("User hit the left arrow")   
                player.x -= 10   
            player.anim_image += 1
            if(player.anim_image == 10):
                player.anim_image = 0
    return event_data