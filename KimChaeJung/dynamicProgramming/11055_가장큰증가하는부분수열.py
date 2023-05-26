# https://www.acmicpc.net/problem/11055
# 120 ms
import sys
input = sys.stdin.readline

numCount = int(input())
numList = list(map(int, input().split()))
sumList = [numList[0]]

for numIdx in range(1, len(numList)):
    appendFlag = False
    possibleSumList = []
    for preNumIdx in range(numIdx-1, -1, -1):
        if numList[preNumIdx] < numList[numIdx]:
            possibleSumList.append(numList[numIdx] + sumList[preNumIdx])
    if len(possibleSumList)>0:
        sumList.append(max(possibleSumList))
    else:
        sumList.append(numList[numIdx])

print(max(sumList))