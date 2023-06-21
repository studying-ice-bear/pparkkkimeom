# https://www.acmicpc.net/problem/9205

# 52ms

import sys
import itertools
input = sys.stdin.readline

testCaseNum = int(input())


def BFS(mapInfo, start, end):
    allNode = []
    allNode.append(start)
    allNode.extend(mapInfo)
    allNode.append(end)

    for nodeIdx in range(len(allNode)):
        allNode[nodeIdx].append(nodeIdx)

    graph = [[] for _ in range(len(allNode))]

    for node1, node2 in itertools.combinations(allNode, 2):
        if abs(node1[0]-node2[0]) + abs(node1[1]-node2[1]) <= 50*20:
            graph[node1[2]].append(node2[2])
            graph[node2[2]].append(node1[2])

    visited = [0]
    queue = []
    queue.extend(graph[0])
    while queue:
        cur_node = queue.pop(0)

        for node in graph[cur_node]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
    return visited


for _ in range(testCaseNum):
    cvsNum = int(input())
    sanggeun = list(map(int, input().split()))
    cvsList = []
    for _ in range(cvsNum):
        cvsList.append(list(map(int, input().split())))
    rockFestival = list(map(int, input().split()))

    if abs(rockFestival[1] - sanggeun[1]) + abs(rockFestival[0]-sanggeun[0]) <= 50*20:
        print('happy')
        continue

    visited = BFS(cvsList, sanggeun, rockFestival)

    if (cvsNum+1) in visited:
        print('happy')
    else:
        print('sad')
