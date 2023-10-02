import time
#answer: 104743

start_time = time.time() #get our starting time

known_primes = [2,3]
i = 4
while(len(known_primes) < 10001):
    is_prime = True
    for a_factor in range(2,i):
        if(i % a_factor == 0):
            is_prime = False
            break
    if(is_prime):
        known_primes.append(i)
    i += 1
print(known_primes[len(known_primes) - 1])
end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")

start_time = time.time() #get our starting time
known_primes = [2,3]
i = 4
while(len(known_primes) < 10001):
    is_prime = True
    for a_prime in known_primes:
        # print(i,a_prime,i % a_prime)
        if(i % a_prime == 0):
            is_prime = False
            break
    if(is_prime):
        known_primes.append(i)
    i += 1

print(known_primes[len(known_primes) - 1])
end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")