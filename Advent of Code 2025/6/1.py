import re
inputLines = open("input.txt").read().splitlines()

inputLinesSplit = []
for row in inputLines:
    inputLinesSplit.append(row.split())
    

amountOfColumns = len(inputLines[0].split())
totalSum = 0

for i in range(amountOfColumns):
    j = 0
    sumToAdd = 0
    numbers = []
    while not re.search("(\+|\*)", inputLinesSplit[j][i]):
        numbers.append(int(inputLinesSplit[j][i]))
        j += 1
    if(inputLinesSplit[j][i] == "+"):
        for number in numbers:
            sumToAdd += number
    else:
        for number in numbers:
            if sumToAdd == 0:
                sumToAdd = number
                continue
            sumToAdd *= number
    totalSum += sumToAdd
    
        
print(totalSum)