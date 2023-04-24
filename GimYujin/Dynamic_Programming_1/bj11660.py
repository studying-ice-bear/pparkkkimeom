'''
문제 풀이 아이디어:
1) 누적합을 저장하는 배열을 따로 두기
2) 누적합을 구하는 방법
    - 누적합 배열은 0을 추가로 넣어주자
3) 누적합 간의 차를 이용해 특정 점들 사이의 합 구하기
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))


dp = [[0] * (N + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + graph[i - 1][j - 1]

for k in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(result)

'''
이전 코드:
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
total = [[0]*(N) for _ in range(N)]
graph = []

tmp = 0
for i in range(N):
    graph.append(list(map(int, input().split())))

    for j in range(N):
        tmp += graph[i][j]
        total[i][j] = tmp


for i in range(N):
    for j in range(N):
        total[i][j] = total[i-1][j] + total[i][j-1] - total[i][j] + graph[i][j]
print(*total, sep='\n')

for i in range(N):
    if i == 0:
        continue

    for j in range(N):
        if j == 0:
            total[i][j] = total[i-1][j] + graph[i][j]
        else:
            total[i][j] = total[i-1][j] + total[i][j-1] - total[i-1][j-1] + graph[i][j]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    if x1 == x2 and y1 == y2:
        answer = graph[x2][y2]
    elif x1 == 0 and y1 == 0:
        answer = total[x2][y2]
    elif x1 == x2:
        answer = total[x2][y2] - total[x2-1][y2]
    elif y1 == y2:
        answer = total[x2][y2] - total[x2-1][y2]
    else:
        answer = total[x2][y2] - (total[x1-1][y2] + total[x2][y1-1] - total[x1-1][y1-1])
    print(answer)
'''
'''TestCases
1 3 6 10
3 8 15 24
6 15 27 42
10 
'''