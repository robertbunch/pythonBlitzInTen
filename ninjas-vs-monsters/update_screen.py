
#this function is in charge of updating stuff
#on the screen

def update_screen(screen,player,background,tick,display_info):
    background.draw_bg(screen)
    player.draw_player(screen,tick,display_info)
    return
