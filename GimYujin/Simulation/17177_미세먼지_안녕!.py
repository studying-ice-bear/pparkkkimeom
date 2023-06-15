R, C, T = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
air_cleaner = []

def dust():
    after = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 0:
                continue

            if graph[i][j] == -1:
                after[i][j] = -1
                air_cleaner.append((i, j))
                continue

            after[i][j] += graph[i][j]
            cnt = 0
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if ni < 0 or ni >= R or nj < 0 or nj >= C or graph[ni][nj] == -1:
                    continue

                after[ni][nj] = after[ni][nj] + graph[i][j] // 5
                cnt += 1

            after[i][j] -= (cnt * (graph[i][j] // 5))

    return after


# new_graph = dust()
# print(*new_graph, sep="\n")

'''
2. 공기청정기가 작동한다.
공기청정기에서는 바람이 나온다.
위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
'''


def clean(graph):

    # 아래쪽 공기 청정
    x, y = air_cleaner.pop()
    # ↑
    for i in range(x, R-1):
        if graph[i][y] == -1:
            continue
        if graph[i+1][y] == -1:
            graph[i][y] = 0
        else:
            graph[i][y] = graph[i+1][y]

    # ←
    for j in range(y, C-1):
        if graph[R-1][j] == -1:
            continue
        if graph[R-1][j+1] == -1:
            graph[R-1][j] = 0
        else:
            graph[R-1][j] = graph[R-1][j+1]

    # ↓
    for i in range(R-1, x, -1):
        if graph[i][C-1] == -1:
            continue
        if graph[i-1][C-1] == -1:
            graph[i][C-1] = 0
        else:
            graph[i][C-1] = graph[i-1][C-1]

    # →
    for j in range(C - 1, y, -1):
        if graph[x][j] == -1:
            continue
        if graph[x][j - 1] == -1:
            graph[x][j] = 0
        else:
            graph[x][j] = graph[x][j - 1]

    # 위쪽 청정기 동작
    x, y = air_cleaner.pop()

    # ↓
    for i in range(x, 0, -1):
        if graph[i][y] == -1:
            continue
        if graph[i - 1][y] == -1:
            graph[i][y] = 0
        else:
            graph[i][y] = graph[i - 1][y]

    # ←
    for j in range(C-1):
        if graph[0][j] == -1:
            continue
        if graph[0][j + 1] == -1:
            graph[0][j] = 0
        else:
            graph[0][j] = graph[0][j + 1]

    # ↑
    for i in range(x+1):
        if graph[i][C-1] == -1:
            continue
        if graph[i + 1][C-1] == -1:
            graph[i][C-1] = 0
        else:
            graph[i][C-1] = graph[i + 1][C-1]

    # →
    for j in range(C-1, 0, -1):
        if graph[x][j] == -1:
            continue
        if graph[x][j - 1] == -1:
            graph[x][j] = 0
        else:
            graph[x][j] = graph[x][j - 1]

    return graph


# print()
# print(*clean(new_graph), sep="\n")

for t in range(T):
    graph = dust()
    graph = clean(graph)

total = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            continue
        total += graph[i][j]

# print(*graph, sep="\n")
print(total)

'''
7 8 1
-1 0 0 0 0 0 0 9
-1 0 0 0 3 0 0 8
0 0 5 0 0 0 22 0
0 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
'''