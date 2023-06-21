# https://www.acmicpc.net/problem/16928

# 44ms

sadari, bam = map(int, input().split())
numGraph = {n: [] for n in range(1, 101)}

for _ in range(sadari):
    a, b = map(int, input().split())
    numGraph[a].append((0, b))

for _ in range(bam):
    a, b = map(int, input().split())
    numGraph[a].append((0, b))

for key, value in numGraph.items():
    if value == []:
        for i in range(1, 7):
            if key + i > 100:
                break
            numGraph[key].append((i, key+i))


def BFS(boardInfo):
    visited = [0 for _ in range(101)]
    queue = [(1, 0)]
    visited[1] = 1
    while queue:
        queue.sort(key=lambda x: x[1])
        curCell, curRollCount = queue.pop(0)

        if curCell == 100:
            print(curRollCount)
            return

        for roll, goTo in boardInfo[curCell]:
            if roll == 0:
                visited[goTo] = 1
                queue.append((goTo, curRollCount))
                continue
            if visited[goTo] == 0:
                visited[goTo] = 1
                queue.append((goTo, curRollCount+1))


BFS(numGraph)
