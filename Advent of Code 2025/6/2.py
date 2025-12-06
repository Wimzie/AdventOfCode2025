import re
inputLines = open("input.txt").read().splitlines()

totalSum = 0

for i in range(len(inputLines[-1])):
    if(re.search("(\+|\*)", inputLines[-1][i])):
        sumToAdd = 0
        numbers = []
        operand = inputLines[-1][i]
         
        k = i + 1
        while not re.search("(\+|\*)", inputLines[-1][k]):
            if k == len(inputLines[-1]) - 1:
                k = len(inputLines[-1]) + 1
                break
            k += 1
    
        endOfBlock = k - 2
        currentColumn = endOfBlock
        while currentColumn >= i:        
            number = ""
            for j in range(len(inputLines)-2, -1, -1):
                if inputLines[j][currentColumn] != " ":
                    number = inputLines[j][currentColumn] + number
            numbers.append(int(number))
            currentColumn -= 1
        
        if(operand == "+"):
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