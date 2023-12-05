import time
start_time = time.time() #get our starting time
# Answer: 137846528820
def findRoutes(gridSize):
    routeMatrix = []
    routeMatrix = [[1] * gridSize] * gridSize
    # 20x20 grid of 1s

    for i in range(0,gridSize):
        for j in range(0,gridSize):
            if(i == 0):
                routeMatrix[i][j] = routeMatrix[i][j-1]
            elif(j == 0):
                routeMatrix[i][j] = routeMatrix[i-1][j]        
            else:
                routeMatrix[i][j] = routeMatrix[i][j-1] + routeMatrix[i-1][j]
            print(i,j,routeMatrix[i][j])
        print(routeMatrix)    
        # routeMatrix[i] = 2 * routeMatrix[i-1]
#     }
    print(routeMatrix)
    return routeMatrix
# }


# console.time('grid')
gridSize = 3
n = findRoutes(gridSize);
print(n)
print(n[1][1])
# console.timeEnd('grid')

# end_time = time.time() #get our ending time
# print(f"--- Number of seconds to solve {time.time() - start_time}")
 