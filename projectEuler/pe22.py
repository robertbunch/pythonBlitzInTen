import time
from radixPE22 import radix_sort
start_time = time.time() #get our starting time
# Answer: 871198282

# opening our file for reading
names_file = open('./names.txt')
# read file into a string and split into a list
names = names_file.read().split(',')
names_file.close() #good practice
# parse our list so the " are gone!
names = [name.strip('"') for name in names]

# for name in names:
#     print(name)

sorted_names = radix_sort(names)
# sorted_names = sorted(names) #sorted is the default python sort

sum = 0 #our answer!
# loop through each name and find the value of the char
for i, name in enumerate(sorted_names):
    this_name_val = 0 #init this name char value
    # loop through the char in this name
    for char in name:
        # A = 1, B = 2, C = 3, ... we use A as our 
        # base, and offset by it, +1
        this_name_val += ord(char) - ord('A') + 1
    sum += this_name_val * (i + 1)
print(sum)


end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")

