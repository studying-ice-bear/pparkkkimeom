from collections import deque

R, C = map(int, input().split())
graph = []
sea = deque()

for i in range(R):
    tmp = input().strip()
    arr = []
    for j in range(C):
        if tmp[j] == 'X':
            sea.append((i, j))
        arr.append(tmp[j])
    graph.append(arr)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[False] * C for _ in range(R)]

while sea:
    sx, sy = sea.popleft()
    count = 0
    visited[sx][sy] = True

    for i in range(4):
        xx = sx + dx[i]
        yy = sy + dy[i]

        if xx < 0 or xx >= R or yy < 0 or yy >= C:
            count += 1
            continue

        if not visited[xx][yy] and graph[xx][yy] == '.':
            count += 1

    if count >= 3:
        graph[sx][sy] = '.'

    # print(*graph, sep="\n")
    # print(*visited, sep="\n")

check = []
check_i = []
check_j = []
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'X':
            check.append((i, j))

            if i not in check_i:
                check_i.append(i)
            if j not in check_j:
                check_j.append(j)

# print(check_i, check_j)
# print(check)

if not check:
    print('X')
else:
    for node in graph[min(check_i):max(check_i)+1]:
        print(*node[min(check_j):max(check_j)+1], sep="")

'''
10 10
..........
....XXX...
XXX....XXX
..........
..........
XX........
..........
..........
..........
..........
->
.....X....
.X......X.
..........
..........
.X........

3 1
X
X
X

3 3
XXX
XXX
XXX
->
XXX
XXX
XXX


3 3
.X.
.X.
...
->
X

3 3
X..
.X.
...
->
X

'''