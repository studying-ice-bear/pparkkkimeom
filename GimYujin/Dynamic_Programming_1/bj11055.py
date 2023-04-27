import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = arr[0]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i], arr[i]+arr[j])

print(max(dp))

# 이전 코드 : 버블 정렬할 때 이전 원소만 비교
# for i in range(1, N):
#     print(arr[i], arr[i+1])
#     if arr[i] < arr[i+1]:
#         dp[i] = dp[i-1] + arr[i]
#     else:
#         dp[i] = dp[i-1]
#     print(dp)

'''
문제 풀이 아이디어: 작은 문제로 나누기 - DP


10
1 100 2 50 60 3 5 6 7 8
답: 113

10
1 100 2 50 60 3 50 60 70 80
답: 266

5
1 8 2 3 9
답: 18

'''