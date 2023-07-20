from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in range(1, N+1):
        if data[j-1] == 1:
            graph[i].append(j)

answer = [[0 for _ in range(N)] for _ in range(N)]
visited = [False for _ in range(N+1)]
# def dfs(check, node):
#     visited[node] = True
#     for i in graph[node]:
#         if not visited[i]:
#             visited[node] = True
#             answer[check][node-1] = 1
#             dfs(check, i)
#     return

def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [False for _ in range(N+1)]

    while queue:
        x = queue.popleft()
        for node in graph[x]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
                answer[start-1][node-1] = 1

for i in range(1, N+1):
    bfs(i)
    # dfs(i, i)

for ans in answer:
    print(*ans)
