inputLines = open("input.txt").read().splitlines()

ranges = []
IDsToCheck = []
freshAvailableIDs = 0
for line in inputLines:
    if line == "":
        continue
    if "-" in line:
        ranges.append(line)
        continue

    IDsToCheck.append(int(line))

for availableID in IDsToCheck:
    for range in ranges:
        lowerBound = int(range.split("-")[0])
        higherBound = int(range.split("-")[1])

        if(availableID >= lowerBound and availableID <= higherBound):
            freshAvailableIDs += 1
            break

print(freshAvailableIDs)