from Character import Character
from GameSettings import GameSettings

game_settings = GameSettings()
charater_name = input("What is thy name, brave adventurer? > ")
the_hero = Character(charater_name, xp = 0, level = 1, 
                     gold = 5, attack_power = 10,
                     defense = 5, max_hp = 10, hp = 10, 
                     weapon = "fists", 
                     inventory = ['health_potion'])
goblin = Character(character_name="Goblin",xp = 0, level = 1,
                   gold = 5, attack_power=3, defense = 3,
                   max_hp=7, hp = 7, weapon="fists",
                   inventory=[])
zombie = Character(character_name="Zombie",xp = 0, level = 1,
                   gold = 5, attack_power=5, defense = 2,
                   max_hp=7, hp = 9, weapon="fists",
                   inventory=[])
enemies = [goblin,zombie]

#make a boolean that will control our main game loop
game_on = True
while(game_on):
    print(f"What would you like to do, {the_hero.character_name}?")
    for option in game_settings.main_options:
        print(f"{option['input_key']}. {option['text']}")
    action = input(" > ") #this will BLOCK the loop, until the user answer