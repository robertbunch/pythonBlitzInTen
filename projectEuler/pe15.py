import time
x=int(input("Enter X of grid: "))
y=int(input("Enter Y of grid: "))
start = time.time()
route_matrix = list(range(1,x+2))
print(route_matrix)
while route_matrix [1]!=y+1:
    i=0
    print(route_matrix)
    for n in route_matrix [1:]:
        i+=1
        route_matrix [i]=n+route_matrix [i-1]
print(f"There are {route_matrix [-1]} routes in {x}x{y} grid!")
end = time.time() - start
print("Runtime =", end)