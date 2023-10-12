'''
왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
'''

N = int(input())
graph = []
for _ in range(N):
    tmp = input().strip()
    arr = list(int(num) for num in tmp)
    graph.append(arr)


def recursion(r, c, cnt):
    color = graph[r][c]

    for i in range(r, r+cnt):
        for j in range(c, c+cnt):
            if color != graph[i][j]:
                print("(", end="")
                recursion(r, c, cnt // 2)
                recursion(r, c + cnt // 2, cnt // 2)
                recursion(r + cnt // 2, c, cnt // 2)
                recursion(r + cnt // 2, c + cnt // 2, cnt // 2)
                print(")", end="")
                return

    print(graph[r][c], end="")


recursion(0, 0, N)

'''
4
0000
1010
1100
1100
((0010)(0010) 1 0)
((0010)(0010)10)

'''