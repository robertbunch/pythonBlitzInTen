import time
start_time = time.time() #get our starting time

num = longest = 1
# 1/n is going to produce 1 of 3 decimals
    # if it is divisible by only primes 2 and 5, it terminates 
    # if it is divisible by primes that aren't 2 or 5, it is
        # repeats 
    # if it is divisible by primes 2 and 5 and something else, it 
        # will have the same cycle as another number from #2
# this means we don't need to check any numbers that are divisible
    # by 2 or 5! Eliniating half, and then another 10%
# Can simulate hand division
def long_division(denom):
    keep_looping = True
    dec_digits = []
    remainders = []
    cur_num = 10 #always at least 10
    # make sure that our cur_num is big enough for our first operation
    while cur_num < denom:
        cur_num *= 10
        dec_digits.append(0)
    while (keep_looping):
        # store the digit without decimal, and the remainder
        digit = cur_num // denom
        cur_num = cur_num % denom
        if cur_num == 0: #terminated. End function
            # print(denominator,"Terminates")
            return 0 #we will optimize in a bit
        if(cur_num in remainders):
            return len(remainders)
        else:
            # add the digit and remainder to the list
            dec_digits.append(digit)
            remainders.append(cur_num)
            # bump up the new number by adding a 0
            cur_num *= 10
    
largest_denom = 0
largest_sequence = 0
for denominator in range(3, 1000,2):
    recurr_cycle = long_division(denominator)
    # print(denominator,cycle_lengths,largest_sequence)
    if(recurr_cycle > largest_sequence):
        largest_sequence = recurr_cycle
        largest_denom = denominator
print(largest_denom,largest_sequence)

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")
