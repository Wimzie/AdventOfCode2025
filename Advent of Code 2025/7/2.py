import functools

inputLines = open("input.txt").read().splitlines()

startPos = ""
splitters = []
#visitedPositions = []
width = len(inputLines[0])
height = len(inputLines)

for i in range(height):
    for j in range(width):
        if inputLines[i][j] == "S":
            startPos = str(i) + "," + str(j)
            continue
        if inputLines[i][j] == "^":
            splitters.append(str(i) + "," + str(j))
            continue

@functools.cache
def trackBeam(startPos):
    yCoord = int(startPos.split(",")[0])
    xCoord = int(startPos.split(",")[1])
    
    if(yCoord == height - 1):
        return 1

    if(str(yCoord + 1) + "," + str(xCoord) in splitters):
        return trackBeam(str(yCoord + 1) + "," + str(xCoord - 1)) + trackBeam(str(yCoord + 1) + "," + str(xCoord + 1))
    
    return trackBeam(str(yCoord + 1) + "," + str(xCoord))

splitCount = trackBeam(startPos)
    
print(splitCount)