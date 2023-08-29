the_hero = {
    "name" : "Incognito",
    "xp" : 0, #use xp to determine when level up
    "level" : 1,
    "gold" : 5, #amount of money the player has to buythings
    "attack_power" : 5,
    "defense" : 2,
    "max_hp" : 10, #this is for reference and will only change when the player levels up
    "hp" : 10, #this hp mutates as the player is hurt or heals
    "weapon" : "fists",
    "inventory" : ["health_potion",]
}

zombie = {
    "name" : "Zombie",
    "adjective" : "fearsome",
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

goblin = {
    "name" : "Goblin",
    "adjective" : "meek",
    "hp" : 8,
    "attack_power" : 4,
    "defense" : 1,
    "weapon" : "fist",
    "xp_drop" : 2, #this is how much xp the bad guy gives the hero when defeated
    "gold_drop" : 1,
    "power" : {
        "name" : "Call For Help",
        "effect" : "hp_up",
        "effect_impact" : 10,
    }
}

enemies = [zombie,goblin]
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