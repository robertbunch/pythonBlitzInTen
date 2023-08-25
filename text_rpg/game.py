
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

enemies = []
zombie = {
    "name" : "Zombie",
    "hp" : 10,
    "attack_power" : 3,
    "defense" : 0,
    "weapon" : "fist",
    "xp_drop" : 2, #this is how much xp the bad guy gives the hero when defeated
    "gold_drop" : 1,
    "power" : {
        "name" : "Berzerk",
        "effect" : "attack_up",
        "effect_impact" : 5,
    }
}

enemies.append(zombie)

main_options = [
    {
        "text" : "Go into the dark forest in search of adventure and loot",
        "input_key" : "1",
    },
    {
        "text" : "Go to the shop",
        "input_key" : "2",
    },
    {
        "text" : "Do a dance",
        "input_key" : "3"
    },
    {
        "text" : "Sleep and adventure another day (exit)",
        "input_key" : "q"
    }
]

#if the player decides to fight, this function will run
def fight():
    enemy_to_fight = enemies[0]
    in_fight = True #boolean that keeps us in the fight loop
    while(in_fight):
        print(f"{the_hero['name']}, thou hast encountered the fearsome {enemy_to_fight['name']}. The battle has begun!")
        battle_action = input("What would you like to do? > ") #this is the chioce the player will make in the fight
        print("Fight has ended")
        in_fight = False

#make a boolean that will control our main game loop
game_on = True
while(game_on):
    print(f"What would you like to do, {the_hero['name']}?")
    for option in main_options:
        print(f"{option['input_key']}. {option['text']}")
    action = input(" > ") #this will BLOCK the loop, until the user answer
    if(action == "1"):
        fight()
    elif(action == "q"):
        game_on = False


