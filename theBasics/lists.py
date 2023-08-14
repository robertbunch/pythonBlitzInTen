
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


animals = ["Dog","Elephant","Cat"]
list_of_different_dt = [
    "Joe",
    4,
    3.14,
    True,
    [1,2,3]
]
print(list_of_different_dt)
