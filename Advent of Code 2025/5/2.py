inputLines = open("input.txt").read().splitlines()

ranges = []
IDsToCheck = []
for line in inputLines:
    if line == "":
        continue
    if "-" in line:
        ranges.append(line)
        continue

    IDsToCheck.append(int(line))

rangesLength = len(ranges)
i = 0
while (i < (rangesLength - 1)):
    lowerBound = int(ranges[i].split("-")[0])
    higherBound = int(ranges[i].split("-")[1])

    j = i + 1
    rangesLength = len(ranges)
    valueRemoved = False
    while (j < rangesLength):
        newLowerBound = int(ranges[j].split("-")[0])
        newHigherBound = int(ranges[j].split("-")[1])

        if(lowerBound >= newLowerBound and higherBound <= newHigherBound):
            ranges.remove(ranges[i])
            i = 0
            valueRemoved = True
            break
        if(newLowerBound >= lowerBound and newHigherBound <= higherBound):
            ranges.remove(ranges[j])
            i = 0
            valueRemoved = True
            break

        if(lowerBound >= newLowerBound and lowerBound <= newHigherBound):
            ranges[i] = str(newLowerBound) + "-" + str(higherBound)
            ranges.remove(ranges[j])
            i = 0
            valueRemoved = True
            break

        if(higherBound >= newLowerBound and higherBound <= newHigherBound):
            ranges[i] = str(lowerBound) + "-" + str(newHigherBound)
            ranges.remove(ranges[j])
            i = 0
            valueRemoved = True
            break
        j += 1
    if valueRemoved:
        rangesLength = len(ranges)
        continue
    i += 1

totalAvailableIDs = 0

for range in ranges:
    lowerBound = int(range.split("-")[0])
    higherBound = int(range.split("-")[1])

    totalAvailableIDs += higherBound - lowerBound + 1

print(totalAvailableIDs)