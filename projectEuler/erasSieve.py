
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

print(known_primes)