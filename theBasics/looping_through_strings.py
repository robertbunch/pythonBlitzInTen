

a_string_to_loop_through = "I love Python"
a_string_as_list = list(a_string_to_loop_through)

# for letter in a_string_to_loop_through:
#     print(letter)

# for letter in a_string_as_list:
#     print(letter)

# print(a_string_to_loop_through[2]) #l
# print(a_string_as_list[2]) #l

# parsing strings is COMMON in programming
#parsing = looking at the string for whatever reason
# is this a valid phone number
# what credit card company is this card?
# is there a space or a ,

# counter = 0
# for letter in a_string_as_list:
#     if(letter == "l"):
#         #this is an l. 
#         print(f"The position of the l is {counter}.")
#         print(a_string_to_loop_through[counter])
#     counter += 1

# len(string) takes an iterable and tells you how long it is

# number_of_letters = len(a_string_to_loop_through)
# number_of_indicies = len(a_string_as_list)
# print(number_of_letters)
# print(number_of_indicies)

# for i in range(0,number_of_letters):
#     print(a_string_to_loop_through[i])
#     if(a_string_to_loop_through[i] == "l"):
#         #this is an l
#         print(f"The position of the l is {i}.")

#lists have an index method
#strings have a find method
#index/find will look through the list/string for
#the FIRST occurance of the var passed and return the index

index_in_string = a_string_to_loop_through.find("l")
print(index_in_string)
index_in_list = a_string_as_list.index("l")
print(index_in_list)

# for letter in a_string_as_list:
for letter in a_string_to_loop_through:
    if(letter == "l"):
        position_of_l = a_string_to_loop_through.find("l")
        print(f"The position of the l is {position_of_l}")
        print(a_string_to_loop_through[position_of_l])
        print(a_string_as_list[position_of_l])

a_new_string = "Hello"
missing_letter = a_new_string.find("z")
print(missing_letter)
a_new_list = list(a_new_string)
missing_letter = a_new_list.index("z")
print(missing_letter)

