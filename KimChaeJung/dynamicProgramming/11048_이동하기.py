# https://www.acmicpc.net/problem/11048
# 1188 ms

import sys
N, M = map(int, input().split())

roomInfo = []
for _ in range(N):
    row = list(map(int, input().split()))
    roomInfo.append(row)

DP = [[0 for _ in range(M)] for _ in range(N)]

for r in range(N):
    for c in range(M):
        left = DP[r][c-1] if c - 1 >= 0 else 0
        upper = DP[r-1][c] if r - 1 >= 0 else 0
        diagonal = DP[r-1][c-1] if c - 1 >= 0 and r - 1 >= 0 else 0
        DP[r][c] = max(left, upper, diagonal) + roomInfo[r][c]

print(DP[N-1][M-1])

# 596 ms
input = sys.stdin.readline

# 620 ms


def solution():
    N, M = map(int, input().split())
    roomInfo = [[0 for _ in range(M+1)]]
    for _ in range(N):
        row = list(map(int, input().split()))
        roomInfo.append([0] + row)

    DP = [[0 for _ in range(M+1)] for _ in range(N + 1)]

    for r in range(1, N + 1):
        for c in range(1, M + 1):
            DP[r][c] = max(DP[r][c-1], DP[r-1][c],
                           DP[r-1][c-1]) + roomInfo[r][c]

    return DP[N][M]


print(solution())
