import time
#answer: 104743

start_time = time.time() #get our starting time

#known_primes is where we keep all our known prime #
#once we hit 10001, we have our answer!
#2 and 3 are always prime in this universe, start there
known_primes = [2,3]
num_to_check = 4 #start at 4 and go until we have 10k primes

while(len(known_primes) < 10001):
    is_prime = True #assume the number is True, until we find it's not
    #loop through all numbers from 2 to num_to_check and % for 0

    #we do NOT need to check for all numbers between 2 and num_to_check
    #we only need to check for prime numbers
    # for i in range(2,num_to_check): #brute force check
    for i in known_primes:
        if(num_to_check % i == 0):
            #this is NOT prime
            is_prime = False #bool set to false
            break #this will STOP the for loop, no reason to keep going
    if(is_prime):
        #this number went all the way through and had no factors.
        known_primes.append(num_to_check)
    num_to_check += 1

print(known_primes[-1])

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")