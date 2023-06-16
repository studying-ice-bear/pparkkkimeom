# https://www.acmicpc.net/problem/17144

# 3936ms

import copy
R, C, T = map(int, input().split())
roomInfo = []

airCleaner = []

for i in range(R):
    eachRow = list(map(int, input().split()))
    if eachRow[0] == -1:
        airCleaner.append((i, 0))
    roomInfo.append(eachRow)


def spread(room):
    afterSpread = [[0 for _ in range(C)] for _ in range(R)]

    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]

    for r in range(R):
        for c in range(C):
            munji = room[r][c]
            if munji == 0 or munji == -1:
                afterSpread[r][c] += munji
                continue
            hwaksanCount = 0
            hwaksanMunji = munji//5
            for i in range(4):
                newR = r + dr[i]
                newC = c + dc[i]
                if 0 > newR or R <= newR or 0 > newC or C <= newC:
                    continue
                if (newR, newC) in airCleaner:
                    continue
                afterSpread[newR][newC] += hwaksanMunji
                hwaksanCount += 1
            afterSpread[r][c] += munji - hwaksanMunji*hwaksanCount
    return afterSpread


def makeCircuit(start, isUpper):
    x, y = start
    # [secondEnd, fourthStart]
    endInfo = [0,  -1,  1] if isUpper else [R-1, 1,  -1]
    circuitList = []
    for c in range(C-1):
        circuitList.append((x, c))
    for r in range(x, endInfo[0], endInfo[1]):
        circuitList.append((r, C-1))
    for c in range(C-1, 0, -1):
        circuitList.append((endInfo[0], c))
    for r in range(endInfo[0], x, endInfo[2]):
        circuitList.append((r, 0))
    return circuitList


def cleanCircuit(circuit, origin, afterClean):
    for idx in range(len(circuit)-1):
        curPointR, curPointC = circuit[idx]
        nextPointR, nextPointC = circuit[idx+1]
        if idx == 0:
            afterClean[nextPointR][nextPointC] = 0
            continue
        afterClean[nextPointR][nextPointC] = origin[curPointR][curPointC]
    return afterClean


def turnOnAC(room):
    afterClean = copy.deepcopy(room)
    uCStart, lCStart = airCleaner

    upperCircuit = makeCircuit(uCStart, True)
    afterClean = cleanCircuit(upperCircuit, room, afterClean)
    lowerCircuit = makeCircuit(lCStart, False)
    afterClean = cleanCircuit(lowerCircuit, room, afterClean)

    return afterClean


for _ in range(T):
    roomInfo = spread(roomInfo)
    roomInfo = turnOnAC(roomInfo)

answer = 0
for row in roomInfo:
    answer += sum(row)

print(answer+2)
