'''
어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다
안전 거리가 가장 큰 칸을 구해보자.
'''
from collections import deque
N, M = map(int, input().split())
graph = []
shark = deque()
for i in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(M):
        if graph[i][j] == 1:
            shark.append((i, j))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
'''
[-1, -1] [-1, 0] [-1, 1]
[0, -1] [0, 0] [0, 1]
[1, -1] [1, 0] [1, 1]
'''


def bfs(que):
    while que:
        x, y = que.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    que.append((nx, ny))
                elif graph[nx][ny] > graph[nx][ny] + 1:
                    graph[nx][ny] = graph[nx][ny] + 1
                    que.append((nx, ny))


bfs(shark)
answer = 0
for i in range(N):
    for j in range(M):
        if answer < graph[i][j]:
            answer = graph[i][j]

print(answer-1)
