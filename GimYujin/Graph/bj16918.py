import sys
from collections import deque

R, C, N = map(int, sys.stdin.readline().split())
board = []
bomb = [[0]*C for _ in range(R)]

for i in range(R):
    board.append(list(x for x in sys.stdin.readline().strip()))
    for j in range(C):
        if board[i][j] == 'O':
            bomb[i][j] = 1
        else:
            bomb[i][j] = 2

result = [['O']*C for _ in range(R)]


def explode(graph, bombType):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[False] * C for _ in range(R)]

    queue = deque()
    for i in range(R):
        for j in range(C):
            if graph[i][j] == bombType:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        result[x][y] = '.'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue

            if not visited[nx][ny]:

                result[nx][ny] = '.'
                visited[nx][ny] = True

                if graph[nx][ny] != bombType:
                    graph[nx][ny] = bombType

    return graph


def show(graph):
    for i in range(R):
        for j in range(C):
            print(graph[i][j], end='')
        print()


if N == 1:      # 초기 폭탄 둔 위치 보여주기
    show(board)
elif N % 2 == 0:
    show(result)
else:
    # 첫 번째 폭탄 터뜨리기
    explode(bomb, 1)

    if N % 4 == 1:
        # 폭탄 채우기
        for i in range(R):
            for j in range(C):
                if result[i][j] == '.':
                    result[i][j] = 'O'
                    bomb[i][j] += 2

        # 두 번째 폭탄 터뜨리기
        explode(bomb, 2)

    show(result)

'''
문제 풀이 아이디어:
반복되는 장면이 나타난다!
    1. 첫 번째 폭탄을 두었을 때
    2. 꽉 찬 보드 - 나머지 칸에 폭탄 두기
    3. 첫 번째 폭탄이 터졌을 때
    4. 꽉 찬 보드 - 나머지 칸에 폭탄 두기
    5. 두 번째 폭탄이 터졌을 때 
    6. 꽉 찬 보드 - 나머지 칸에 폭탄 두기
    7. 4번에서 채운 폭탄 펑!
    ...
        
N == 1: 첫 번째 폭탄을 두었을 때
N % 2 == 0: 꽉 찬 보드!
N이 1이 아니고, N % 4 == 1:  첫 번째 폭탄 터지고 두 번째 폭탄 터뜨릴 때
N이 3이 아니고, N % 4 == 3:  첫 번째 폭탄 터뜨릴 때


3 3 3
OO.
OOO
OOO

3 3 5
OO.
OOO
OOO

<결과>
OOO
OOO
OOO

3 3 6
OO.
OOO
OOO

<결과>
OOO
OOO
OOO

3 3 7
OO.
OOO
OOO

<결과>
...
...
...

'''