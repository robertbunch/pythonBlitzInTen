import game_data
#the entry point (this is the file we run python on)
#for our text based RPG

game_data.the_hero["name"] = input("What is thy name, brave adventurer? > ")

#if the player decides to fight, this function will run
def fight():
    enemy_to_fight = game_data.enemies[0]
    in_fight = True #boolean that keeps us in the fight loop
    while(in_fight):
        print(f"{game_data.the_hero['name']}, thou hast encountered the fearsome {enemy_to_fight['name']}. The battle has begun!")
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

