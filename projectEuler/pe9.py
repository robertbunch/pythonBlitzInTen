import time
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    # a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 5^2 = 25.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product of a*b*c.
# Answer: 31875000

start_time = time.time() #get our starting time
def find_triplet():
    count = 0
    #try all numbers between 1 and 1000 for a and b
    for a in range(1,1000):
        for b in range(1,1000):
            count += 1
            c = 1000 - a - b #solve for c
            if(a*a + b*b == c*c):
                print(f"Counter ran: {count}")
                print(a,b,c)
                return(a*b*c)
answer = find_triplet()
print(answer)
end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")


# ==============opt1================
start_time = time.time() #get our starting time
def find_triplet():
    count = 0
    #try all numbers between 1 and 1000 for a and b
    for a in range(1,333): #a cannot be bigger than 332 or there won't be room in 1000 for b and c
        for b in range(a+1,1000): #b must be larger than a
            count += 1
            c = 1000 - a - b #solve for c
            if(a*a + b*b == c*c):
                print(f"Counter ran: {count}")
                print(a,b,c)
                return(a*b*c)
answer = find_triplet()
print(answer)
end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")


# ==============opt2================
start_time = time.time() #get our starting time
def find_triplet():
    count = 0
    #try all numbers between 1 and 1000 for a and b
    for a in range(1,333): #a cannot be bigger than 332 or there won't be room in 1000 for b and c
        for b in range(a+1,500): #b must be larger than a, b must also be less than c, with a max of 500 or there won't be room for c
            count += 1
            c = 1000 - a - b #solve for c
            if(a*a + b*b == c*c):
                print(f"Counter ran: {count}")
                print(a,b,c)
                return(a*b*c)
answer = find_triplet()
print(answer)
end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")
