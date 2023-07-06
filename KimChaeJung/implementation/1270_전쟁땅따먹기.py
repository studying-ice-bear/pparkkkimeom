# https://www.acmicpc.net/problem/1270

# 11984ms
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

'''
for i in range(n):
    soldierList = list(map(int, input().split()))
    soldierCount = soldierList[0]
    soldierDict = {}
    answer = 'SYJKGW'
    for idx in range(1, soldierCount+1):
        curSoldier = soldierList[idx]
        if soldierDict.get(curSoldier):
            soldierDict[curSoldier] += 1
            if soldierDict[curSoldier] >= soldierCount//2 + 1:
                answer = curSoldier
                break
        else:
            soldierDict[curSoldier] = 1
    print(answer)
'''
# 5916ms


def boyer_moore(arr, soldierCount):
    count = 0
    major = 0
    for soldier in arr:
        if count == 0:
            major = soldier
        if major == soldier:
            count += 1
        else:
            count -= 1
    half = soldierCount//2 + 1
    majorCount = arr.count(major)
    if majorCount >= half:
        return major
    else:
        return False
    # 6616 ms
    '''
    majorCount = 0
    for target in arr:
        if target == major:
            majorCount += 1
            if majorCount >= half:
                return major
    return False
    '''


for _ in range(n):
    soldierList = list(map(int, input().split()))
    soldierCount = soldierList.pop(0)
    answer = boyer_moore(soldierList, soldierCount)
    # 6108ms
    # soldierCount = soldierList.popleft()
    # answer = boyer_moore(soldierList, soldierCount)
    if answer == False:
        answer = 'SYJKGW'
    print(answer)
