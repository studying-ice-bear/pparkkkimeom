# https://www.acmicpc.net/problem/15565
import sys
input = sys.stdin.readline
N, K = map(int, input().split())

dollList = list(map(int, input().split()))

ryonList = [idx for idx, doll in enumerate(dollList) if doll == 1]

answer = N

if len(ryonList) < K:
    print(-1)
    exit()

for idx in range(len(ryonList)):

    if idx + (K-1) >= len(ryonList):
        break
    answer = min(ryonList[idx + (K-1)] - ryonList[idx]+1, answer)

print(answer)
