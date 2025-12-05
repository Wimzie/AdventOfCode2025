inputLines = open("input.txt").read()

totalSum = 0
ranges = inputLines.split(",")
for currentRange in ranges:
    firstIndex = int(currentRange.split("-")[0])
    lastIndex = int(currentRange.split("-")[1])

    for i in range(firstIndex, lastIndex + 1):
        lengthofi = len(str(i))
        if ((lengthofi % 2) != 0):
            continue
        
        if(str(i)[:int(lengthofi/2)] == str(i)[int(lengthofi/2):]):
            totalSum += int(str(i)[:lengthofi])

print(totalSum)