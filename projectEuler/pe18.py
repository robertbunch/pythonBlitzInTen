
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

path = []
# convert to a list
parsed_tri = triangle.strip().split("\n")
# convert row into a list of numbers
for i in range(0,len(parsed_tri)):
    parsed_tri[i] = parsed_tri[i].strip().split(' ')
    for j in range(0,len(parsed_tri[i])):
        parsed_tri[i][j] = int(parsed_tri[i][j])
        print(parsed_tri[i][j],type(parsed_tri[i][j]))
star_tri_row = len(parsed_tri) - 2
# print("star_tri_row: ",star_tri_row)
for i in range(star_tri_row,-1,-1):
    for j in range(0,i+1):
        print("i: ",i," j: ",j,type(parsed_tri[i][j]))
        if(parsed_tri[i + 1][j] > parsed_tri[i + 1][j + 1]):
            path.append('left')
        else:
            path.append('right')

        parsed_tri[i][j] += max(parsed_tri[i + 1][j], parsed_tri[i + 1][j + 1])
print(parsed_tri[0][0])

for row in parsed_tri:
    print(row)
print(path)
