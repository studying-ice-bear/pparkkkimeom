import sys
from collections import deque
input = sys.stdin.readline

def fillBomb(b, bp):
    for i in range(r):
        for j in range(c):
            if b[i][j] == '.':
                b[i][j] = 'O'
            elif b[i][j] == 'O':
                bp.append((i, j))

def explosion(b, bp):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while bp:
        x, y = bp.popleft()
        b[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                b[nx][ny] = '.'
    

r, c, n = map(int, input().split())

board = []
bombPos = deque([])
for i in range(r):
    board.append(list(input().strip()))

    

for i in range(1, n):
    if i % 2 == 1:
        fillBomb(board, bombPos)
    elif i % 2 == 0:
        explosion(board, bombPos)

for i in range(r):
    print(''.join(board[i]))