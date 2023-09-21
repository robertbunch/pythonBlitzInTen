
#this function is in charge of updating stuff
#on the screen

def update_screen(screen,player,background,tick):
    background.draw_bg(screen)
    player.draw_player(screen,tick)
    return
