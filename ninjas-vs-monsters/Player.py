import pygame
#images from https://opengameart.org/content/ninja-adventure-free-sprite
class Player():
    def __init__(self,screen):
        self.screen = screen
        self.x = 200
        self.y = 200
        # anim_image is the number cooresponding to the number in the filename of the that image
        self.anim_image = 0
        self.image_type = "Idle"
        self.stop_attacking_at = False
        self.should_move_up = False
        self.should_move_down = False
        self.should_move_left = False
        self.should_move_right = False

        self.image_types = {
            "Attack" : [],
            "Dead" : [],
            "Idle" : [],
            "Jump" : [],
            "Jump_Attack" : [],
            "Jump_Throw" : [],
            "Run" : [],
            "Slide" : [],
            "Throw" : [],
        }

        for image_type in self.image_types:
            for i in range(0,10):
                image_to_load = pygame.image.load(f"./images/ninja/{image_type}__00{i}.png")
                image_to_load = pygame.transform.scale_by(image_to_load,.35)
                self.image_types[image_type].append(image_to_load)
        # print(self.image_types)
        #load the image from the hd
        self.image = pygame.image.load("./images/ninja/Idle__000.png")
        self.image = pygame.transform.scale_by(self.image,.35)
        #get the coords of the image
        self.rect = self.image.get_rect() 
    def draw_player(self,screen,tick,display_info):
        # print(tick)
        #when we draw the player, we can decide
        #where the player should be
        if(self.should_move_up and self.y > 0):
            self.y -= 10
        elif(self.should_move_down and (self.y + self.rect.height) < display_info.current_h):
            self.y += 10
        ##cannot go up and down at the same time
        ##but can go left/right AND down/up at the same time
        ##so use 2 different if statements
        if(self.should_move_left and self.x > 0):
            self.x -= 10
        elif(self.should_move_right and (self.x + self.rect.width) < display_info.current_w):
            self.x += 10
        #the tick is updated everytime through the game loop
        #that is A LOT. We can use it to do "time things"
        if(tick % 5 == 0):
            #anim_image only changes every 5 ticks
            self.anim_image += 1
            if(self.anim_image == 10):
                #we only have 0-9 images, so 10 is too far
                self.anim_image = 0
        #check to see if the player is attacking, AND it's time to stop
        if(self.image_type == "Attack" and tick > self.stop_attacking_at):
            self.image_type = "Idle" #the attack is done. Go into idle
        #image_types is a dictionary of all possible image_types
        #image_type is a particular image_type such as run, idle, or attack
        #anim_image is a particular image of a particular image_type
        cur_image = self.image_types[self.image_type][self.anim_image]
        if(self.should_move_left):
            #the player is moving left... flip image
            #only time we flip
            cur_image = pygame.transform.flip(cur_image,True,False)
        #blit draws the player
        screen.blit(cur_image,(self.x,self.y))
    def should_move(self, direction, move_or_not):
        #if the user is running, i.e. move_or_not is true
        #we want to set the image_type to run
        #BUT ONLY if the player is not in the middle of an attack
        if(self.image_type == "Attack"):
            #return will kill the function in its tracks
            return
        if(move_or_not):
            self.image_type = "Run"
        else:
            #if move_or_not is false then the user has
            #let go of an arrow key, and he should idle
            self.image_type = "Idle"
        if(direction == "up"):
            self.should_move_up = move_or_not
        elif(direction == "down"):
            self.should_move_down = move_or_not
        elif(direction == "left"):
            self.should_move_left = move_or_not
        elif(direction == "right"):
            self.should_move_right = move_or_not
    def attack(self,tick):
        #All things attack happen here... like, did we hit something?
        #set the image_type
        self.image_type = "Attack"
        #reset the animation_image to 0 because we want to start from the beginning
        self.anim_image = 0
        #how long does it take for an animation to complete?
        #we have 10 images. Each image lasts for 5 ticks
        #that means lock the player for 50 ticks
        self.stop_attacking_at = tick + 50
    def dead(self):
        self.image_type = "Dead"
    def jump(self):
        self.image_type = "Jump"