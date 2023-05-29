from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N+1)

    def dfs(x, cnt):
        visited[x] = True
        for node in graph[x]:
            if not visited[node]:
                cnt = dfs(node, cnt+1)
        return cnt

    # print(dfs(1, 0))

    def bfs(start, cnt):
        que = deque()
        que.append(start)
        visited[start] = True

        while que:
            check = False
            for i in range(1, N + 1):
                if not visited[i]:
                    check = True
                    break

            if check:
                x = que.popleft()
                for node in graph[x]:
                    if not visited[node]:
                        que.append(node)
                        cnt += 1
                        visited[node] = True
            else:
                return cnt

    print(bfs(1, 0))

'''
2
3 3
1 2
2 3
1 3
5 4
2 1
2 3
4 3
4 5

1
3 3
1 2
2 3
1 3

1
5 4
2 1
2 3
4 3
4 5
'''