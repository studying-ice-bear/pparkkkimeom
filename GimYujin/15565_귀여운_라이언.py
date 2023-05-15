N, K = map(int, input().split())
arr = list(map(int, input().split()))

dp = []

for i in range(N):
    if arr[i] == 1:
        dp.append(i)

if len(dp) < K:
    answer = -1
else:
    answer = 1000001

    for i in range(len(dp)):
        if i + K > len(dp):
            continue
        answer = min(answer, dp[i+K-1] - dp[i]+1)

print(answer)

'''
5 2
1 1 2 2 1
2
'''
