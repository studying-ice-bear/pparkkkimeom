from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [0] * (N+1)
visited = [False] * (N+1)


def bfs():
    answer = []
    que = deque([X])
    visited[X] = True
    distance[X] = 0

    while que:
        now = que.popleft()
        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                distance[node] = distance[now] + 1
                que.append(node)

                if distance[node] == K:
                    answer.append(node)

    if not answer:
        print(-1)
    else:
        print(*answer, sep="\n")


bfs()
