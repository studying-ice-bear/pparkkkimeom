from collections import deque
N, M = map(int, input().split())
campus = []
visited = [[False for _ in range(M)] for _ in range(N)]

queue = deque()

for i in range(N):
    tmp = []
    pp = input().strip()
    for j in range(M):
        p = pp[j]
        if p == 'I':
            tmp.append(0)
            queue.append((i, j))
            visited[i][j] = True
        elif p == 'X':
            tmp.append(-1)
            visited[i][j] = True
        elif p == 'P':
            tmp.append(1)
        else:
            tmp.append(0)

    campus.append(tmp)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 0

while queue:
    x, y = queue.popleft()

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if xx < 0 or xx >= N or yy < 0 or yy >= M:
            continue

        if visited[xx][yy]:
            continue

        visited[xx][yy] = True
        queue.append((xx, yy))

        if campus[xx][yy] == 1:
            cnt += 1

if cnt == 0:
    print('TT')
else:
    print(cnt)
