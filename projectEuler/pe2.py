# Answer: 4613732
# Each new term in the Fibonacci sequence is generated 
# by adding the previous two terms. By starting with 
# 1 and 2, the first 10 terms will be:
# 1,2,3,5,8,13,21,34,55,89
# By considering the terms in the Fibonacci sequence 
# whose values do not exceed four million, find the 
# sum of the even-valued terms.

import time
#create a point in time as our start. Then go...
start_time = time.time()

sum_of_evens = 2
fib1 = 1
fib2 = 2
newFib = 0
while(fib1 + fib2 < 4000000):
    #if we are inside this while loop, then the next
	#number in fib is less than 4M
	newFib = fib1+fib2
	fib1 = fib2
	fib2 = newFib
	if(fib2 % 2 == 0):
		#if so, this is even and in the sequence. Add it!
		sum_of_evens += fib2

print(sum_of_evens)
print(f"--- Number of seconds to solve {time.time() - start_time}")