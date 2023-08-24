
#tuples and sets are built in data types in Python
#tuple = a list that CANNOT be changed. Immutable
#tuple unlike lists which use [] use ()
vowels = ("a","e","i","o","u","a")
# print(vowel[0])
# print(type(vowel))
#you can make them without ()... this is BAD
a_tuple = 1, 2, 3 #DONT DO THIS. Use ()
# print(type(a_tuple))

#tuples are iterable because they ALWAYS have the same order
#in programming this is called a discrete structure
for v in vowels:
    print(v)

# vowels.append("a")
# vowels.add("a")
# tuples have 2 methods
# - count() = will return teh number of an element in the tuple
# - index() = just like a list, finds the index of hte element passed
# number_of_a = vowels.count("a")
# number_of_e = vowels.count("e")
# print(number_of_a)
# print(number_of_e)
# number_of_o = vowels.count("oo")
# print(number_of_o)
# index_of_a = vowels.index("a")
# print(index_of_a)

#set = like a list, except... it has NO order
# AND it cannot have any duplicates
# it uses {} like dict, but has no keys
some_numbers = { 1, 5, 6, 1, 12, 3}
some_numbers2 = { 9,1, 5, 6, 1, 12, 3}
print(some_numbers)
# print(some_numbers[0]) ERROR... no order
#the add method adds a new member. We dont know where
some_numbers.add(1)
some_numbers.add(4)
print(some_numbers)
# some_numbers.clear() #empty the set
# print(some_numbers)
some_numbers.discard(1)
print(some_numbers)
element_removed = some_numbers.pop() # pop will remove a RANDOM element
print(some_numbers)
print(element_removed)

print(some_numbers)
print(some_numbers.difference_(some_numbers2))
print(some_numbers)
