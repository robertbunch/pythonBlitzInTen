

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
