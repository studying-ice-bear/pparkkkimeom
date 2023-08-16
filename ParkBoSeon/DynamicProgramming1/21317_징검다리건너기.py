import sys
input = sys.stdin.readline

n = int(input())

dp = [1e9 for _ in range(n)]
jumps = []
dp[0] = 0

for i in range(n - 1):
    a, b = map(int, input().split())
    jumps.append((a, b))
    
    if i + 1 < n:
        dp[i + 1] = min(dp[i + 1], dp[i] + a)

    if i + 2 < n:
        dp[i + 2] = min(dp[i + 2], dp[i] + b)
        

k = int(input())

answer = dp[-1]

for i in range(3, n):
    a, b, c = dp[i - 3] + k, 1e9, 1e9
    
    for j in range(i, n - 1):
        if i + 1 <= n:
            b = min(b, a + jumps[j][0])
        if i + 2 <= n:
            c = min(c, a + jumps[j][1])
        a, b, c = b, c, 1e9
    answer = min(answer, a)

print(answer)        
