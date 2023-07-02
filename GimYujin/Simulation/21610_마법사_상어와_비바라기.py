N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

move = []
for _ in range(M):
    move.append(list(map(int, input().split())))

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

cloud = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]


def cloudRain(graph, direction, num_move):
    for k in range(len(graph)):
        c_x, c_y = graph[k][0], graph[k][1]

        c_x = (c_x + dx[direction] * num_move) % N
        c_y = (c_y + dy[direction] * num_move) % N
        c_x = N - c_x if c_x < 0 else c_x
        c_y = N - c_y if c_y < 0 else c_y

        graph[k][0] = c_x
        graph[k][1] = c_y
        board[c_x][c_y] += 1

    return graph


def waterCopyMagic(array):
    diagonal_x = [-1, -1, 1, 1]
    diagonal_y = [-1, 1, -1, 1]

    for i in range(len(array)):
        cx, cy = array[i][0], array[i][1]
        cnt = 0
        for j in range(4):
            nx = cx + diagonal_x[j]
            ny = cy + diagonal_y[j]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0:
                cnt += 1

        board[cx][cy] += cnt


def makeCloud(array):
    visited = [[False for _ in range(N)] for _ in range(N)]
    result = []

    for i in range(len(array)):
        cx, cy = array[i][0], array[i][1]
        visited[cx][cy] = True

    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and not visited[i][j]:
                board[i][j] -= 2
                result.append([i, j])

    return result
def getTotal():
    total = 0
    for i in range(N):
        for j in range(N):
            total += board[i][j]
    return total


for i in range(M):
    # 구름 이동
    d, s = move[i][0], move[i][1]
    cloud = cloudRain(cloud, d, s)
    waterCopyMagic(cloud)
    cloud = makeCloud(cloud)
    # print(i)
    # print(*board, sep="\n")
    # print(len(cloud), cloud)

print(getTotal())

'''
(-1, -1) (-1, 0) (-1, 1)
(0, -1) (0, 0) (0, 1)
(1, -1) (1, 0) (1, 1)
'''