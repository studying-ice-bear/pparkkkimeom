# https://www.acmicpc.net/problem/21772
# 988 ms
# [ ] 시간 줄이기
R, C, T = map(int, input().split())
mapInfo = []

gogumaCount = 0
maxGogumaCount = 0

gahee = [-1, -1]

for r in range(R):
    row = input()

    listRow = list(row)

    if gahee == [-1, -1]:
        Gidx = row.find('G')
        if Gidx != -1:
            gahee = [r, Gidx]
            listRow = list(row.replace('G', '.'))

    mapInfo.append(listRow)

dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]

visitedInfo = [(gahee[0], gahee[1])]


def backtracking(r, c):
    global dr, dc, gogumaCount, maxGogumaCount, visitedInfo

    if mapInfo[r][c] == 'S':
        if (r, c) not in visitedInfo[:-1]:
            gogumaCount += 1

    if len(visitedInfo) == T+1:
        maxGogumaCount = max(maxGogumaCount, gogumaCount)
        return

    for i in range(4):
        nextR, nextC = r + dr[i], c + dc[i]

        if nextR < 0 or R <= nextR or nextC < 0 or C <= nextC:
            continue

        if mapInfo[nextR][nextC] == '#':
            continue

        visitedInfo.append((nextR, nextC))
        backtracking(nextR, nextC)
        visitedInfo.pop()

        if mapInfo[nextR][nextC] == 'S':
            if (nextR, nextC) not in visitedInfo[:-1]:
                gogumaCount -= 1


def shortBacktracking():
    return


backtracking(gahee[0], gahee[1])
print(maxGogumaCount)
