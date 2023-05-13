from collections import deque
V, E = map(int, input().split())

weight = []

for _ in range(E):
    a, b, c = map(int, input().split())
    weight.append((c, a, b))

weight.sort()

union_find = [i for i in range(V+1)]
pick = []


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


total = 0
for w in weight:
    pick.append((w[1], w[2]))
    if find_parent(union_find, w[1]) != find_parent(union_find, w[2]):
        union_parent(union_find, w[1], w[2])
        total += w[0]
    # print(pick, union_find)
print(total)

def dfs(start):
    visited = []
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.append(node)


