

#like all varaibles, strings have methods
#that make life better

#Mutation = does the thing change or not.
#when it comes to methods, does the method
# "mutate" the varaible, or does it take the varaible
# do something with it, and return the value
a_string = "i love python"
cap_string = a_string.capitalize() #capitalize will return the string with the first letter capitalized
print(cap_string)
print(a_string)

#a way to use a method that does not mutate, to mutate
a_string = a_string.title() # cap each letter 
print(a_string)

#lower = make every letter lower case in the string
a_string = a_string.lower()
print(a_string)

#upper = make every letter upper case in the string
a_string = a_string.upper()
print(a_string)

#find = you know. It gets the index of the character
print(a_string.find("l"))
print(a_string.find("L"))

#count = returns the number of times a character appears
print(a_string.count("P"))

#replace = hand it what to look for, and what to replae it with
#an optional 3rd arg, is how many times to change
a_string = "I think Python is fun fun fun fun!"
a_string = a_string.replace("fun", "hard", 2)
print(a_string)