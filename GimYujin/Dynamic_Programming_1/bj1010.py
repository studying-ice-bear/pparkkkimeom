T = int(input())

dp = [0] * 31

dp[0] = 1

for i in range(1, 31):
    dp[i] = dp[i-1] * i

for _ in range(T):
    N, M = map(int, input().split())
    print(dp[M]//(dp[M-N]*dp[N]))
