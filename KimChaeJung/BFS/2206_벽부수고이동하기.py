# https://www.acmicpc.net/problem/2206
# https://www.acmicpc.net/board/view/109499
# 시간초과
import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())

mapInfo = []
for _ in range(N):
    mapRow = list(input().strip())
    mapInfo.append(mapRow)


def BFS(graph, start):
    distances = [[[float("inf"), False] for _ in range(M)] for _ in range(N)]
    distances[start[0]][start[1]][0] = 1
    queue = []
    heapq.heappush(queue, [1, start])

    while queue:
        curDistance, (curR, curC) = heapq.heappop(queue)

        isWallBrokenInCur = distances[curR][curC][1]
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        for i in range(4):
            newR, newC = curR+dr[i], curC+dc[i]
            if 0 > newR or newR >= N or 0 > newC or newC >= M:
                continue
            isWallBrokenInNew = distances[newR][newC][1]
            if distances[newR][newC][0] != float("inf"):
                if isWallBrokenInCur == False:
                    if isWallBrokenInNew == True:
                        distances[newR][newC][1] = False
                    else:
                        continue
                else:
                    continue
            if graph[newR][newC] == '1' and isWallBrokenInCur == True:
                continue

            if graph[newR][newC] == '1' and isWallBrokenInCur == False:
                distances[newR][newC][1] = True
            else:
                distances[newR][newC][1] = isWallBrokenInCur
            distances[newR][newC][0] = curDistance + 1
            heapq.heappush(queue, [curDistance+1, (newR, newC)])

    return distances


distanceInfo = BFS(mapInfo, (0, 0))
answer = distanceInfo[N-1][M-1][0]

if answer == float('inf'):
    print(-1)
else:
    print(answer)
