# When you run return, the function terminates instantly

#palidrome = is a word that is spelled the same forward and backward
#tacocat

#is_palidrome's job is to find out if the word we send as an arg
#is in fact a palidrome or not. It will return True or False
def is_palidrome(word_to_check):
    # modified_word = f"I am checking if {word_to_check} is a palidrome."
    #we can covert a string to a list! This will put a letter in each
    #index
    word_as_list = list(word_to_check)   
    # print(word_as_list) 
    #reverse is a method that all lists have that will switch all the indicies in reverse order
    word_as_list.reverse()
    # print(word_as_list)
    #we can turn a list back into a string by using the join method
    reversed_word_as_string = ''.join(word_as_list)
    if(reversed_word_as_string == word_to_check):
        #if the word reversed as a string = what we were sent, it is a palidrome, return True!
        return True
    else:
        #this is not a palidrome
        return False

list_of_strings = [
    "tacocat",
    "jump",
    "testset",
    "William",
]

for word in list_of_strings:
    is_word_a_palidrome = is_palidrome(word)
    print(f"Is {word} a Palidrome? Answer:{is_word_a_palidrome}")