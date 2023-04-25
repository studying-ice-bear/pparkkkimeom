import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
dp = [0] * (K+1)
dp[0] = 1

for _ in range(N):
    coin.append(int(input()))

for i in range(N):
    for j in range(coin[i], K+1):
        dp[j] += dp[j-coin[i]]

print(dp[K])

'''
문제 풀이 아이디어:
점화식을 찾자!
https://velog.io/@jxlhe46/%EB%B0%B1%EC%A4%80-2293%EB%B2%88.-%EB%8F%99%EC%A0%84-1-bfi120m5

'''