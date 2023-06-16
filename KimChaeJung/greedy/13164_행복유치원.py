# https://www.acmicpc.net/problem/13164

# 236ms

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
childrenList = list(map(int, input().split()))
gapList = [childrenList[i] - childrenList[i-1] for i in range(1, N)]
gapList.sort()

print(sum(gapList[:(N-1)-(K-1)]))
