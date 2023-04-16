import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = 0
flag = False
flagSet = []

def bfs(c, v, a, b):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque([[a, b]])
    v[a][b] = True
    
    posQueue = deque([])
    t = 0
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        t += c[x][y]
        posQueue.append([x, y])
        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] != True:
                if l <= abs(c[x][y] - c[nx][ny]) <= r:
                    queue.append([nx, ny])
                    v[nx][ny] = True
    if len(posQueue) == 1:
        return False
    
    temp = t // cnt
    while posQueue:
        x, y = posQueue.popleft()
        c[x][y] = temp
    
    return True


while True:
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                flag = bfs(countries, visited, i, j)
                flagSet.append(flag)
    
    visited = [[False] * n for _ in range(n)]
    
    if True not in flagSet:
        break
    else:
        flagSet = []
        answer += 1

print(answer)