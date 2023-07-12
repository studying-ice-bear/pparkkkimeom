import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

time = sys.maxsize
height = 0

for h in range(257):
    remove = 0
    build = 0
    for i in range(N):
        for j in range(M):
            if h <= board[i][j]:
                remove += board[i][j] - h
            else:
                build += h - board[i][j]

    if B + remove - build >= 0:
        tmp = (2 * remove) + build

        if tmp <= time:
            time = tmp
            height = h

print(time, h)
