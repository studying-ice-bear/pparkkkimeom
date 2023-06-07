import sys
input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

count = min(N, M) // 2
for cnt in range(count):
    total = 2 * ((N-2*cnt) + (M-2*cnt) - 2)
    for r in range(R % total):
        n_max = N - cnt - 1
        m_max = M - cnt - 1

        tmp = graph[cnt][cnt]

        for j in range(cnt, m_max):
            graph[cnt][j] = graph[cnt][j+1]

        for i in range(cnt, n_max):
            graph[i][m_max] = graph[i+1][m_max]

        for j in range(m_max, cnt, -1):
            graph[n_max][j] = graph[n_max][j-1]

        for i in range(n_max, cnt, -1):
            graph[i][cnt] = graph[i-1][cnt]

        graph[cnt + 1][cnt] = tmp


for arr in graph:
    print(*arr)

'''
4 4 12
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

4 5 14
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20

5 4 7
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28

4 2 3
1 2
3 4
5 6
7 8

'''