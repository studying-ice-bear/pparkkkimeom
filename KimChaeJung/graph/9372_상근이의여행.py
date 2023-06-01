# https://www.acmicpc.net/problem/9372
# 192ms
import sys
import heapq
input = sys.stdin.readline

T = int(input())


def findAirCount(mapInfo):
    visitied = [0 for _ in range(len(mapInfo))]
    visitied[1] = 1
    airCount = 0

    queue = []
    heapq.heappush(queue, 1)

    while queue:
        curCity = heapq.heappop(queue)

        for nextCity in mapInfo[curCity]:
            if visitied[nextCity] == 1:
                continue
            visitied[nextCity] = 1
            heapq.heappush(queue, nextCity)
            airCount += 1

    return airCount


for _ in range(T):
    N, M = map(int, input().split())
    airInfo = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        airInfo[a].append(b)
        airInfo[b].append(a)
    airCount = findAirCount(airInfo)
    print(airCount)
