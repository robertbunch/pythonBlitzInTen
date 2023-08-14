
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

animals = ["Dog","Elephant","Cat","Dog"]
# print(animals)
#clear method = this burns everything in the array
#it is essentially the equiv of starting over from scratch
#we dont need to pass clear anything
# animals.clear()
# animals = []
# print(animals)

#count method
#count will "count" the number of times a thing shows up in a list
number_of_dogs = animals.count("dog")
print(number_of_dogs)

#sort and reverse
#sort method = will sort the list in natural order
#we don't have it anything for natural order, we do pass it something for control (later)
animals.sort()
print(animals)

#cannot mix data types
# list_of_numbers = [1,3,6,4,2,6,"Hello",2,7,81,3,4] THIS WILL BREAK
list_of_numbers = [1,3,6,4,2,6,2,7,81,3,4]
list_of_numbers.sort()
print(list_of_numbers)

list_of_different_dt = [
    "Joe",
    4,
    3.14,
    True,
    [1,2,3]
]

#reverse method = switch the order of the indicides exactly
list_of_different_dt.reverse()
print(list_of_different_dt)
