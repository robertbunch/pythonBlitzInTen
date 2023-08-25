
#the entry point (this is the file we run python on)
#for our text based RPG

hero_name = input("What is thy name, brave adventurer? > ")

the_hero = {
    "name" : hero_name,
    "xp" : 0, #use xp to determine when level up
    "level" : 1,
    "gold" : 5, #amount of money the player has to buythings
    "attack_power" : 5,
    "defense" : 2,
    "hp" : 10,
    "weapon" : "fists",
    "inventory" : ["health_potion",]
}

#make a boolean that will control our main game loop
game_on = True
while(game_on):
    print(f"What would you like to do, {the_hero['name']}?")
    print(f"1. Fight a monster")
    print(f"2. Go to the shop")
    print(f"3. Do a dance")
    action = input(" > ") #this will BLOCK the loop, until the user answer
    if(action == "3"):
        game_on = False


