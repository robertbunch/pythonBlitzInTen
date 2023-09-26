import time
# Answer: 232,792,560 (232792560)
# 2520 is the smallest number that can be divided by each
# of the numbers 1 to 10 from to without any remainder.

# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20 ?

start_time = time.time() #get our starting time

def is_divisible_by_1_through_20(num):
    # for i in range(1,21):
    #we are sending numbers by the 20, so we don't have to 
    # check 20. We also don't have to check 1 because all 
    # numbers are divisible by 1
    # for i in range(2,20):
    # if we check in reverse order, we can break out of
    # #function sooner, because less numebrs are divisible
    # by 19 than by 2 
    # for i in range(19,1,-1):
    #we dont need to check for numbers that are multiples
    #of a number in the list
    #2 is a mutliple of 4
    #4 is a multiple of 8 and 8 is of 16
    # factors_list = [11,12,13,14,15,16,17,18,19]
    for i in range(11,20):
        if(num % i != 0):
            #this is NOT a winner. It is missing a number
            return False #end our function
    #if we make it this far, then ALL 20 numbers worked. REturn true
    return True

#bool that will keep our loop going until we find an answer
not_found = True
number_to_check = 20 #this is our number we hope is the answer... if not, inc
while(not_found):
    answer_found = is_divisible_by_1_through_20(number_to_check)
    if(answer_found):
        #we have a winner! Stop the loop, and print
        not_found = False
    else:
        #not the answer... incrament number_to_check
        #bump it up by one.
        number_to_check += 20

print(number_to_check) #this is the answer!
end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")