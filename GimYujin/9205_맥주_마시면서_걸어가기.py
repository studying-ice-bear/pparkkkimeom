from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())  # 편의점 개수
    # 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표

    start = list(map(int, input().split()))

    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))

    end = list(map(int, input().split()))

    visited = [False for i in range(N+1)]


    def solution():
        queue = deque()
        queue.append(start)

        # bfs보단 stack을 활용하는 듯한 느낌
        while queue:
            nx, ny = queue.popleft()

            if abs(nx - end[0]) + abs(ny - end[1]) <= 1000:
                return "happy"

            for i in range(N):
                if not visited[i]:
                    xx, yy = data[i]
                    if abs(nx-xx) + abs(ny-yy) <= 1000:
                        queue.append([xx, yy])
                        visited[i] = True

        return "sad"


    print(solution())

'''
20병 50미터에 한 병씩 마심 -> 1000
편의점에서 빈 병은 버리고 새 맥주 병을 살 수 있다.
맥주 20개까지
두 좌표 사이의 거리 : x 좌표의 차이 + y 좌표의 차이

2
0 0
-1000 0
1000 0
2000 2000
"sad"

2
0 0
-1000 0
1000 0
1000 1000
"happy"

1
3
1000 0
2000 1000
3000 0
2000 1000
2000 2000
"sad"

1
3
1000 0
2000 1000
2000 0
2000 1000
2000 2000
"happy"

1
2
0 0
-1000 0
-1000 -1000
-1000 -2000
"happy"

1
2
0 0
100 0
20 0
-1000 -1000
"sad"

1
2
0 0
0 -1000
20 0
-1000 -1000
"happy"

그리디 알고리즘을 활용하면?
반례: 
1
2
0 500
-1000 1000
1000 500
1000 1500
"happy"


'''