

class GameSettings():
    def __init__(self):
        self.main_options = [
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
        #levels is where we keep {} for each level
        self.levels = [
            {}, #0
            {}, #1
            {
                "threshold" : 15, #amount of xp to go to this level
                "attack_increase" : 2,
                "defense_increase" : 1,
                "hp_increase" : 7,
            }, #2
            {
                "threshold" : 35, #amount of xp to go to this level
                "attack_increase" : 2,
                "defense_increase" : 1,
                "hp_increase" : 9,
            }, #3         
            {
                "threshold" : 80, #amount of xp to go to this level
                "attack_increase" : 3,
                "defense_increase" : 2,
                "hp_increase" : 10,
            }, #4               
        ]        
        self.colors = {
            #Colors for Python terminal
            "red" :  "\033[1;31;40m",
            "redB" :  "\033[0;31;47m",
            "white" :  "\033[1;37;40m",
            "blue" :  "\033[1;34;40m",
            "blueB" :  "\033[0;34;47m",
            "yellow" :  "\033[1;33;40m",
            "green" :  "\033[1;32;40m",
            "greenB" :  "\033[0;32;47m",
            "normal" : "\033[0;37;40m",
        }   