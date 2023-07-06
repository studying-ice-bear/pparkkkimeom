# https://www.acmicpc.net/problem/11403
'''
3
0 1 0
0 0 1
1 0 0
(0, 1), (2, 0), (1, 2)

7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
(0, 3), (1, 6), (3, 4), (3, 5), (4, 0), (5, 6), (6, 2)
'''

import sys
input = sys.stdin.readline

N = int(input())

adjacentMatrix = []
distanceMatrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    adjacentMatrix.append(row)
    distanceMatrix.append(row)

for r in range(N):
    for c in range(N):
        if distanceMatrix[r][c] == 0:
            distanceMatrix[r][c] = float('inf')


for midNode in range(N):
    for r in range(N):
        for c in range(N):
            distanceMatrix[r][c] = min(
                distanceMatrix[r][c], distanceMatrix[r][midNode] + distanceMatrix[midNode][c])

for r in range(N):
    for c in range(N):
        if distanceMatrix[r][c] == float('inf'):
            distanceMatrix[r][c] = 0
        else:
            distanceMatrix[r][c] = 1

for row in distanceMatrix:
    print(*row)
