# https://www.acmicpc.net/problem/16927
N, M, R = map(int, input().split())

originArray = []
for _ in range(N):
    eachRow = list(map(int, input().split()))
    originArray.append(eachRow)


def makeCircuitSet(n, m):
    spList = [(0, 0)]
    startPoint = (0, 0)
    while (startPoint[0] < n//2-1 and startPoint[1] < m//2-1):
        startPoint = (startPoint[0]+1, startPoint[1]+1)
        spList.append(startPoint)

    circuitList = []
    limitR, limitC = (n, m)
    for point in spList:
        pointList = []
        for down in range(point[0], limitR-1):
            pointList.append((down, point[1]))
        for right in range(point[1], limitC-1):
            pointList.append((limitR-1, right))
        for up in range(limitR-1, point[0], -1):
            pointList.append((up, limitC-1))
        for left in range(limitC-1, point[1], -1):
            pointList.append((point[0], left))
        limitR, limitC = (limitR-1, limitC-1)
        circuitList.append(pointList)
    return circuitList


def rotateCircuit(givenList, rotateCount):
    result = []
    for eachCircuit in givenList:
        splitPoint = len(eachCircuit) - rotateCount % len(eachCircuit)
        rotatedCircuit = eachCircuit[splitPoint:]+eachCircuit[:splitPoint]
        result.append(rotatedCircuit)
    return result


def putPointAfterRotate(beforeList, afterList, n, m):
    emptyList = [[None for _ in range(m)] for _ in range(n)]
    for rowIdx in range(len(beforeList)):
        for colIdx in range(len(beforeList[rowIdx])):
            row, col = beforeList[rowIdx][colIdx]
            emptyList[row][col] = afterList[rowIdx][colIdx]
    return emptyList


basicCircuitSet = makeCircuitSet(N, M)
rotatedCircuitList = rotateCircuit(basicCircuitSet, R)
rotatedIndexList = putPointAfterRotate(
    basicCircuitSet, rotatedCircuitList, N, M)
for i in range(N):
    eachRow = []
    for j in range(M):
        row, col = rotatedIndexList[i][j]
        eachRow.append(originArray[row][col])
    print(*eachRow)
