import time
import math
# The prime factors of 13195 are 5,7,13, and 29.

# What is the largest prime factor of the number 
# 600,851,475,143?
# Answer is 6857

start_time = time.time()
big_num = 600851475143
# 5 seconds
# 50
# 500
# 5000
# 50000 = 13 hours

# big_num = 13195
list_of_prime_factors = []

def am_i_prime(i):
    is_prime = True #assume the number is prime until we find it's not
    #is this number, which is a factor, prime?
    for n in range(2,i):
        #check if i % n is 0. If so... NOT prime
        if(i % n == 0):
            is_prime = False
            break #no reason to keep checking. It's not prime
    return is_prime    


#find all the factors of big_num
top_num = math.floor(math.sqrt(big_num)) + 1
for i in range(2,top_num):
    #is it a factor? Use %
    if(big_num % i == 0):
        #this is a factor! Get it's pair
        j = math.floor(big_num / i)
        # Find out if it is prime
        is_this_factor_prime = am_i_prime(i)
        # print(f"{i} - {is_this_factor_prime}")
        if(is_this_factor_prime):
            list_of_prime_factors.append(i)
        is_this_factor_prime = am_i_prime(j)
        if(is_this_factor_prime):
            list_of_prime_factors.append(j)
        # print(f"{j} - {is_this_factor_prime}")

print(list_of_prime_factors)

end_time = time.time()
print(f"--- number of secodns to solve... {end_time - start_time}" )