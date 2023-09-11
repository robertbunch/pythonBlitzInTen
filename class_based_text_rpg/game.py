# from Character import Character
from Hero import Hero #Hero is a subclass of Character
from GameSettings import GameSettings
from battle_engine_function import battle_engine
from Shop import Shop

shop = Shop()
game_settings = GameSettings()
charater_name = input("What is thy name, brave adventurer? > ")
the_hero = Hero(charater_name, xp = 0, level = 1, 
                     gold = 5, attack_power = 10,
                     defense = 2, max_hp = 10, hp = 10, 
                     weapon = "fists", 
                     inventory = ['health_potion'],
                     game_settings = game_settings)

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
        if(the_hero.hp <= 0):
            print(f"All hope is lost...")
            game_on = False
            #game over :(
    elif(action == "2"):
        #player has chosen to enter the shop
        shop.display(the_hero,game_settings) #run the display method on our shop object. Pass the hero object, and the game_settings object
    elif(action == "q"):
        game_on = False