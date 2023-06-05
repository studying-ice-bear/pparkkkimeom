# https://www.acmicpc.net/problem/22858
# 1704ms
import sys
input = sys.stdin.readline
N, K = map(int, input().split())

finalCard = list(input().split())

Dn = list(map(int, input().split()))

originCard = ['-1' for _ in range(N)]

for i in range(K):

    if i == 0:
        for j in range(N):
            originCard[Dn[j]-1] = finalCard[j]
    else:
        tempCard = ['-1' for _ in range(N)]

        for j in range(N):
            tempCard[Dn[j]-1] = originCard[j]
        originCard = tempCard

print(*list(map(int, originCard)))
