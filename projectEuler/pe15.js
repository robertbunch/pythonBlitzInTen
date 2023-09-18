// Node/JavaScript version
// 137846528820
function findRoutes(gridSize){
    // console.log(gridSize)
    let routeMatrix = [];
    for(let i = 1; i <= gridSize; i++){
        routeMatrix.push(1);
    }
    console.log(routeMatrix)

    for(let i = 1; i <= gridSize; i++){
        for(let j = 1; j < gridSize; j++){
            routeMatrix[j] = routeMatrix[j] + routeMatrix[j-1];
        }
        console.log(routeMatrix)
        
        routeMatrix[i] = 2 * routeMatrix[i-1];
    }
    console.log(routeMatrix)
    return routeMatrix[gridSize]
}


console.time('grid')
gridSize = 3;
n = findRoutes(gridSize);
console.log(n)
console.timeEnd('grid')