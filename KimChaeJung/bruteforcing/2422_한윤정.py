# https://www.acmicpc.net/problem/2422

# 1204ms

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

noMix = {icecreamNum: [] for icecreamNum in range(N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    noMix[a].append(b)
    noMix[b].append(a)


for (num, blackList) in noMix.items():
    if num == 0:
        continue
    entireList = [i for i in range(1, N+1)]
    possibleSetList = list(
        filter(lambda x: x not in blackList and x > num, entireList))
    noMix[num] = possibleSetList

possibleList = []
answer = 0
for (firstNum, possible) in noMix.items():
    if firstNum == 0:
        continue
    for secondNum in noMix[firstNum]:
        for thirdNum in noMix[secondNum]:
            if thirdNum in possible:
                answer += 1

print(answer)
