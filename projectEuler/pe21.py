import math
import time
start_time = time.time() #get our starting time
# Answer: 31626

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into ).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55,and 110; 
# therefore d(220) = 284. The proper divisors of 284 are 1,2,4,,71, and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

limit = 10000 #limit is how high we are going to look
factors = [1] * limit
# print(factors)
for i in range(2, limit):
    # what are i's divisors
    for j in range(2, int(math.sqrt(i))):
        if(i % j == 0):
            # this is a divisor!
            factors[i] += j #the smaller divisor
            factors[i] += int(i/j) #this will be the bigger divisor

# for i, value in enumerate(factors):
#     print(i,":",value)

# find the pairs!
an_sum = 0
for index1 in range(2,limit):
    value1 = factors[index1]
    # we are lookign for pairs
    # one value will always be higher than the index
    # and the other index will be higher than the value
    if(value1 < index1):
        index2 = value1
        value2 = factors[index2]
        if(value2 == index1):
            # this is a match
            an_sum += index1 + value1
print(an_sum)

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")

#############################
# Sieve solution
start_time = time.time() #get our starting time
factors = [1] * limit
# we mutliply every possible combo of numbers that
# have a product of less than 10000.
for i in range(2,int(math.sqrt(i))):
    for j in range(i,int(limit/i)):
        factors[i*j] += i + j

# find the pairs!
an_sum = 0
for index1 in range(2,limit):
    value1 = factors[index1]
    # we are lookign for pairs
    # one value will always be higher than the index
    # and the other index will be higher than the value
    if(value1 < index1):
        index2 = value1
        value2 = factors[index2]
        if(value2 == index1):
            # this is a match
            an_sum += index1 + value1
print(an_sum)

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")
