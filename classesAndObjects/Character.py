
#self is a special key word that is used to reference
#the object's stuff. It is used in the class, NOT
#by the object, becuase the object knows it's variable name (the_hero, goblin, zombie)
#the class just knows it's an object, so thje class
#must use "self" to reference the object

class Character():
    #python has dunder method
    #dunder = a method that starts and ends with __
    #dunder methods run at special times, i.e. we do not call them
    def __init__(self,character_name):
        #init is a dunder method that belongs in a class
        #it is also known in oop as the constructor method
        #it runs ONE time. When a new object is created
        self.name = character_name
        self.hp = 10

    #all methods in a class MUST take self as the first param
    def print_name(self):
        # global name #global is ALWAYS neccessary if the variable is not defined localally
        print(f"Hello from Character class, {self.name}")


