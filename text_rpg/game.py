#random is a "CORE" module that comes with python
#it has some cool methods to generate random numbers
import random
#game_data is where our data lives at. We can access it quickly and easily
#but it is out of the way the rest of time
import game_data
from battle_engine import battle_engine
#the entry point (this is the file we run python on)
#for our text based RPG

game_data.the_hero["name"] = input("What is thy name, brave adventurer? > ")

#make a boolean that will control our main game loop
game_on = True
while(game_on):
    print(f"What would you like to do, {game_data.the_hero['name']}?")
    for option in game_data.main_options:
        print(f"{option['input_key']}. {option['text']}")
    action = input(" > ") #this will BLOCK the loop, until the user answer
    if(action == "1"):
        battle_engine() #renamed fight to battle_engine since it's a better varaible name
    elif(action == "q"):
        game_on = False

