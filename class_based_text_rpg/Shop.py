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
                "cost" : 1,
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
        annoy_tries = 0
        while(keep_shopping):
            print(f"Thou hast entered the shop with {game_settings.colors['yellow']}{hero.gold} gold{game_settings.colors['normal']}.")
            counter = 0
            for item in self.items:
                counter += 1 #counter is to give the user the number to push
                #each item is a {} in self.items
                print(f"{counter}. {item['item_name']}, {item['cost']} - {item['desc']}")
            shop_action = input("The keeper of the shop is gruff and short with you. Well? What do you want? > ")
            #to get the index in self.items that matches what the user entered, we -1 because the indicies start at 0
            index_in_items = int(shop_action) - 1
            #get the item from self.items based on the index
            item_to_buy = self.items[index_in_items]
            #did the player choose to leave
            if(item_to_buy['py_name'] == "leave"):
                keep_shopping = False
            #does the user have the money to buy the item?
            elif(hero.gold >= item_to_buy["cost"]):
                #the user has enough gold!
                hero.gold -= item_to_buy["cost"] #reduce the amount of gold the hero has... ie. pay for the time
                if(item_to_buy['py_name'] == "health_potion"):
                    hero.inventory.append('health_potion')
                elif(item_to_buy['py_name'] == "magic_sword"):
                    hero.set_weapon(item_to_buy['item_name'])
                elif(item_to_buy['py_name'] == "magic_armor"):
                    hero.set_armor(item_to_buy['item_name'])
                print(f"{game_settings.colors['blue']}{item_to_buy['item_name']}{game_settings.colors['normal']} has been added to your inventory!")
            else:  
                #the user does NOT have enough gold
                annoy_tries += 1 #each time the player tries to buy something they do not have the money for, increase annoy_tries
                if(annoy_tries == 1):
                    #just one time making a mistake
                    print(f"The keeper responds, 'dont waste my time. Go earn some coin, and come back'")
                elif(annoy_tries == 2):
                    print(f"{game_settings.colors['blue']}The shop owner eyes you angrily... You cannot afford that item.{game_settings.colors['normal']}")
                elif(annoy_tries == 3):
                    print(f"{game_settings.colors['red']}The shopkeeper howls. He grabs you by the coller and throws you out of the shop!{game_settings.colors['normal']}")
                    keep_shopping = False
