import math

an = [1]*10000
for i in range(2,10000):
    for j in range(2,int(math.sqrt(i))):
        if(i % j == 0):
            an[i] += j
            an[i] += int(i/j)

for i,row in enumerate(an):
    print(i,row)

total = 0
for i in range(2,10000):
    num2 = an[i]
    if(an[i] == i and an[an[i]] == i):
        total += an[i] + i
print(total)