N, M = map(int, input().split())
arr = list(map(int, input().split()))

visited = [False for _ in range(N)]
comb = []
combinations = []
last = -1

def dfs(depth):
    global last
    if depth == M:
        comb.sort()
        if comb not in combinations:
            combinations.append(comb.copy())
        return

    for i in range(N):
        if not visited[i] and last != i:
            comb.append(arr[i])
            visited[i] = True
            last = i
            dfs(depth+1)
            visited[i] = False
            comb.remove(arr[i])


dfs(0)
combinations.sort()
for c in combinations:
    print(*c, sep=" ")
