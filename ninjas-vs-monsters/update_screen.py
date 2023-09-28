from pygame.sprite import spritecollide

#this function is in charge of updating stuff
#on the screen

def update_screen(screen,player,background,tick,display_info,monsters):
    background.draw_bg(screen)

    #collision detection!
    #spritecollide takes 3 args:
    #1. the sprite to collide wtih
    #2. the group to collide with the sprite
    #3. should the sprite in the group, be removed on collision
    #retrun value is all sprites in teh group that were collided with 
    hit_monsters = spritecollide(player,monsters,False)
    for monster in hit_monsters:
        # print("monster collided with!")
        #stop the monster from moving
        #start attacking/hurt/die animation
        #take and cause damage
        if(monster.image_type != "ATTAK"):
            #only run stop_and_attack if teh monster is NOT attacking already
            monster.stop_and_attack()
        elif(player.image_type == "Attack" and player.anim_image == 0 and tick % 5 == 0):
            #the player is attacking and the monster is colliding. 
            # Take damage! But only if the player is on the first animation
            #and the first animation is on the first tick
            print("Player has hit the monster")
    #for all the monsters that WERE attacking, but are 
    #no longer colliding, we need to start them up again
    for monster in monsters:
        if(monster.image_type == "ATTAK" and monster not in hit_monsters):
            #this monster is a NON collided with monster
            #and this monster IS attacking
            #We need to start him moving again
            monster.move_on()
    player.draw_player(screen,tick,display_info)
    for monster in monsters:
        monster.draw_monster(screen, tick)
    return
