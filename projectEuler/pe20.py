import math
import time
start_time = time.time() #get our starting time
# Answer: 648

sum_total = 0 #init answer
big_num = str(math.factorial(100)) #this is 100! as a string
print((big_num))
for digit in big_num:
    sum_total += int(digit)
print(sum_total)
end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")

# the one line answer
func_total = sum(map(int,str(math.factorial(100))))
print(func_total)