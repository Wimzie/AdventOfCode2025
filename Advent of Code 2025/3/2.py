inputLines = open("inputTest.txt").read().splitlines()

totalJoltage = 0

for row in inputLines:
    numberString = ""
    highestNumber = 0
    highestNumberIndex = 0
    for i in range(len(row) - 11):
        if int(row[i]) > highestNumber:
            highestNumber = int(row[i])
            highestNumberIndex = i
    numberString += str(highestNumber)

    
    while(len(numberString) < 12):
        highestNumber = 0
        for i in range(highestNumberIndex + 1, len(row)):
            if 12 - len(numberString) > len(row) - i:
                break
            if int(row[i]) > highestNumber:
                highestNumber = int(row[i])
                highestNumberIndex = i
        if highestNumber != 0:
            numberString += str(highestNumber)
    totalJoltage += int(numberString)


print(totalJoltage)

