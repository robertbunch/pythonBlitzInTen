class Shop():
    def __init__(self):
        self.items = [
            {
                "item_name" : "Health Potion",
                "py_name" : "health_potion",
                "desc" : "Refresh all hit points",
                "cost" : 10,
            },
            {
                "item_name" : "Magic Sword",
                "py_name" : "magic_sword",
                "desc" : "Attack Power +15%",
                "cost" : 50,
            },
            {
                "item_name" : "Magic Armor",
                "py_name" : "magic_armor",
                "cost" : 50,
                "desc" : "Defense +15%",
            },
            {
                "item_name" : "Evasion Potion",
                "py_name" : "evasion_potion",
                "cost" : 20,
                "desc" : "+20% chance to evade attack",
            },
            {
                "item_name" : "Magic Carpet",
                "py_name" : "magic_carpet",
                "cost" : 30,
                "desc" : "Guarantee fight escape",
            },
            {
                "item_name" : "Leave",
                "py_name" : "leave",
                "cost" : "",
                "desc" : "Leave the shop",
            },
        ]
    def display(self,hero,game_settings):
        #display the shop options to the player
        keep_shopping = True #bool to keep the shop loop running
        while(keep_shopping):
            print(f"Thou hast entered the shop with {game_settings.colors['yellow']}{hero.gold} gold{game_settings.colors['normal']}.")
            counter = 0
            for item in self.items:
                counter += 1 #counter is to give the user the number to push
                #each item is a {} in self.items
                print(f"{counter}. {item['item_name']}, {item['cost']} - {item['desc']}")
            
            keep_shopping = False