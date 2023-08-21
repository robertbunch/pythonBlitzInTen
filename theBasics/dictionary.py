
#dictionary = a variable of variables
#unlike lists, it has key:value pairs instead of indicies
#like lists, it is a variable with many parts,
#and uses [] when we want to reference it
#like lists, you can always leave a comma after 
#the last one

country1 = {
    "name" : "United States",
    "population" : 35000000,
    "capital" : "Washington D.C.",
    # 3.14 : "What is pi doing here?" #THIS IS BAD. DONT DO THIS. It is valid, but it is confusing!
}

print(country1["name"]) #United States
# print(country1["other_name"]) #this will give us a KeyError
# print(country1[3.14])
# print(country1[3]) #I would assume this was a list. And it's not!!
# country1.append('Test')


