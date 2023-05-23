# https://www.acmicpc.net/problem/18352
# 시간 초과
'''
import sys
input = sys.stdin.readline

city, node, target, start = map(int, input().split())

cityInfo = [[] for _ in range(city+1)]
shortInfo = [1000000 for _ in range(city+1)]

for _ in range(node):
    a, b = map(int, input().split())
    cityInfo[a].append(b)


def BFS(mapInfo, firstNode):
    distance = 0
    visited = [firstNode]
    queue = [firstNode]

    while queue:
        cur_node = queue.pop(0)

        shortInfo[cur_node] = min(shortInfo[cur_node], distance)

        for node in mapInfo[cur_node]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
                shortInfo[node] = min(shortInfo[node], distance+1)
        distance += 1


BFS(cityInfo, start)

hasAnswer = False

for cityIdx in range(len(shortInfo)):
    if shortInfo[cityIdx] == target:
        print(cityIdx)
        hasAnswer = True

if hasAnswer == False:
    print(-1)
'''

# 2752ms

import heapq
import sys
input = sys.stdin.readline

inf = float("inf")

city, node, target, start = map(int, input().split())

cityInfo = [[] for _ in range(city+1)]

for _ in range(node):
    a, b = map(int, input().split())
    cityInfo[a].append(b)


def dijkstra(mapInfo, start):
    distances = [float("inf") for _ in range(city+1)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        curDistance, curNode = heapq.heappop(queue)

        if distances[curNode] < curDistance:
            continue

        for newNode in mapInfo[curNode]:
            if curDistance + 1 < distances[newNode]:
                distances[newNode] = curDistance + 1
                heapq.heappush(queue, [curDistance + 1, newNode])

    return distances


shortInfo = dijkstra(cityInfo, start)

noAnswer = True
for cityIdx in range(len(shortInfo)):
    if shortInfo[cityIdx] == target:
        print(cityIdx)
        noAnswer = False

if noAnswer:
    print(-1)
