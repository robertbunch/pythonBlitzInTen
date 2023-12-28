import time
start_time = time.time() #get our starting time

# Answer: 1074
# Find the maximum total from top to bottom of the triangle below:

triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

parsed_tri = triangle.strip().split('\n')
# convert each row into a list or integers
for i in range(0,len(parsed_tri)):
    # create our rows
    parsed_tri[i] = parsed_tri[i].strip().split(' ')
    for j in range(0,len(parsed_tri[i])):
        # convert each col into an int (from a str)
        parsed_tri[i][j] = int(parsed_tri[i][j])

# start at the 2nd to last row in parsed_tri list
start_tri_row = len(parsed_tri) - 2

# row loop
for i in range(start_tri_row,-1,-1):
    # loop backwards from 14, until 0 and stop at -1
    # decrament by each time through
    for j in range(0,i+1): #i+1 because the next row has 1 more col than this one
        down_left = parsed_tri[i+1][j]
        down_right = parsed_tri[i+1][j+1]
        if(down_left > down_right):
            parsed_tri[i][j] += down_left
        else:
            parsed_tri[i][j] += down_right

for row in parsed_tri:
    print(row)

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")
