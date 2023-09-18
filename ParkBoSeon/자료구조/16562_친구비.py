import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)
def dfs(v, arr):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(i, arr)
    

n, m, k = map(int, input().split())
A = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
friends = []
answer = 0

for _ in range(m):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)
    

for i in range(1, n + 1):
    if not visited[i]:
        arr = [i]
        visited[i] = True
        dfs(i, arr)
        friends.append(arr)

for friend in friends:
    cost = 10000001
    
    for j in friend:
        if cost > A[j]:
            cost = A[j]
    answer += cost
    
if answer <= k:
    print(answer)
else:
    print("Oh no")