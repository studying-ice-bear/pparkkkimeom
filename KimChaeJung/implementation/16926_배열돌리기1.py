# https://www.acmicpc.net/problem/16926
N, M, R = map(int, input().split())

arrayInfo = []

for _ in range(N):
    row = list(map(int, input().split()))
    arrayInfo.append(row)

def makeLoopPoints(N, M, startPoint):
    loopPointList = []
    x, y = startPoint
    for i in range(N-1):
        loopPointList.append((i+x, 0+y))
    for j in range(M-1):
        loopPointList.append((N-1+x, j+y))
    for i in range(N-1, 0, -1):
        loopPointList.append((i+x, M-1+y))
    for j in range(M-1, 0, -1):
        loopPointList.append((0+x, j+y))
    return loopPointList

def makeLoopList(N, M):
    loopList = []
    startPoint = (0, 0)
    isNSmaller = True if N<=M else False
    if isNSmaller:
        for i in range(N, 0, -2):
            loopList.append(makeLoopPoints(i, M, startPoint))
            startPoint = (startPoint[0]+1, startPoint[1]+1)
            M -= 2
    else:
        for i in range(M, 0, -2):
            loopList.append(makeLoopPoints(N, i, startPoint))
            startPoint = (startPoint[0]+1, startPoint[1]+1)
            N -= 2
    return loopList


def rotateLoopList(loopList, count):
    result = []
    for loopPoints in loopList:
        for _ in range(count):
            poppedElement = loopPoints.pop()
            loopPoints.insert(0, poppedElement)
        result.append(loopPoints)
    return result

rotatedResult = rotateLoopList(makeLoopList(N, M), R)

def putPointToList(rotatedLoopList, N, M):
    originLoopList = makeLoopList(N, M)

    newPointList = [[(-1, -1) for _ in range(M)] for _ in range(N)]
    for loopPointsIdx in range(len(originLoopList)):
        for originPointIdx in range(len(originLoopList[loopPointsIdx])):
            x, y = originLoopList[loopPointsIdx][originPointIdx]
            newPointList[x][y] = rotatedLoopList[loopPointsIdx][originPointIdx]
    return newPointList

rotatedPointResult = putPointToList(rotatedResult, N, M)

def makeRotatedList(origin, rotatedPointList, N, M):
    newList = [[0 for _ in range(M)] for _ in range(N)]
    for rowIdx in range(len(rotatedPointList)):
        for colIdx in range(len(rotatedPointList[0])):
            x, y = rotatedPointList[rowIdx][colIdx]
            newList[rowIdx][colIdx] = origin[x][y]
    return newList

answer = makeRotatedList(arrayInfo, rotatedPointResult, N, M)

for answerRow in answer:
    print(*answerRow, end='\n')
