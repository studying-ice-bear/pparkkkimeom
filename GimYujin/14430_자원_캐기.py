N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(1, M):
    graph[0][i] += graph[0][i-1]

for i in range(1, N):
    graph[i][0] += graph[i-1][0]

for i in range(1, N):
    for j in range(1, M):
        graph[i][j] = max(graph[i-1][j], graph[i][j-1]) + graph[i][j]
# print(*graph, sep="\n")
print(graph[N-1][M-1])

'''
max_count = 0


def dfs(x, y, cnt):
    global max_count

    dx = [0, 1]
    dy = [1, 0]

    if x == N-1 and y == M-1:
        if max_count < cnt:
            max_count = cnt
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1:
                dfs(nx, ny, cnt+1)
            else:
                dfs(nx, ny, cnt)


dfs(0, 0, 0)
print(max_count)
'''

'''
3 3
0 0 0
0 1 1
0 0 0
'''