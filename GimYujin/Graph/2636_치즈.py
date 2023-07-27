'''
    문제 아이디어: 공기를 체크해서 가장자리 판별하기
'''

from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def leftover():     # 남은 치즈의 개수를 찾는 함수.
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                count += 1
    return count


def checkEdge():
    '''
        1. 가장자리 찾기
        2. 가장자리 녹기
    '''
    queue = deque()
    queue.appendleft((0, 0))

    edge = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

                    elif graph[nx][ny] == 1:
                        graph[nx][ny] = -1
                        edge.append((nx, ny))

    while edge:
        x, y = edge.popleft()
        graph[x][y] = 0


time = 0
leftCheese = 0
while True:
    tmp = leftover()
    if tmp == 0:
        break

    leftCheese = tmp
    checkEdge()
    time += 1

print(time)
print(leftCheese)

#
# def checkMelt():
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 0:
#                 continue
#
#             for k in range(4):
#                 ni = i + dx[k]
#                 nj = j + dy[k]
#
#                 if 0 <= ni < N and 0 <= nj < M:
#                     if graph[ni][nj] == -1:
#                         graph[ni][nj] = 2
#                         break
#
#
# def melt():
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 2:
#                 graph[i][j] = 0



# time = 0
# leftCheese = 0
# while True:
#     tmp = leftover()
#
#     if tmp == 0:
#         time += 1
#         break
#
#     check()
#     time += 1
#     leftCheese = tmp
#
#     print(time)
#     for i in range(N):
#         print(*graph[i])
#
# print(time)
# print(leftCheese)

'''
5 5
0 0 0 0 0
0 1 1 1 0 
0 1 1 1 0
0 1 1 1 0
0 0 0 0 0

5 5
0 0 0 0 0
0 2 2 2 0 
0 2 1 2 0
0 2 2 2 0
0 0 0 0 0

5 5
0 0 0 0 0
0 0 0 0 0 
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0

5 5
0 0 0 0 0
0 0 0 0 0 
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
'''