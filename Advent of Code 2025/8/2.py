import math, re
inputLines = open("input.txt").read().splitlines()

pairsToCheck = 10000

def calculateDistance(point1, point2):
    p1Coords = point1.split(",")
    p2Coords = point2.split(",")

    return math.sqrt(math.pow(int(p1Coords[0]) - int(p2Coords[0]), 2) + math.pow(int(p1Coords[1]) - int(p2Coords[1]), 2) + math.pow(int(p1Coords[2]) - int(p2Coords[2]), 2))

def insertIntoList(distanceList, distanceIndexList, distance, firstIndex, secondIndex):
    if not distanceList:
        distanceList.append(distance)
        distanceIndexList.append(str(i) + "," + str(j))
        return distanceList, distanceIndexList
    if len(distanceList) < pairsToCheck:
        if len(distanceList) == 1:
            if distance < distanceList[-1]:
                distanceList.insert(0, distance)
                distanceIndexList.insert(0, str(firstIndex) + "," + str(secondIndex))
            else:
                distanceList.append(distance)
                distanceIndexList.append(str(firstIndex) + "," + str(secondIndex))
            return distanceList, distanceIndexList
        for k in range(len(distanceList)):
            if distance < distanceList[k]:
                distanceList.insert(k, distance)
                distanceIndexList.insert(k, str(firstIndex) + "," + str(secondIndex))
                return distanceList, distanceIndexList
        distanceList.append(distance)
        distanceIndexList.append(str(firstIndex) + "," + str(secondIndex))
        return distanceList, distanceIndexList
    
    if distance > distanceList[-1]:
        return distanceList, distanceIndexList
    for k in range(len(distanceList)):
        if distance < distanceList[k]:
            distanceList.insert(k, distance)
            distanceIndexList.insert(k, str(firstIndex) + "," + str(secondIndex))
            distanceList.pop(-1)
            distanceIndexList.pop(-1)
            return distanceList, distanceIndexList

distances = []
distanceIndexes = []

lowestDistance = ""
firstLowestDistanceIndex = ""
secondLowestDistanceIndex = ""

for i in range(len(inputLines) - 1):
    for j in range(i + 1, len(inputLines)):
        distance = calculateDistance(inputLines[i], inputLines[j])
        distances, distanceIndexes = insertIntoList(distances, distanceIndexes, distance, i, j)

connections = []
lastPair = ""
for distanceIndex in distanceIndexes:
    if lastPair:
        break
    if len(connections) == 2:
        print("break")
    if not connections:
        connections.append(distanceIndex + ",")
        continue
    existingConnectionFound = False
    for i in range(len(connections)):
        if re.search("(^|,)" + distanceIndex.split(",")[0] + ",", connections[i]) and re.search("(^|,)" + distanceIndex.split(",")[1] + ",", connections[i]):
            existingConnectionFound = True
            break
        if re.search("(^|,)" + distanceIndex.split(",")[0] + ",", connections[i]):
            existingConnectionFound = True
            linkedChains = False
            for j in range(i + 1, len(connections)):
                if re.search("(^|,)" + distanceIndex.split(",")[1] + ",", connections[j]):
                    connections[i] += connections[j]
                    connections.remove(connections[j])
                    linkedChains = True
                    break
            if linkedChains:
                if len(connections) == 1:
                    if len(connections[0][:-1].split(",")) == len(inputLines):
                        lastPair = inputLines[int(distanceIndex.split(",")[0])] + ";" + inputLines[int(distanceIndex.split(",")[1])]    
                break
            connections[i] += distanceIndex.split(",")[1] + ","
            if len(connections[0][:-1].split(",")) == len(inputLines):
                lastPair = inputLines[int(distanceIndex.split(",")[0])] + ";" + inputLines[int(distanceIndex.split(",")[1])]    
            break
        if re.search("(^|,)" + distanceIndex.split(",")[1] + ",", connections[i]):
            existingConnectionFound = True
            linkedChains = False
            for j in range(i + 1, len(connections)):
                if re.search("(^|,)" + distanceIndex.split(",")[0] + ",", connections[j]):
                    connections[i] += connections[j]
                    connections.remove(connections[j])
                    linkedChains = True
                    break
            if linkedChains:
                if len(connections) == 1:
                    if len(connections[0][:-1].split(",")) == len(inputLines):
                        lastPair = inputLines[int(distanceIndex.split(",")[0])] + ";" + inputLines[int(distanceIndex.split(",")[1])]    
                break
            connections[i] += distanceIndex.split(",")[0] + ","
            if len(connections[0][:-1].split(",")) == len(inputLines):
                lastPair = inputLines[int(distanceIndex.split(",")[0])] + ";" + inputLines[int(distanceIndex.split(",")[1])]    
            break
    if not existingConnectionFound:
        connections.append(distanceIndex + ",")
    
totalSum = int(lastPair.split(";")[0].split(",")[0]) * int(lastPair.split(";")[1].split(",")[0])
print(totalSum)


