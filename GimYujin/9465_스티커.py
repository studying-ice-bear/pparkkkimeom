import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    n = int(input())
    S = []
    for _ in range(2):
        S.append([0]+list(map(int, input().split())))

    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    dp[0][1] = S[0][1]
    dp[1][1] = S[1][1]

    if n > 1:

        for i in range(2, n+1):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + S[0][i])
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] + S[1][i])

    # print(*dp, sep="\n")
    print(max(dp[0][n], dp[1][n]))



'''
    dp[0][2] = max(dp[1][1], dp[2][1] + S[1][2])
    dp[1][2] = max(dp[2][1], dp[1][1] + S[2][2])

    dp[0][3] = max(dp[1][2], dp[2][2] + S[1][3])
    dp[1][3] = max(dp[2][2], dp[1][2] + S[2][3])
'''

'''
dp[1] = max(S[0][1], S[1][1])
dp[2] = max(S[0][1] + S[1][2], S[1][1]+S[0][2])
dp[3] = max(S[0][1] + S[1][3],
            S[1][1] + S[0][3],
            S[0][1] + S[1][2] + S[0][3],
            S[1][1] + S[0][2] + S[1][3])
print(dp)
'''



'''
50 80 10
10 50 100

'''