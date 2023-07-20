# https://www.acmicpc.net/problem/1890
# 52 ms
N = int(input())
boardInfo = []

for _ in range(N):
    row = list(map(int, input().split()))
    boardInfo.append(row)

DP = [[0 for _ in range(N)] for _ in range(N)]
DP[0][0] = 1

for r in range(N):
    for c in range(N):
        cell = boardInfo[r][c]
        if cell == 0:
            break
        if r + cell < N:
            DP[r + cell][c] += DP[r][c]
        if c + cell < N:
            DP[r][c + cell] += DP[r][c]

print(DP[N-1][N-1])
