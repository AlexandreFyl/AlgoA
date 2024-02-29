# Imports

import random

# =============================================================================
# ============================ Grid functions =================================
# =============================================================================

# 0 = empty cell
# 1 = obstacle
# 2 = destination

def initialize_grid():
    grid = [[0 for x in range(10)] for y in range(10)]
    return grid

def fill_grid(grid, numberOfObstacles):
    # we place the destination in (9,9)
    grid[9][9] = 2
    # we randomly place the obstacles
    for i in range(numberOfObstacles):
        x = random.randint(0,9)
        y = random.randint(0,9)
        grid[x][y] = 1
    # we randomly place the starting point and we make sure it is not an obstacle
    while grid[x][y] == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    # we return the starting point
    return (x,y)

def show_grid(grid):
    for i in range(10):
        print(grid[i])

# =============================================================================
# ========================= Structures & Function =============================
# =============================================================================
        
class Node:
    def __init__(self, x, y, cost, heuristic, parent):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent

# Euclidean distance heuristic
def calculateEuclideanDistance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# We return an object of the following form : (0,0,0,0) considering left, up, right, bottom. 1 if a neighbour exists, 0 if not (grid edge)
def checkForNeighbours(currentNode: Node):
    # Check for x axis
    if currentNode.x == 0:
        #Check for y axis 
        if currentNode.y == 0:
            # no left neighbour & no up neighbour
            return (0,0,1,1)
        elif currentNode.y == 9:
            # no left neighbour & no bottom neighbour
            return (0,1,1,0)
        # no left neighbour only
        return (0,1,1,1)
    # Check for x axis
    elif currentNode.x == 9:
        #Check for y axis 
        if currentNode.y == 0:
            # no right neighbour & no up neighbour
            return (1,0,0,1)
        elif currentNode.y == 9:
            # no right neighbour & no bottom neighbour
            return (1,1,0,0)
        # No right neighbour only
        return (1,1,0,1)

# =============================================================================
# ============================== Test Grid ====================================
# =============================================================================
        
grid = initialize_grid()
startingPoint = fill_grid(grid, 10)
show_grid(grid)  
print("Starting point: ", startingPoint)      

# Init the open and closed lists
openList = []
closedList = []

# Init the starting node
startNode = Node(startingPoint[0], startingPoint[1], 0, calculateEuclideanDistance(startingPoint[0], startingPoint[1], 9,9), None)

# Add the starting node to the open list
openList.append(startNode)

# show the open list
for i in range(len(openList)):
    print("Node ", i, " : ", openList[i].x, openList[i].y, openList[i].cost, openList[i].heuristic)


while len(openList) != 0:
    # Current node
    currentNode = openList[-1]
    # We check if the destination is reached
    if grid[currentNode.x][currentNode.y] == 2:
        print("Destination reached")
        print("Cost: ", currentNode.cost)
        # TO ADD : PRINT PATH FUNCTION
        break
    # We check every neighbour node of the current one
    toCheck = checkForNeighbours(Node)
    if toCheck[0] == 1:
        # left neighbour
        leftNode = Node(currentNode.x-1, currentNode.y, currentNode.cost + 1, calculateEuclideanDistance(currentNode.x-1, currentNode.y, 9,9), currentNode)
        # check if the node is already in the closed list
        if leftNode in closedList:
            continue
    if toCheck[1] == 1:
        # up neighbour
        upNode = Node(currentNode.x, currentNode.y-1, currentNode.cost + 1, calculateEuclideanDistance(currentNode.x, currentNode.y-1, 9,9), currentNode)
        openList.append(upNode)
    if toCheck[2] == 1:
        # right neighbour
        rightNode = Node(currentNode.x+1, currentNode.y, currentNode.cost + 1, calculateEuclideanDistance(currentNode.x+1, currentNode.y, 9,9), currentNode)
        openList.append(rightNode)
    if toCheck[3] == 1:
        # bottom neighbour
        bottomNode = Node(currentNode.x, currentNode.y+1, currentNode.cost + 1, calculateEuclideanDistance(currentNode.x, currentNode.y+1, 9,9), currentNode)
        openList.append(bottomNode)       
                                                                                                       
    