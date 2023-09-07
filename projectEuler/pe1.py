# Answer: 233168
import time
#create a point in time as our start. Then go...
start_time = time.time()

# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6,and 9. The sum of these multiples is 23.
## natural numbers = non-negative integers. 1-9, integers

# Find the sum of all the multiples of 3 or 5 below 1000.
sum_total = 0 #init sum of our multiples if 3 or 5
for i in range(1,1000):
    #is i divisible (evenly) by 3 or 5
    if(i % 3 == 0 or i % 5 == 0):
        #it is a match!
        sum_total += i
        # print(f"{i} is divisible by 3 or 5")
print(sum_total)

#ridiculous 1 line answer
x = sum([n for n in range(1,1000) if n % 3 == 0 or n % 5 == 0])
print(x)
print(f"--- Number of seconds to solve {time.time() - start_time}")