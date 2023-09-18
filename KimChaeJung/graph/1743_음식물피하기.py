# https://www.acmicpc.net/problem/1743
# 256 ms
N, M, K = map(int, input().split())
coresco = [[0 for _ in range(M)] for _ in range(N)]
trashList = []
for _ in range(K):
    r, c = map(int, input().split())
    trashList.append([r-1, c-1])
    coresco[r-1][c-1] = 1


def BFS(r, c):
    global visited
    trashSize = 1
    queue = [(r, c)]
    visited[r][c] = True

    while queue:
        curR, curC = queue.pop()
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]

        for i in range(4):
            newR, newC = curR + dr[i], curC + dc[i]
            if newR < 0 or N <= newR or newC < 0 or M <= newC:
                continue
            if visited[newR][newC]:
                continue
            if coresco[newR][newC] == 1:
                trashSize += 1
                visited[newR][newC] = True
                queue.append((newR, newC))

    return trashSize


maxTrashSize = 0
visited = [[False for _ in range(M)] for _ in range(N)]
for trash in trashList:
    r, c = trash
    if not visited[r][c]:
        trashSize = BFS(r, c)
        maxTrashSize = max(maxTrashSize, trashSize)

print(maxTrashSize)
