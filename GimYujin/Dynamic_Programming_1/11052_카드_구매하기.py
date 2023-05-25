N = int(input())
P = [0]+list(map(int, input().split()))
'''

# 두 번째 풀이
dp = [0] * (N+1)

for i in range(1, N+1):
    print(i, dp)
    for j in range(1, i+1):
        print(j, dp)
        dp[i] = max(dp[i], dp[i-j] + P[j])

print(dp[N])
'''
# 첫 번째 풀이

dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        # i번째까지 팩이 있을 때 j개의 카드로 만들 수 있는 금액의 최대값
        if i > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i][j-i]+P[i], dp[i-1][j])

print(dp[N][N])
print(*dp, sep="\n")

'''
두 번째 풀이 참고: https://developer-mac.tistory.com/69
'''

'''
4
1 5 6 7
10
[0, 0, 0, 0, 0]
[0, 1, 2, 3, 4]
[0, 1, 5, 6, 10]
[0, 1, 5, 6, 10]
[0, 1, 5, 6, 10]
'''
