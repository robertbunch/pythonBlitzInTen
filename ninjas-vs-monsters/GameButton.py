import pygame.font

class GameButton():
    def __init__(self,screen,button_text,text_color,
                 background_color,location_x,location_y,
                 button_height,button_width,font_size,
                 center_on_screen):
        self.screen = screen
        self.background_color = background_color
        self.font = pygame.font.Font(None,font_size)
        self.rect = pygame.Rect(0,0,button_width,button_height)
        if(center_on_screen):
            self.screen_rect = self.screen.get_rect()
            self.rect.center = self.screen_rect.center
        else:
            self.rect.x = location_x
            self.rect.y = location_y
        self.msg_image = self.font.render(button_text,True,text_color,background_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    def draw_me(self):
        self.screen.fill(self.background_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
