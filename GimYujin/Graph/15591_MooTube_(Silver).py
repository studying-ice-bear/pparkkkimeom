from collections import deque

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]


for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))


def bfs(usado, start):
    que = deque()
    que.append(start)

    visited = [False for _ in range(N + 1)]
    answer = 0

    while que:
        v = que.popleft()

        for vv, uu in graph[v]:
            if vv != start and not visited[vv]:
                if uu >= usado:
                    answer += 1
                    que.appendleft(vv)
                    visited[vv] = True

    return answer


for i in range(Q):
    k, v = map(int, input().split())
    print(bfs(k, v))
