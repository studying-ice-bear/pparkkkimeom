import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
money = [0] + list(map(int, input().split()))
friend = [i for i in range(N+1)]


def find(x):
    if x != friend[x]:
        friend[x] = find(friend[x])
    return friend[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if money[x] < money[y]:
        friend[y] = x
    else:
        friend[x] = y


for _ in range(M):
    v, w = map(int, input().split())
    union(v, w)

group = set()
total = 0
for i in range(1, N+1):
    if find(i) not in group:
        total += money[friend[i]]
        group.add(friend[i])

if total <= K:
    print(total)
else:
    print("Oh no")
