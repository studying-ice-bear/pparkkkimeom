import sys
input = sys.stdin.readline

A = ' ' + input().strip()
B = ' ' + input().strip()

n = len(A)
m = len(B)
dp = [[0] * (m + 1) for _ in range(n + 1)]

answer = 0

for i in range(1, n):
    for j in range(1, m):
        if A[i] == B[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

for i in range(1, n):
    answer = max(answer, max(dp[i]))

print(answer)