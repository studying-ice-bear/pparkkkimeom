# https://www.acmicpc.net/problem/21610
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

mapInfo = [[0 for _ in range(N+1)]]
for _ in range(N):
    eachRow = list(map(int, input().split()))
    mapInfo.append([0] + eachRow)

moveInfo = []
for _ in range(M):
    eachMove = list(map(int, input().split()))
    moveInfo.append(eachMove)

#        ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]


def getMovedGoorm(goorm, way, distance):
    result = []
    for singleGoorm in goorm:
        prevRow, prevCol = singleGoorm
        standardMove = distance % N
        newRow, newCol = prevRow + standardMove * \
            dr[way], prevCol + standardMove*dc[way]
        if newRow <= 0:
            newRow += N
        if newRow > N:
            newRow -= N
        if newCol <= 0:
            newCol += N
        if newCol > N:
            newCol -= N
        result.append((newRow, newCol))
    return result


def makeItRain(goorm):
    global mapInfo
    for singleGoorm in goorm:
        curRow, curCol = singleGoorm
        mapInfo[curRow][curCol] += 1


def waterCopyBug(goorm):
    global mapInfo
    for singleGoorm in goorm:
        curRow, curCol = singleGoorm
        waterCount = 0
        for diagonal in range(2, 9, 2):
            adjacentR, adjacentC = curRow + dr[diagonal], curCol + dc[diagonal]
            if adjacentR <= 0 or adjacentR > N:
                continue
            if adjacentC <= 0 or adjacentC > N:
                continue
            if mapInfo[adjacentR][adjacentC] > 0:
                waterCount += 1
        mapInfo[curRow][curCol] += waterCount


def makeGoorm(vanished):
    global mapInfo
    visited = [[0 for _ in range(N+1)]for _ in range(N+1)]
    for prevCloud in vanished:
        prevR, prevC = prevCloud
        visited[prevR][prevC] = 1
    currentGoormList = []
    for r in range(1, N+1):
        for c in range(1, N+1):
            if visited[r][c] == 1:
                continue
            if mapInfo[r][c] >= 2:
                mapInfo[r][c] -= 2
                currentGoormList.append((r, c))
    return currentGoormList


goormInfo = [(N, 1), (N, 2), (N-1, 1), (N-1, 2)]

for order in moveInfo:
    d, s = order
    movedGoorm = getMovedGoorm(goormInfo, d, s)
    makeItRain(movedGoorm)
    waterCopyBug(movedGoorm)
    goormInfo = makeGoorm(movedGoorm)

water = 0
for row in range(N+1):
    for col in range(N+1):
        water += mapInfo[row][col]
print(water)
