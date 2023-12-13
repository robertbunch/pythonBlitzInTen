import time
start_time = time.time() #get our starting time
# Answer: 1366
# 2^15 is 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
# What is the sum of the digits of the number 2^1000

# this is 2 to the 1000th power... 302 digits
big_num = str(2**1000) #convert the integer into a string
sum = 0
for letter in big_num:
    sum += int(letter)
print(sum)

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")
