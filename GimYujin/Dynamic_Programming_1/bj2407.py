
N, M = map(int, input().split())

dp = [1]*101

max_n = max(N, M)
for i in range(1, max_n+1):
    dp[i] = i * dp[i-1]

print(dp[N]//(dp[N-M]*dp[M]))
