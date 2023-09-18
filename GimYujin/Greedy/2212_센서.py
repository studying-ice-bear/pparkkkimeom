N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()
dp = [0] * N

if N < K:
    print(0)
else:
    for i in range(1, len(arr)):
        dp[i] = arr[i] - arr[i-1]

    dp.sort(reverse=True)
    answer = 0
    for i in range(K-1, N):
        answer += dp[i]

    print(answer)

'''
1, 3, 6, 7, 9
  2  3  1  2 

'''