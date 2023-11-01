import time
#answer: 142913828922
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# the goal of the sieve is to mark off the numbers that aren't prime
# because they are factors of a prime. We don't need to store them 
# like we did in problem 7, we just need to know if it's prime or not
# if it is:
    # sum it
    # mark every factor up to our number as false, starting with the square
# if it's not, just move on
# This means that our algorithm isn't looking for primes, it's just
# looking to see if this number has been marked by the time we get to it
# if it hasn't then it's prime, and do a little addition, do our marking

start_time = time.time() #get our starting time

def sieveOfEra(upperLimit):
    # we need to init our list of 2million numbers. We will put True 
    # in each index
    primes = [True] * upperLimit
    # print(len(primes))
    sum = 0 #sum is our running total. start at 0
    counter = 0
    # we will a loop to start at 2, and keep going as long as we are 
    # below the upperlimit
    for i in range(2,upperLimit):
        counter += 1
        # check to see if i is prime
        if(primes[i]):
            # this is prime! Add it
            sum += i
            # go hunting for multiples to mark False
            for j in range(i**2,upperLimit,i):
                counter += 1
                primes[j] = False
    print(sum)
    print(counter)

sieveOfEra(2000000)
end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")

# =================pe7======================
start_time = time.time() #get our starting time

#known_primes is where we keep all our known prime #
#once we hit 10001, we have our answer!
#2 and 3 are always prime in this universe, start there
known_primes = [2,3]
num_to_check = 4 #start at 4 and go until we have 10k primes
sum = 0
counter = 0
while(num_to_check < 2000000):
    is_prime = True #assume the number is True, until we find it's not
    #loop through all numbers from 2 to num_to_check and % for 0

    #we do NOT need to check for all numbers between 2 and num_to_check
    #we only need to check for prime numbers
    # for i in range(2,num_to_check): #brute force check
    for i in known_primes:
        # print(i)
        counter += 1
        if(num_to_check % i == 0):
            #this is NOT prime
            is_prime = False #bool set to false
            break #this will STOP the for loop, no reason to keep going
    if(is_prime):
        #this number went all the way through and had no factors.
        known_primes.append(num_to_check)
        sum += i
    num_to_check += 1

print(sum)
print(counter)

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")