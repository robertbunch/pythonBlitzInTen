#random is a "CORE" module that comes with python
#it has some cool methods to generate random numbers
import random
#game_data is where our data lives at. We can access it quickly and easily
#but it is out of the way the rest of time
import game_data
#the entry point (this is the file we run python on)
#for our text based RPG

game_data.the_hero["name"] = input("What is thy name, brave adventurer? > ")

#if the player decides to fight, this function will run
def fight():
    #randint is a method from random. It takes 2 args:
    #1. integer to start at
    #2. integer to end at
    total_enemies = len(game_data.enemies)
    # random_number = random.randint(0,total_enemies-1)
    random_index = random.randint(0,total_enemies-1)
    enemy_to_fight = game_data.enemies[random_index]
    in_fight = True #boolean that keeps us in the fight loop
    while(in_fight):
        print(f"{game_data.the_hero['name']}, thou hast encountered the {enemy_to_fight['adjective']} {enemy_to_fight['name']}. The battle has begun!")
        battle_action = input("What would you like to do? > ") #this is the chioce the player will make in the fight
        print("Fight has ended")
        in_fight = False

#make a boolean that will control our main game loop
game_on = True
while(game_on):
    print(f"What would you like to do, {game_data.the_hero['name']}?")
    for option in game_data.main_options:
        print(f"{option['input_key']}. {option['text']}")
    action = input(" > ") #this will BLOCK the loop, until the user answer
    if(action == "1"):
        fight()
    elif(action == "q"):
        game_on = False

