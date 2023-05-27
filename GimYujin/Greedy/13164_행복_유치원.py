import sys, math
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * N

for i in range(1, N):
    dp[i] = arr[i] - arr[i-1]

dp.sort()
answer = 0
for i in range(N-K+1):
    answer += dp[i]
print(answer)

'''
참고: https://dkswnkk.tistory.com/591,
https://velog.io/@ich0906/%EB%B0%B1%EC%A4%80-13164-%ED%96%89%EB%B3%B5-%EC%9C%A0%EC%B9%98%EC%9B%90

'''