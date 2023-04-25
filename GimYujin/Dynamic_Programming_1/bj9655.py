
N = int(input())

# 2. DP를 이용한 방법, 게임 횟수에 따른 승패 결정
dp = [-1]*1001

dp[1] = 1
dp[2] = 0
dp[3] = 1

for i in range(4, N+1):
    if dp[i-1] or dp[i-3]:
        dp[i] = 0
    else:
        dp[i] = 1
print('CY' if dp[N] == 0 else 'SK')

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