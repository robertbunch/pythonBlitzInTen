import pygame

def check_events(player,tick):
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
                # player.y += 10
                player.should_move("down",True)
            elif(event.key == pygame.K_UP):
                # The user pressed the up arrow!
                player.should_move("up",True)
            elif(event.key == pygame.K_RIGHT):
                # The user pressed the right arrow!
                player.should_move("right",True)
            elif(event.key == pygame.K_LEFT):
                # The user pressed the left arrow!  
                player.should_move("left",True)
            elif(event.key == pygame.K_SPACE):
                #player hit the space bar... ATTACK!
                #it's not check_events job to mess with the player
                #that's the player's job. check_events lets the 
                #player know what happened
                player.attack(tick)
            elif(event.key == pygame.K_d):
                #if "d" key is pressed, run dead animation
                player.dead()    
            elif(event.key == pygame.K_j):
                #if "d" key is pressed, run jump animation
                player.jump()                    
        elif(event.type == pygame.KEYUP):
            #user released a key... what key is it?
            if(event.key == pygame.K_DOWN):
                #the down arrow!
                player.should_move("down",False)
            elif(event.key == pygame.K_UP):
                player.should_move("up",False)
            elif(event.key == pygame.K_LEFT):
                player.should_move("left",False)
            elif(event.key == pygame.K_RIGHT):
                player.should_move("right",False)                                
    return event_data