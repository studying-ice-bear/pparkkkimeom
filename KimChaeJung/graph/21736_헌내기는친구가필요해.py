# https://www.acmicpc.net/problem/21736

# 484ms

N, M = map(int, input().split())

campusMapInfo = []
doyeonPoint = ()
friendCount = 0
visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    row = list(input())
    if 'I' in row:
        for j in range(M):
            if row[j] == 'I':
                doyeonPoint = (i, j)
    campusMapInfo.append(row)


def BFS(start, mapInfo):
    global friendCount
    queue = [start]
    visited[start[0]][start[1]] = 1

    while queue:
        curR, curC = queue.pop()

        dr = [0, 0, 1, -1]
        dc = [-1, 1, 0, 0]

        if mapInfo[curR][curC] == 'P':
            friendCount += 1
        for i in range(4):
            newR, newC = curR + dr[i], curC + dc[i]
            if 0 > newR or N <= newR or 0 > newC or M <= newC:
                continue
            if visited[newR][newC] == 1:
                continue
            if mapInfo[newR][newC] == 'X':
                continue
            visited[newR][newC] = 1
            queue.append((newR, newC))


BFS(doyeonPoint, campusMapInfo)
print(friendCount if friendCount != 0 else 'TT')
