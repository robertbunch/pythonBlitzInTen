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
    print(f"{game_data.the_hero['name']}, thou hast encountered the {enemy_to_fight['adjective']} {enemy_to_fight['name']}. The battle has begun!")
    while(in_fight):
        print(f"Thou hast {game_data.the_hero['hp']} health points. Thine enemy has {enemy_to_fight['hp']} health points.")
        #this loop is the back and forth during a battle. Until someone wins
        print(f"1. Attack with thine {game_data.the_hero['weapon']}.")
        health_potion_count = game_data.the_hero['inventory'].count("health_potion")
        print(f"2. Drink the health potion. Thou hast {health_potion_count} potions.")
        print(f"3.Defend and heal.")
        print(f"4. Do a little dance.")
        print(f"5. Flee for your miserable, pitiful life.")
        battle_action = input("What would you like to do? > ") #this is the chioce the player will make in the fight
    #hero's turn
        if(battle_action == "1"):
            #user has chosen to attack
            #hero_power_hit = take the hero's attack_power - monster's defense
            #reduce the monster's hp by hero_power_hit
            hero_power_hit = game_data.the_hero['attack_power'] - enemy_to_fight['defense']
            enemy_to_fight['hp'] -= hero_power_hit
        elif(battle_action == "5"):
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

