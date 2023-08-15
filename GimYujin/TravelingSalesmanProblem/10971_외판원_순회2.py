'''
참고 코드: https://velog.io/@y7y1h13/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-10971%EB%B2%88-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-2python

'''
import sys

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

answer = sys.maxsize
visited = [False for _ in range(N)]


def dfs(start, now, value, cnt):
    global answer
    if cnt == N:
        if graph[now][start]:
            value += graph[now][start]
            answer = min(answer, value)

    if value > answer:
        return

    for i in range(N):
        if not visited[i] and graph[now][i]:
            visited[i] = True
            dfs(start, i, value+graph[now][i], cnt+1)
            visited[i] = 0


for i in range(N):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(answer)


# import sys
# N = int(input())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, input().split())))
#
#
# answer = sys.maxsize
#
# visited = [False for _ in range(N)]
# def dfs(node, cnt):
#     global answer, cost
#
#     if cnt == N:
#         answer = min(answer, cost)
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             cost += graph[node][i]
#             dfs(i, cnt+1)
#             visited[i] = False
#             cost -= graph[node][i]
#             dfs(i, cnt-1)
#
#
# for i in range(N):
#     cost = 0
#     dfs(i, 0)
#
# print(answer)

'''
i에서 j로 가는 값이랑 j에서 i로 가는 값이 다르고,
시작위치가 다른데?

'''