# https://www.acmicpc.net/problem/5212

# 틀렸습니다

'''
R, C = map(int, input().split())

islandInfo = []

for _ in range(R):
    mapRow = list(input())
    islandInfo.append(mapRow)

after50IslandInfo = [['' for _ in range(C)] for _ in range(R)]

for row in range(R):
    for col in range(C):
        if islandInfo[row][col] == 'X':
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            seaCount = 0
            for i in range(4):
                newR, newC = row + dx[i], col + dy[i]
                if 0 > newR or newR >= R or 0 > newC or newC >= C:
                    seaCount += 1
                    continue
                if islandInfo[newR][newC] == '.':
                    seaCount += 1
            if seaCount >= 3:
                after50IslandInfo[row][col] = '.'
                continue
        after50IslandInfo[row][col] = islandInfo[row][col]

deletedInfo = [[], []]

for row in range(R):
    if after50IslandInfo[row] == ['.']*C:
        deletedInfo[0].append(row)
        continue

for col in range(C):
    isAllOcean = True
    for row in range(R):
        if after50IslandInfo[row][col] != '.':
            isAllOcean = False
            break
    if isAllOcean:
        deletedInfo[1].append(col)
    else:
        break

for col in range(C-1, 0, -1):
    isAllOcean = True
    for row in range(R):
        if after50IslandInfo[row][col] != '.':
            isAllOcean = False
            break
    if isAllOcean:
        deletedInfo[1].append(col)
    else:
        break

for row in range(R):
    completedRow = []
    if row not in deletedInfo[0]:
        for col in range(C):
            if col not in deletedInfo[1]:
                completedRow.append(after50IslandInfo[row][col])
    else:
        continue
    print(*completedRow, sep='')
'''

# 44ms

R, C = map(int, input().split())
originMap = []

for _ in range(R):
    row = list(input())
    originMap.append(row)

newMap = []
for row in range(R):
    changedRow = []
    for col in range(C):
        if originMap[row][col] == 'X':
            dr = [1, -1, 0, 0]
            dc = [0, 0, 1, -1]
            seaCount = 0
            for i in range(4):
                newR = row + dr[i]
                newC = col + dc[i]
                if 0 > newR or R <= newR or 0 > newC or C <= newC:
                    seaCount += 1
                    continue
                if originMap[newR][newC] == '.':
                    seaCount += 1
            if seaCount >= 3:
                changedRow.append('.')
                continue
        changedRow.append(originMap[row][col])
    newMap.append(changedRow)

start = [R-1, C-1]
end = [0, 0]
for row in range(R):
    for col in range(C):
        if newMap[row][col] == 'X':
            start[0] = min(start[0], row)
            start[1] = min(start[1], col)
            end[0] = max(end[0], row)
            end[1] = max(end[1], col)

for row in range(start[0], end[0]+1):
    newRow = []
    for col in range(start[1], end[1]+1):
        newRow.append(newMap[row][col])
    print(*newRow, sep='')
