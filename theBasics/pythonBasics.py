# # # Comments = are anything that is NOT for python
# # # Comments are for the devoloper/human

# # # variable assignment is var name on left, an =, value on right
# # name = "Rob" # assigning name to Rob
# # # Snake case is used in Python when you have a variable 
# # # name that has more than one word. The words are 
# # # separated by _
# # # camel case (alternative to snake) means starting each
# # # new word with a capital letter, except the first
# # #example: cookieCount
# # cookie_count = 12 # assigning cookie_count to 12
# # print("=========expecting 12=============")
# # print(cookie_count)
# # cookie_count = cookie_count - 2 #2 cookies were taken out
# # print("=========expecting 10=============")
# # print(cookie_count)
# # cookie_count = cookie_count + 10 #bake 10 new cookies
# # print("=========expecting 20=============")
# # print(cookie_count)

# # name = "Rob"
# # print(name)
# # name = 'Rob'
# # print(name)
# # # name = `Rob` Python will not like this!
# # print(name)

# # Data Types
# # - String = "English" that is meant for the user
# # in VS code, strings are orange
# # we make a string with "", '', or """
# really_long_text = """they and was they and was they 
#     and was they and was they and was they and was 
#     they and was they and was they and was they and 
#     was """
# print(really_long_text)
# # - Numbers
# # -- Integers
# an_integer = 1
# # -- Floats
# a_float = 3.14
# # - Booleans
# a_boolean = True # False

# really_long_text_data_type = type(really_long_text)
# print(really_long_text_data_type)
# an_integer_data_type = type(an_integer)
# print(an_integer_data_type)
# a_float_data_type = type(a_float)
# print(a_float_data_type)
# a_boolean_data_type = type(a_boolean)
# print(a_boolean_data_type)

# # - List/Dictionaries/Objects

# cookie_count = 12 + " cookies"
# isDayTime = True #Boolean, True = 1, False = 0 
# nonsense = isDayTime + 3
# print(nonsense)
# isNightTime = False
# nonsense2 = isNightTime + 3
# print(nonsense2)

#input() will PAUSE or BLOCK the program
#until the user enters something
name = input("What is your name? >> ") #input is ALWAYS a string data type
# the + sign is NOT a plus sign. It is called
# concatenate in programming. concatenation is when
# you stick 2 strings together 
print("Welcome, " + name)