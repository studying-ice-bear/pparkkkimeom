from collections import deque
def solution2(maps):
    answer = 0
    n, m = len(maps), len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False for _ in range(m)] for _ in range(n)]

    queue = deque()
    queue.append((n-1, m-1))
    visited[n-1][m-1] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    answer = maps[0][0]
    if maps[0][0] == 1:
        answer = -1

    return answer


def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False for _ in range(m)] for _ in range(n) ]

    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        if x == n-1 and y == m-1:
            answer = maps[x][y]
            return answer

        # visited[x][y] = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if not visited[nx][ny] and maps[nx][ny] != 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1
    # if answer == 0:
    answer = -1
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
