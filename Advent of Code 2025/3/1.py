inputLines = open("input.txt").read().splitlines()

totalJoltage = 0

for row in inputLines:
    highestNumber = 0
    highestNumberIndex = 0
    for i in range(len(row)):
        if int(row[i]) > highestNumber:
            highestNumber = int(row[i])
            highestNumberIndex = i

    nextHighestNumberRight = 0
    for i in range(highestNumberIndex + 1, len(row)):
        if int(row[i]) > nextHighestNumberRight:
            nextHighestNumberRight = int(row[i])
    nextHighestNumberLeft = 0
    for i in range(highestNumberIndex):
        if int(row[i]) > nextHighestNumberLeft:
            nextHighestNumberLeft = int(row[i])

    if nextHighestNumberRight != 0 and int(str(highestNumber) + str(nextHighestNumberRight)) > int(str(nextHighestNumberLeft) + str(highestNumber)):
        totalJoltage += int(str(highestNumber) + str(nextHighestNumberRight))
        continue

    totalJoltage += int(str(nextHighestNumberLeft) + str(highestNumber))


print(totalJoltage)

