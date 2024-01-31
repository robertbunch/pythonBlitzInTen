from radixPE22 import radix_sort

import time
start_time = time.time() #get our starting time
# Answer: 871198282

f = open("names.txt", "r")
names = f.read().split(',')
f.close()

names = [name.strip('"') for name in names]

# sorted_names = sorted(names)
sorted_names = radix_sort(names)

sum = 0
for i,name in enumerate(sorted_names):
    this_name = 0
    for char in name:
        this_name += ord(char) - ord("A") + 1
    sum += this_name * (i+1)

print(sum)

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")

# import time
# start_time = time.time() #get our starting time
# sorted_names = radix_sort(names)
# print(sorted_names[0])
# print(f"--- Number of seconds to solve {time.time() - start_time}")

