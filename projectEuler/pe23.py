import time
import math
start_time = time.time() #get our starting time
# Answer: 4179871

# Problem:
# DISTRACTION - perfect numbers 
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be:
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# Half distraction - deficient is irrelevant 
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1+2+3+4+6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# Wow. That was wordy. 
# Job 1: Find all abundant numbers with the sieve from 21 (really, really fast)
# Job 1b: To do that, we find all proper divisors for every number under our limit 
# Job 1c: We don't need to keep all divisors, just add them as we go
# Job 2: Sum every abundant number with every number above it and whatever the sum is, is not in final list
# Job 2b: We can break out of our loop when the sum breaks the limit because we know nothing above that will work
# Job 3: Sum up whatever numbers are left over

limit = 28123
factors = [1] * limit
# we mutliply every possible combo of numbers that
# have a product of less than our limit.
for i in range(2,math.ceil(math.sqrt(limit))):
	for j in range(i,int(limit/i)):
		if(i == j):
			# this is the sq root. only add it one time
			factors[i*j] += i
		else:
			# add both numbers/divisors
			factors[i*j] += i + j

# factors now contains the sum of all proper divisers of every number below our limit

abundant_numbers = []
for i,num in enumerate(factors):
	if(num > i):
		#this is abundant! Add it to our list
		abundant_numbers.append(i)

# we have all the abundant numbers in our list, + the number 0 at the beginning
abundant_numbers.pop(0) #get rid of 0 at the beginning. It was there to make the code simpler
# print(abundant_numbers[0:10])

# assume that all numbers qualify (they dont), remove them when we find a sum
non_abundant_numbers = [num for num in range(limit)]
for i in range(len(abundant_numbers)):
	# outer loop is the lower number
	for j in range(i,len(abundant_numbers)):
		# inner loop is teh upper number
		lower_number = abundant_numbers[i]
		higher_number = abundant_numbers[j]
		sum_of_numbers = lower_number + higher_number
		if(sum_of_numbers < limit):
			# this number does NOT qualify
			# clear out that number from our non_abundant_numbers
			non_abundant_numbers[sum_of_numbers] = 0
		else:
			# we dont need to keep going. We are too high
			break

print(sum(non_abundant_numbers))

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")