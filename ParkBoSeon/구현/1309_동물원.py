import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n + 1)]

dp[0] = 1
dp[1] = 2

if n == 1:
    print(3)
    exit()

for i in range(2, n + 1):
    dp[i] = 2
    dp[i - 1] = dp[i - 1] * 2