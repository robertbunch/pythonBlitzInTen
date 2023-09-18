import time
# Answer: 906609
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product 
# of two 3-digit numbers. 

#our goal is to multply every combo of 3 digit numbers
#loop from 100 - 999, and multiply times
#loop from 100 - 999. This means we will have 
# 900*900 = 810,000... but Python will smile
start_time = time.time()
highest_palindrome = 0
highest_palindrome_as_list = []

def am_i_a_palindrome(number_to_check):
    #reverse method is very nice
    #but... reverse is a list method
    #cannot cast number -> list
    #but we cann cast number -> string -> list
    number_as_string = str(number_to_check)
    number_as_list = list(number_as_string)
    #reverse method is a list method that reverses the indicies
    number_as_list.reverse()
    # print(f"{number_as_list} {number_to_check}")
    #cast number_as_list into a string, then a number
    num_reversed = int(''.join(number_as_list))
    # print(f"{number_to_check} - {num_reversed}")
    return number_to_check == num_reversed

for num1 in range(100,1000): #outer loop = num1
    #we dont have to check 100->1000 for the inner loop
    #every time. we just have to check from num1 to 1000
    #because we already checked everything below num1
    #on the way up
    for num2 in range(num1,1000):
        #product = the result of multiplication
        product = num1 * num2
        #now... find is this a pal
        pal_check = am_i_a_palindrome(product)
        if(pal_check):
            highest_palindrome_as_list.append(product)
            if(product > highest_palindrome):
                highest_palindrome = product

# print(highest_palindrome_as_list)
print(highest_palindrome)
end_time = time.time()
print(f"--- number of secodns to solve... {end_time - start_time}" )