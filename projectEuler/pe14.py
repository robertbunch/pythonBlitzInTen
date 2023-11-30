import time
start_time = time.time() #get our starting time
# The following iterative sequence is defined for the set 
# of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate 
# the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
# 2:1
# 3:7
# 4:2
# 5:5
# 6:8
# 7:13

# It can be seen that this sequence (starting at 
# and finishing at 13 and ending at 1) contains 
# 10 terms. Although it has not been proved yet 
# (Collatz Problem), it is thought that all starting 
# numbers finish at 1.

# Which starting number, under one million, produces 
# the longest chain?

# NOTE: Once the chain starts the terms are allowed to go 
# above one million.    
# answer: 837799

# init our winners
top_num = 0
top_num_chain_count = 0
known_nums = {}
for i in range(2,1000000):
    #i needs to stay in the sequence
    #cur_num starts at i, then we change it
    cur_num = i
    cur_num_chain_count = 0
    while(cur_num > 1):
        if(cur_num in known_nums):
            #we have solved this before! Just add the total
            cur_num_chain_count += known_nums[cur_num]
            cur_num = 1 #end the while
        else:
            if(cur_num % 2 == 0):
                #this number is even!
                cur_num /= 2
            else:
                #odd number
                cur_num = (cur_num * 3) + 1
            cur_num_chain_count += 1
    if(cur_num_chain_count > top_num_chain_count):
        #we have a new winner!
        top_num = i #not the cur_num, because it will be 1
        top_num_chain_count = cur_num_chain_count
    known_nums[i] = cur_num_chain_count
print(top_num)
print(top_num_chain_count)

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")
 
    

