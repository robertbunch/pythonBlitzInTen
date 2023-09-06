from Character import Character

#the_hero is an object. What type of object? A Character object
#Character is the class
the_hero = Character("Axe")
goblin = Character("a simple goblin")
zombie = Character("a brain seeking zombie")
print(the_hero)
print(f"The hero has {the_hero.hp} hp.")
#unlike dictionaries, we can go straight to our
# "attributes" which are variables and methods/functions
#we use . to get to our object "stuff"

#python, whether we like it or not, is ALWAYS
#going to send "self" to any object method
the_hero.print_name() #uhh, do we pass it something here, or not?
goblin.print_name()
zombie.print_name()
print(the_hero.name) #self.name in the class, variable_name.name in the place where the object exists