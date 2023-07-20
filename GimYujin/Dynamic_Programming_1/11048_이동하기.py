N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [1, 0, 1]
dy = [0, 1, 1]

dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = arr[0][0]
for i in range(N):
    for j in range(M):
        print(j)
        for k in range(3):
            ni = i + dx[k]
            nj = j + dy[k]

            if 0 <= ni < N and 0 <= nj < M:
                dp[ni][nj] = max(dp[i][j] + arr[ni][nj], dp[ni][nj])

        print(*dp, sep="\n")
    print()
print(dp[N-1][M-1])
