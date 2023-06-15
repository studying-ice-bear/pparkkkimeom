N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

blue = 0
white = 0


def bt(x, y, N):
    global white, blue
    color = graph[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != graph[i][j]:
                bt(x, y, N // 2)
                bt(x, y + N // 2, N // 2)
                bt(x + N // 2, y, N // 2)
                bt(x + N // 2, y + N // 2, N // 2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1


bt(0, 0, N)
print(white)
print(blue)
