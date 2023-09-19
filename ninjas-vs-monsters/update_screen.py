
#this function is in charge of updating stuff
#on the screen

def update_screen(screen,player,background):
    background.draw_bg(screen)
    player.move_player(screen)
    return
