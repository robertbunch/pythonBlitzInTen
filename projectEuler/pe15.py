import time
start_time = time.time() #get our starting time
# [
    # [1,1,1],
    # [1,2,3],
    # [1,3,6]
# ]
# Answer: 137,846,528,820

def find_routes(grid_size):
    grid = []
    # grid = [[1] * grid_size] * grid_size WONT WORK!!
    for i in range(0,grid_size):
        grid.append([1] * grid_size)
    # grid[2][2] = 5 #test memory
    for i in range(0,grid_size):
        for j in range(0,grid_size):
            if(i == 0 or j == 0):
                #we are in the 1st row or 1st col
                #just put a 1
                grid[i][j] = 1
            else:
                number_above = grid[i-1][j]
                number_left = grid[i][j-1]
                grid[i][j] = number_above + number_left
    for row in grid:
        print(row)
    return grid[grid_size - 1][grid_size - 1]

#21 = 21 points, so a 20 sided grid
grid_size = 21
answer = find_routes(grid_size) #3 = a 2x2 grid!
print(f"Answer for a {grid_size - 1} x {grid_size - 1} is: {answer}")

end_time = time.time() #get our ending time
print(f"--- Number of seconds to solve {time.time() - start_time}")
 