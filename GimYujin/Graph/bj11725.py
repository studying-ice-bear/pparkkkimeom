from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0 for _ in range(N+1)]
visited = [False] * (N+1)


def dfs(n):
    visited[n] = True

    graph[n].sort()
    for node in graph[n]:
        if not visited[node]:
            visited[node] = True
            parent[node] = n
            dfs(node)


def bfs(n):
    que = deque()
    que.append(n)

    while que:
        x = que.popleft()
        visited[x] = True
        for node in graph[x]:
            if not visited[node]:
                visited[node] = True
                parent[node] = x
                que.append(node)


# bfs(1)
dfs(1)
print(*parent[2:], sep='\n')
'''
1: [4, 6]
2: [4]
3: [5, 6]
4: [1, 7]
5: [3, 6]
6: [1, 3]
7: [4]

* dfs로 할 때 재귀 호출 제한을 늘려야 함

'''