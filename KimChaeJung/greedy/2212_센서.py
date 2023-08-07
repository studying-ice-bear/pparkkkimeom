# https://www.acmicpc.net/problem/2212
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensorList = sorted(list(map(int, input().split())))

gapList = []
for idx in range(1, N):
    gapList.append(sensorList[idx] - sensorList[idx-1])

if K >= N:
    print(0)
else:
    # 52 ms
    # print(sum(sorted(gapList)[:-(K-1) if K != 1 else None]))
    # 48 ms
    print(sum(sorted(gapList, reverse=True)[(K-1):]))
