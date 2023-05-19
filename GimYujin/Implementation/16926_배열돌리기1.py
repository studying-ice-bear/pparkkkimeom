N, M, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


def rotate():
    check = min(N, M) // 2

    for cnt in range(check):
        n_max = N - cnt - 1
        m_max = M - cnt - 1

        tmp = graph[cnt][cnt]

        for i in range(cnt, m_max):
            graph[cnt][i] = graph[cnt][i+1]

        for i in range(cnt, n_max):
            graph[i][m_max] = graph[i+1][m_max]

        for i in range(m_max, cnt, -1):
            graph[n_max][i] = graph[n_max][i-1]

        for i in range(n_max, cnt, -1):
            graph[i][cnt] = graph[i-1][cnt]

        graph[cnt+1][cnt] = tmp


for i in range(R):
    rotate()

for x in graph:
    print(*x, sep=" ")


'''
참고한 코드: https://dkanxmstmdgml.tistory.com/731
다시 풀어보기!!
'''