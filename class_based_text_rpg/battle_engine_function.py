import random
# from Character import Character
from Monster import Monster #Monster is a subclass of Character
import time #part of core
import os #os is part of core, stands for operating system
from Troll import Troll
from Zombie import Zombie
from Goblin import Goblin

#if the player decides to fight, this function will run
def battle_engine(the_hero):
    #inside of battle_engine, make some enemies
    troll = Troll()
    goblin = Goblin()
    zombie = Zombie()
    # zombie = Monster(character_name="Zombie",xp_drop = 2,
    #                 gold_drop = 5, attack_power=5, defense = 2,
    #                 max_hp=7, hp = 9, weapon="fists",)
    enemies = [goblin, zombie, troll]
    random_list = ([0] * 5) + ([1] * 4) + [2]
    # [0,0,0,0,0,1,1,1,1,2]

    # os.system('cls') #this is for windows
    os.system('clear') #this is for Mac
    #time.sleep(x) will force the program to stop for x seconds
    print(f"Thou hast entered the forest. Danger creeps everywhere...")
    time.sleep(2) #pause for 2 seconds

    # os.system("say Hooray, Hero!")

    #randint is a method from random. It takes 2 args:
    #1. integer to start at
    #2. integer to end at
    total_enemies = len(enemies)
    # random_number = random.randint(0,total_enemies-1)
    # random_index = random.randint(0,total_enemies-1)
    random_index = random.choice(random_list)
    #we need to use the copy method, so that we don't change the original
    enemy_to_fight = enemies[random_index]
    in_fight = True #boolean that keeps us in the fight loop
    print(f"{the_hero.character_name}, thou hast encountered the {enemy_to_fight.character_name}. The battle has begun!")
    while(in_fight):
        print(f"Thou hast {the_hero.hp} health points. Thine enemy has {enemy_to_fight.hp} health points.")
        #this loop is the back and forth during a battle. Until someone wins
        print(f"1. Attack with thine {the_hero.weapon}.")
        health_potion_count = the_hero.inventory.count("health_potion")
        print(f"2. Drink the health potion. Thou hast {health_potion_count} potions.")
        print(f"3. Defend and heal.")
        print(f"4. Do a little dance.")
        print(f"5. Flee for your miserable, pitiful life.")
        battle_action = input("What would you like to do? > ") #this is the chioce the player will make in the fight
    #hero's turn
        if(battle_action == "1"):
            #the_hero has chosen to attack
            power_hit = enemy_to_fight.take_damage(the_hero)
            print(f"Thou hast struck thine enemy with {the_hero.weapon} for {power_hit} damage.")
        elif(battle_action == "2"):
            #this means, players wants to drink a potion
            if(health_potion_count > 0):
                #restore all hp
                # health_potion_count -= 1 #this will not work! Because we get the count from the list in the_hero
                #remove is like append, but we pass it the value to find and remove
                the_hero.inventory.remove('health_potion')
                the_hero.hp = the_hero.max_hp
                print(f"Thou hast drank thy potion. Thine hp is restored to full. ")
            else:
                #player had no potions. Make the enemy take advantage
                print(f"Thou fool. Thou hast no potions of health, thine enemy has taken advatange of thine blunder")
                enemy_to_fight.damage_modifier = 2
                the_hero.defense_modifier = 1 #reset the defense mod for the hero to 1
        elif(battle_action == "3"):
            #player has chosen to heal and defend
            the_hero.defense_modifier = 2
        elif(battle_action == "5"):
            print("Fight has ended")
            in_fight = False
            return #return will keep the enemy from getting a chance to attack
    #enemy's turn, if alive   
        if(enemy_to_fight.hp > 0):
            #enemy is alive. Attack back.
            power_hit = the_hero.take_damage(enemy_to_fight)
            print(f"Thine enemy {enemy_to_fight.character_name} has struck thee with {enemy_to_fight.weapon} for {power_hit} damage.")
            #check to see if hero has hp > 0
            #if not... break out of the fight loop
            if(the_hero.hp <= 0):
                in_fight = False
                print(f"Thou hast been slain by {enemy_to_fight.character_name}")
        else:
            #the enemy has no more hp. Fight is won for the hero
            the_hero.battle_victory(enemy_to_fight)
            in_fight = False #the fight is over! End the loop