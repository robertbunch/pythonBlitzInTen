
# #dictionary = a variable of variables
# #unlike lists, it has key:value pairs instead of indicies
# #like lists, it is a variable with many parts,
# #and uses [] when we want to reference it
# #like lists, you can always leave a comma after 
# #the last one

# #we can assign key:values when we make the dictionary
# country1 = {
#     "name" : "United States",
#     "population" : 35000000,
#     "capital" : "Washington D.C.",
#     # 3.14 : "What is pi doing here?" #THIS IS BAD. DONT DO THIS. It is valid, but it is confusing!
# }

# print(country1["name"]) #United States
# # print(country1["other_name"]) #this will give us a KeyError
# # print(country1[3.14])
# # print(country1[3]) #I would assume this was a list. And it's not!!
# # country1.append('Test')

# # countries = [
# #     "US", #0
# #     "Ireland", #1
# # ]

# #we can make an empty {}
# #later on we can add key:value
# user_country = {}
# user_country["name"] = "England"
# print(user_country["name"])

# user_country["population"] = input("What is your country's population? > ")
# print(user_country["population"])
# print(f"Your country is {user_country['name']} and population is {user_country['population']}")

#dictionaries + lists = WOAH.
countries_by_population = [
    {
        "name" : "India",
        "capital" : "New Delhi",
    }, #end of index 0
    {
        "name" : "China",
        "capital" : "Beijing",
    }, #end of index 1
    {
        "name" : "United States",
        "capital" : "Washington D.C."
    }, #end of index 2
]
print(f'The name of the country with the largest population in the world is {countries_by_population[0]["name"]}. The capital is {countries_by_population[0]["capital"]}')

#dictionaries + loops = WOAH.
car = {
    "make" : "Tesla",
    "model" : "S",
    "range" : "250 miles"
}
car["country_of_origin"] = "United States"

for key in car:
    #call the value of the key in a loop through 
    #a dictionary is "key"
    #in a dictionary loop, we can grab
    #a variable key by removing the ""
    print(f"Key: {key} value: {car[key]}")

# dictionaries + lists + loops = !!!!!WOAH!!!!!
for country in countries_by_population:
    #in a block of code (loop)... indentation matters!
    #country = a dictionary inside our list
    country_name = country["name"]
    country_capital = country["capital"]
    print(f"Country: {country_name} has capital {country_capital}")

#often times you will get data from a database
#in the form of a list of dictionaries
