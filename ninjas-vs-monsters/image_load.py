import pygame

def player_image_load():
    image_types = {
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

    for image_type in image_types:
        for i in range(0,10):
            image_to_load = pygame.image.load(f"./images/ninja/{image_type}__00{i}.png")
            image_to_load = pygame.transform.scale_by(image_to_load,.35)
            image_types[image_type].append(image_to_load)
    return image_types

def monster_image_load(monster_name):
    image_types = {
        "ATTAK" : [],
        "DIE" : [],
        "IDLE" : [],
        "HURT" : [],
        "JUMP" : [],
        "RUN" : [],
        "WALK" : [],
    }
    for image_type in image_types:
        for i in range(0,7):
            image_to_load = pygame.image.load(f"./images/{monster_name}/{image_type}/{image_type}_00{i}.png")
            image_to_load = pygame.transform.scale_by(image_to_load,.35)
            image_types[image_type].append(image_to_load)
    return image_types