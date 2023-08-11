from collections import deque
N, M, K = map(int, input().split())
graph = [[0 for _ in range(M)]for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

length = 0
visited = [[False for _ in range(M)] for _ in range(N)]

def bfs(s_x, s_y):
    global length
    que = deque()
    que.append((s_x, s_y))
    count = 0
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1

    length = max(count, length)


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs(i, j)

print(length)
