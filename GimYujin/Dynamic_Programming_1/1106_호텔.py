import sys
input = sys.stdin.readline

C, N = map(int, input().split())
money = []
for _ in range(N):
    a, b = map(int, input().split())
    money.append([a, b])

dp = [1000 * 100 for i in range(C+100)]
dp[0] = 0

for c, n in money:
    for i in range(n, C+100):
        dp[i] = min(dp[i], dp[i-n]+c)

print(min(dp[C:]))

'''
참고: https://bio-info.tistory.com/218
왜 C+100인지?: https://www.acmicpc.net/board/view/107696
'''