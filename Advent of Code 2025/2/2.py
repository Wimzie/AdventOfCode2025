import re
import math
inputLines = open("input.txt").read()

totalSum = 0
ranges = inputLines.split(",")
for currentRange in ranges:
    firstIndex = int(currentRange.split("-")[0])
    lastIndex = int(currentRange.split("-")[1])

    for i in range(firstIndex, lastIndex + 1):
        lengthofi = len(str(i))
        if(lengthofi == 1):
            continue

        for j in range(math.ceil(lengthofi /2)):
        #for j in range(lengthofi):
            currentCheck = str(i)[:j + 1]
            if(lengthofi % len(currentCheck) != 0):
                continue
            test = "(" + currentCheck + "){" + str(int(lengthofi / (j + 1))) + "}"
            match = re.search("(" + currentCheck + "){" + str(int(lengthofi / (j + 1))) + "}", str(i))

            if(match):
                totalSum += i
                break
            secondMatch = re.findall("(" + currentCheck + ")", str(i))
            if(len(secondMatch) == 1):
                break


print(totalSum)