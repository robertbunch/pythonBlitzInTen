import pygame
#images from https://opengameart.org/content/ninja-adventure-free-sprite
class Player():
    def __init__(self,screen):
        self.screen = screen
        self.x = 200
        self.y = 200
        # anim_image is the number cooresponding to the number in the filename of the that image
        self.anim_image = 0
        self.should_move_up = False
        self.should_move_down = False
        self.should_move_left = False
        self.should_move_right = False

        self.image_types = {
            "Idle" : [],
            "Run" : [],
        }

        for image_type in self.image_types:
            for i in range(0,10):
                image_to_load = pygame.image.load(f"./images/ninja/{image_type}__00{i}.png")
                image_to_load = pygame.transform.scale_by(image_to_load,.35)
                self.image_types[image_type].append(image_to_load)
        print(self.image_types)
        #load the image from the hd
        self.image = pygame.image.load("./images/ninja/Idle__000.png")
        self.image = pygame.transform.scale_by(self.image,.35)
        #get the coords of the image
        self.rect = self.image.get_rect() 
    def draw_player(self,screen):
        #when we draw the player, we can decide
        #where the player should be
        if(self.should_move_up):
            self.y -= 10
        elif(self.should_move_down):
            self.y += 10
        ##cannot go up and down at the same time
        ##but can go left/right AND down/up at the same time
        ##so use 2 different if statements
        if(self.should_move_left):
            self.x -= 10
        elif(self.should_move_right):
            self.x += 10            
        #blit draws the player
        screen.blit(self.image_types["Run"][self.anim_image],(self.x,self.y))
    def should_move(self, direction, move_or_not):
        if(direction == "up"):
            self.should_move_up = move_or_not
        elif(direction == "down"):
            self.should_move_down = move_or_not
        elif(direction == "left"):
            self.should_move_left = move_or_not
        elif(direction == "right"):
            self.should_move_right = move_or_not
        