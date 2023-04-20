
N = int(input())

# 2. DP를 이용한 방법, 게임 횟수에 따른 승패 결정
dp = [0] * (N+1)
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = min(dp[i-1]+1, dp[i-3]+1)

if dp[N] % 2 == 1:
    print("SK")
else:
    print("CY")

'''
첫 번째 문제 풀이 아이디어:
1. 홀수, 짝수 
홀수 개일 때 상근이가 승
짝수 개일 때 창섭이가 승
N = int(input())

if N % 2 == 0:
    print("CY")
else:
    print("SK")

'''