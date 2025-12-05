inputLines = open("input.txt").read().splitlines()

coords = []

accessibleRolls = 0
width = len(inputLines[0])
height = len(inputLines)


for i in range(height):
    for j in range(width):
        if(inputLines[i][j] == "@"):
            coords.append(str(i) + "," + str(j))
            
while (True):
    coordsToRemove = []
    for coord in coords:
        rollsAdjacent = 0
        yCoord = int(coord.split(",")[0])
        xCoord = int(coord.split(",")[1])

        #Check up
        if (str(yCoord - 1) + "," + str(xCoord)) in coords:
            rollsAdjacent += 1
        #Check right
        if (str(yCoord) + "," + str(xCoord + 1)) in coords:
            rollsAdjacent += 1
        #Check down
        if (str(yCoord + 1) + "," + str(xCoord)) in coords:
            rollsAdjacent += 1
        #Check left
        if (str(yCoord) + "," + str(xCoord - 1)) in coords:
            rollsAdjacent += 1
        #Check up right
        if (str(yCoord - 1) + "," + str(xCoord + 1)) in coords:
            rollsAdjacent += 1
        #Check down right
        if (str(yCoord + 1) + "," + str(xCoord + 1)) in coords:
            rollsAdjacent += 1
        #Check down left
        if (str(yCoord + 1) + "," + str(xCoord - 1)) in coords:
            rollsAdjacent += 1
        #Check up left
        if (str(yCoord - 1) + "," + str(xCoord - 1)) in coords:
            rollsAdjacent += 1

        if rollsAdjacent < 4:
            accessibleRolls += 1
            coordsToRemove.append(str(yCoord) + "," + str(xCoord))
    
    if not coordsToRemove:
        break
    for coord in coordsToRemove:
        coords.remove(coord)

print(accessibleRolls)