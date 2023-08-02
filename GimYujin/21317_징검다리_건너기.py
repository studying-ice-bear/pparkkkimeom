'''
참고: https://ddiyeon.tistory.com/55
이분 코드가 제일 이해가 된다!
'''

N = int(input())
jump = []
dp = [1e9] * N
dp[0] = 0
for i in range(N-1):
    jump.append(list(map(int, input().split())))
    if i+1 < N:
        dp[i+1] = min(dp[i+1], dp[i] + jump[i][0])
    if i+2 < N:
        dp[i+2] = min(dp[i+2], dp[i] + jump[i][1])

# 모든 경우에서 큰 점프를 사용한 경우 확인해보기
K = int(input())
print(dp)
answer = dp[-1]
for i in range(3, N):
    end = dp[i-3]+K     # 큰 점프를 시도할 위치
    dp1, dp2 = 1e9, 1e9
    for j in range(i, N-1):
        if i+1 <= N:
            dp1 = min(dp1, end + jump[j][0])
        if i+2 <= N:
            dp2 = min(dp2, end + jump[j][1])
        end, dp1, dp2 = dp1, dp2, 1e9
    answer = min(answer, end)

print(answer)

# import sys
#
# N = int(input())
# jump = [[0, 0]]
# for _ in range(N-1):
#     jump.append(list(map(int, input().split())))
# K = int(input())
# jump.append(K)
# dp = [[sys.maxsize for _ in range(2)] for _ in range(21)]
# dp[1][0] = 0
# dp[2][0] = jump[1][0]
# dp[3][0] = min(jump[1][0]+jump[2][0], jump[2][1])
#
# if N >= 4:
#     for i in range(4, N):
#         dp[i][0] = min(dp[i-2][0]+jump[i-2][1], dp[i-1][0]+jump[i][0])
#         dp[i][1] = min(min(dp[i-1][1]+jump[i-1][1], dp[i-2][1]+jump[i-2][1]),
#                     K + dp[i-3][0])
#
# print(min(dp[N][0], dp[N][1]))
