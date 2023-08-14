
# A list is a "list" of variables
# they are grouped together for some reason
    # maybe came from a backend (api, database)
    # maybe they are a logical group (countries, animals, etc)
    # maybe they need to be looped through
# they come with some awesome tools

empty_list = []
# print(type(empty_list))
countriesByPop = [
    "India", #this is index 0
    "China", #1
    "US", #2
    "Indonesia", #3
]
print(countriesByPop[3])

#len() whatever is in the () len will try and find how many items there
print(f"The length of countriesByPop is: {len(countriesByPop)}.")

#lists have methods!! 
#what is a method? A method is some code that
#python has written/built into the language
#that works on a variable/data type/data structure (class/object)

#the append method belongs to all lists
#that means if you are a list, you can run .append()
#whatever is inside of the () is what you will add
#to the end of this list
countriesByPop.append('Pakistan')
print(f"The length of countriesByPop is now: {len(countriesByPop)}.")
print(countriesByPop)
print("======================")

#insert method
#is some code that Python has given us for our lists
#if you're a list, you have the insert method
#you can do a_list.insert()
#we pass insert 2 things, 1. The place to insert, 2. the variable to insert
countriesByPop.insert(4,"Nigeria")
print(countriesByPop)
print("=====================")

#let's say a new country called "pythonmania" came into being
countriesByPop.insert(0,"Pythonmania")
print(countriesByPop)
print("=====================")


#pop and remove
#if you're a list, you have the pop and remove methods
#pop = remove the specified index from the list
#we pass the .pop() the index we want to remove
countriesByPop.pop(0) #this will remove from the list the thing in spot 0 (the first element)
print(countriesByPop)
print("=====================")


#remove is like pop, but instead of giving it/passing
#an index, we pass a value
countriesByPop.append("AI")
print(countriesByPop)
countriesByPop.remove("AI") #instead of the index, we give it the value
print(countriesByPop)


animals = ["Dog","Elephant","Cat"]
list_of_different_dt = [
    "Joe",
    4,
    3.14,
    True,
    [1,2,3]
]
print(list_of_different_dt)
