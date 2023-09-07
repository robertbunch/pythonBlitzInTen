import random

#if the player decides to fight, this function will run
def battle_engine(enemies,the_hero):
    #randint is a method from random. It takes 2 args:
    #1. integer to start at
    #2. integer to end at
    total_enemies = len(enemies)
    # random_number = random.randint(0,total_enemies-1)
    random_index = random.randint(0,total_enemies-1)
    #we need to use the copy method, so that we don't change the original
    enemy_to_fight_og = enemies[random_index]
    # enemy_to_fight = enemies[random_index].copy()
    # print(id(enemy_to_fight_og))
    # print(id(enemies[random_index]))
    enemy_to_fight = enemy_to_fight_og.copy()
    # print(id(enemy_to_fight))
    in_fight = True #boolean that keeps us in the fight loop
    print(f"{the_hero['name']}, thou hast encountered the {enemy_to_fight['adjective']} {enemy_to_fight['name']}. The battle has begun!")
    while(in_fight):
        enemy_attack_modifier = 1 #by default the enemy does no more or less damage
        print(f"Thou hast {the_hero['hp']} health points. Thine enemy has {enemy_to_fight['hp']} health points.")
        #this loop is the back and forth during a battle. Until someone wins
        print(f"1. Attack with thine {the_hero['weapon']}.")
        health_potion_count = the_hero['inventory'].count("health_potion")
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
            hero_power_hit = the_hero['attack_power'] - enemy_to_fight['defense']
            enemy_to_fight['hp'] -= hero_power_hit
            print(f"Thou hast struck thine enemy with {the_hero['weapon']} for {hero_power_hit} damage.")
        elif(battle_action == "2"):
            #this means, players wants to drink a potion
            if(health_potion_count > 0):
                #restore all hp
                # health_potion_count -= 1 #this will not work! Because we get the count from the list in the_hero
                #remove is like append, but we pass it the value to find and remove
                the_hero['inventory'].remove('health_potion')
                the_hero['hp'] = the_hero['max_hp']
                print(f"Thou hast drank thy potion. Thine hp is restored to full. ")
            else:
                #player had no potions. Make the enemy take advantage
                print(f"Thou fool. Thou hast no potions of health, thine enemy has taken advatange of thine blunder")
                enemy_attack_modifier = 2
        elif(battle_action == "5"):
            print("Fight has ended")
            in_fight = False
    #enemy's turn, if alive   
        if(enemy_to_fight['hp'] > 0):
            #enemy is alive. Attack back.
            #monster_power_hit = take the monster's attack_power - hero's defense
            #reduce the hero's hp by monster_power_hit
            monster_power_hit = (enemy_to_fight['attack_power'] * enemy_attack_modifier)- the_hero['defense']
            print(f"Thine enemy {enemy_to_fight['name']} has struck thee with {enemy_to_fight['weapon']} for {monster_power_hit} damage.")
            the_hero['hp'] -= monster_power_hit
        else:
            #the enemy has no more hp. Fight is won for the hero
            print(f"Well done, magnificant {the_hero['name']}, thou hast slain the impudent {enemy_to_fight['name']}.")
            #the hero won, so grant the hero some gold and xp
            the_hero['gold'] += enemy_to_fight['gold_drop']
            the_hero['xp'] += enemy_to_fight['xp_drop']
            print(f"Thou has gained {enemy_to_fight['gold_drop']} gold and {enemy_to_fight['xp_drop']} experience.")
            print(f"Thou now hasts {the_hero['gold']} gold and {the_hero['xp']} experience.")
            in_fight = False #the fight is over! End the loop