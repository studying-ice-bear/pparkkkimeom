import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [[0 for _ in range(N)] for _ in range(N)]

dp[0][0] = 1
for i in range(N):
    for j in range(N):
        moveto = board[i][j]
        if moveto > 0:
            ni = i + moveto
            nj = j + moveto
            if ni < N:
                dp[ni][j] += dp[i][j]
            if nj < N:
                dp[i][nj] += dp[i][j]

print(dp[N-1][N-1])

