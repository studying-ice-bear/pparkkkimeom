from collections import deque

N, M = map(int, input().split())
board = []
j_x, j_y = 0, 0

fire_que = deque()

for i in range(N):
    tmp = list(i for i in input())
    board.append(tmp)

    for j in range(M):
        if board[i][j] == 'J':
            j_x, j_y = i, j
        elif board[i][j] == 'F':
            fire_que.append((i, j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

j_time = [[0] * M for _ in range(N)]
f_time = [[0] * M for _ in range(N)]


def move():
    while fire_que:
        x, y = fire_que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not f_time[nx][ny] and board[nx][ny] != '#' and board[nx][ny] != 'J':
                    f_time[nx][ny] = f_time[x][y] + 1
                    fire_que.append((nx, ny))

    jihun = deque()
    jihun.append((j_x, j_y))

    while jihun:
        x, y = jihun.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                return j_time[x][y]+1

            if board[nx][ny] == '#' or board[nx][ny] == 'F':
                continue

            if not j_time[nx][ny]:
                if not f_time[nx][ny] or f_time[nx][ny] > j_time[x][y]+1:
                    j_time[nx][ny] = j_time[x][y]+1
                    jihun.append((nx, ny))

    return "IMPOSSIBLE"


answer = move()
print(answer)
'''
def bfs(q, visited, graph):
    j_time = [[0]*M for _ in range(N)]
    f_time = [[0]*M for _ in range(N)]

    while q:
        x, y, kind = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                if kind == 'J':
                    return j_time[x][y] + 1

                continue

            if graph[nx][ny] == '#':
                continue

            if not visited[nx][ny]:
                if graph[nx][ny] == '.' and kind == 'J':
                    j_time[nx][ny] = j_time[x][y] + 1
                    graph[nx][ny] = 'J'

                    q.append((nx, ny, 'J'))
                    visited[nx][ny] = True
                elif graph[nx][ny] == '.' and kind == 'F':
                    f_time[nx][ny] = f_time[x][y] + 1
                    graph[nx][ny] = 'F'

                    q.append((nx, ny, 'F'))
                    visited[nx][ny] = True
            else:
                if graph[nx][ny] == 'J' and kind == 'F':
                    f_time[nx][ny] = f_time[x][y]+1
                    if f_time[nx][ny] <= j_time[nx][ny]:
                        return 'IMPOSSIBLE'

    return 'IMPOSSIBLE'


visit = [[False]*M for _ in range(N)]
# print(bfs(que, visit, board))
'''

'''
.: 지나갈 수 있는 공간
#: 벽
F: 불이 난 공간
J: 지훈이 초기 위치

4 4
J###
#.F#
..##
#.F#
1

4 4
####
#JF#
.###
#.F#
IMPOSSIBLE

4 4
#####
#.JF#
..###
#.F##
IMPOSSIBLE

3 3
FFF
.J.
...
2
'''
