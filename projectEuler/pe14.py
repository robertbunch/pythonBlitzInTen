import time
start_time = time.time() #get our starting time
# The following iterative sequence is defined for the set 
# of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate 
# the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
# answer: 837799

# It can be seen that this sequence (starting at 
# and finishing at 13 and ending at 1) contains 
# 10 terms. Although it has not been proved yet 
# (Collatz Problem), it is thought that all starting 
# numbers finish at 1.

# Which starting number, under one million, produces 
# the longest chain?

# NOTE: Once the chain starts the terms are allowed to go 
# above one million.

top_num = 0
top_num_chain_length = 0
calc_numbers = {}
for i in range(3,1000000,2):
    cur_num = i
    odd = True #keep bool so we dont have to % 2
    cur_num_chain_length = 0
    print(f"i: {i}")
    while(cur_num > 1):
        # print(cur_num)
        if(cur_num in calc_numbers):
            cur_num_chain_length += calc_numbers[cur_num]
            cur_num = 0
        else:
            cur_num_chain_length += 1
            if(cur_num % 2 == 0):
                cur_num = int(cur_num / 2) #divide by 2
            else: 
                cur_num = 3 * cur_num + 1
    if(cur_num_chain_length > top_num_chain_length):
        top_num_chain_length = cur_num_chain_length
        top_num = i
    calc_numbers[i] = top_num_chain_length
print(top_num)
print(top_num_chain_length)
        
end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")
 
    

