from Character import Character
from GameSettings import GameSettings
from battle_engine_function import battle_engine

game_settings = GameSettings()
charater_name = input("What is thy name, brave adventurer? > ")
the_hero = Character(charater_name, xp = 0, level = 1, 
                     gold = 5, attack_power = 10,
                     defense = 5, max_hp = 10, hp = 10, 
                     weapon = "fists", 
                     inventory = ['health_potion'])

#make a boolean that will control our main game loop
game_on = True
while(game_on):
    print(f"What would you like to do, {the_hero.character_name}?")
    for option in game_settings.main_options:
        print(f"{option['input_key']}. {option['text']}")
    action = input(" > ") #this will BLOCK the loop, until the user answer
    if(action == "1"):
        #call the battle engine
        battle_engine(the_hero)
    elif(action == "q"):
        game_on = False