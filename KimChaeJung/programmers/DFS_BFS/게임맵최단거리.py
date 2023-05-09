# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    row = len(maps)
    col = len(maps[0])

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= row or ny < 0 or ny >= col:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
        return maps[row-1][col-1]

    answer = bfs(0, 0)
    if answer == 1:
        return -1
    return answer
