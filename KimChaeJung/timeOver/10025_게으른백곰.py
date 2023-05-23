# https://www.acmicpc.net/problem/10025
# 시간 초과
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())

pointList = []
for _ in range(N):
    iceCount, point = map(int, input().strip().split())
    pointList.append([iceCount, point])

pointList.sort(key=lambda x: x[1])

maxIceCount = 0

for firstIdx in range(len(pointList)):
    ice01, point01 = pointList[firstIdx]
    iceCount = ice01
    for secondIdx in range(firstIdx + 1, len(pointList)):
        ice02, point02 = pointList[secondIdx]
        if point02 > point01 + K*2:
            break
        iceCount += ice02

    maxIceCount = max(iceCount, maxIceCount)

# for i in range(K, pointList[-1][1]-K+1):
#     iceCount = 0
#     for ice in pointList:
#         if i-K <= ice[1] <= i+K:
#             iceCount += ice[0]
#     maxIceCount = max(iceCount, maxIceCount)

print(maxIceCount)
