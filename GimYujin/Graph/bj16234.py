import math
from collections import deque

N, L, R = map(int, input().split())

land = []
for _ in range(N):
    land.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(s_x, s_y, visited):

    que = deque()
    que.append((s_x, s_y))
    visited[s_x][s_y] = True

    union = deque()
    union.append((s_x, s_y))
    total = land[s_x][s_y]

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if visited[nx][ny]:
                continue

            if L <= abs(land[x][y]-land[nx][ny]) <= R:
                union.append((nx, ny))
                que.append((nx, ny))
                visited[nx][ny] = True
                total += land[nx][ny]

    n = len(union)
    while union:
        xx, yy = union.popleft()
        land[xx][yy] = math.floor(total/n)

    return n


day = 0
while True:
    stop = True
    visit = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                if bfs(i, j, visit) > 1:
                    stop = False

    if stop:
        break

    day += 1

print(day)

'''
문제 링크: https://www.acmicpc.net/problem/16234
문제 풀이 아이디어:
- 연합 국가 처리를 어떻게 할 것인가?
    deque에 좌표값을 넣어주자
- 이동이 일어났는지 안 일어났는지 체크하기
    stop 체크 포인트 추가하기
    
'''