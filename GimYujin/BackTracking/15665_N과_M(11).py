N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

comb = []


def dfs(depth):
    if depth == M:
        print(*comb)
        return

    last = 0
    for i in range(N):
        if last != arr[i]:
            comb.append(arr[i])
            last = arr[i]
            dfs(depth + 1)
            comb.remove(arr[i])


dfs(0)
