import re
import math
inputLines = open("input.txt").read().splitlines()

currentPos = 50
occurancesOfZero = 0
for row in inputLines:
    direction = row[0]
    number = int(row[1:])

    previousCurrentPos = currentPos

    if(direction == "R"):
        for i in range(number):
            currentPos += 1
            if(currentPos == 100):
                currentPos = 0
                occurancesOfZero += 1

    else:
        for i in range(number):
            currentPos -= 1
            if(currentPos == -1):
                currentPos = 99
            if(currentPos == 0):
                occurancesOfZero += 1

    
print(occurancesOfZero)