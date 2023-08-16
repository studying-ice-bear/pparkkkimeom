import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

gameBoard = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break
        jump = gameBoard[i][j]
        
        if i + jump < n:
            dp[i + jump][j] += dp[i][j]
        if j + jump < n:
            dp[i][j + jump] += dp[i][j]
            
            
##############################################
# def bfs(x, y, c):
#     # if x == n - 1 and y == n - 1:
#     #     dp[x][y] = c
#     #     return
    
#     # if x + gameBoard[x][y] < n:
#     #     dp[x][y] = min(dp[x][y], c)
#     #     bfs(x + gameBoard[x][y], y, c + 1)
#     # if y + gameBoard[x][y] < n:
#     #     dp[x][y] = min(dp[x][y], c)
#     #     bfs(x, y + gameBoard[x][y], c + 1)
    
#     queue = deque([[x, y, c]])
    
#     while queue:
#         i, j, k = queue.popleft()
        
#         if i == n - 1 and j == n - 1:
#             dp[i][j] = min(dp[i][j], k)
#             continue
        
#         if i + gameBoard[i][j] < n:
#             dp[i][j] = min(dp[i][j], k)
#             queue.append([i + gameBoard[i][j], j, k + 1])
#         if j + gameBoard[i][j] < n:
#             dp[i][j] = min(dp[i][j], k)
#             queue.append([i, j + gameBoard[i][j], k + 1])
    
# n = int(input())

# gameBoard = [list(map(int, input().split())) for _ in range(n)]
# dp = [[101] * n for _ in range(n)]

# bfs(0, 0, 0)

# print(dp[n-1][n-1])

