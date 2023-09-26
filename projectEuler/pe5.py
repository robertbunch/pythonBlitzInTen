# Answer: 232792560
import time
#create a point in time as our start. Then go...
start_time = time.time()


primes = [3,6,7,8,9,11,12,13,14,15,16,17,18,19]
primes.reverse()
def is_divis_by_20(num):
    for i in primes:
        if(num % i != 0):
            return False
    return True


not_found = True
number_to_check = 20
while(not_found):
    if(is_divis_by_20(number_to_check)):
        print(number_to_check)
        not_found = False
    else:
        number_to_check += 20

print(f"--- Number of seconds to solve {time.time() - start_time}")