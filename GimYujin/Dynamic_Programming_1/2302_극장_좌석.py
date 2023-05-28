import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
dp = [0] * (N+1)
fixed = [False] * (N+1)

for _ in range(M):
    n = int(input())
    fixed[n] = True

dp[0] = 1
dp[1] = 1
for i in range(2, N+1):
    if fixed[i] or fixed[i-1]:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[N])

'''
1~N번
1<= N <= 40

자기의 왼쪽 좌석 또는 바로 오른쪽 좌석으로는 자리를 옮길 수 있다.
VIP 회원들: 반드시 자기 좌석에만 앉아야 한다.
출력: 사람들이 좌석에 앉을 수 있는 방법의 가짓수


3
3
1
2
3
'''