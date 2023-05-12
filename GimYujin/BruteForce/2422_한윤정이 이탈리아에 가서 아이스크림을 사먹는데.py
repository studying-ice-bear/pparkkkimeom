from collections import deque, defaultdict
from copy import copy

comb = deque()
answer = 0
N, M = map(int, input().split())
notTogether = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    notTogether[a].append(b)
    notTogether[b].append(a)

result = [0] * 3
numbers = [i for i in range(1, N+1)]

def dfs(depth, num):
    global answer
    if depth == 3:
        # print(*result)

        new_result = copy(result)
        new_result.sort()
        if new_result not in comb:
            answer += 1
            comb.append(new_result)
        return

    for i in range(num, N+1):

        if i in notTogether[num]:
            continue

        if num in notTogether[i]:
            continue

        if visited[i]:
            continue

        visited[i] = True
        result[depth] = i
        visited[i] = True
        dfs(depth+1, i)
        visited[i] = False


for i in range(1, N+1):
    visited = [False] * (N + 1)
    dfs(0, i)

print(answer)
