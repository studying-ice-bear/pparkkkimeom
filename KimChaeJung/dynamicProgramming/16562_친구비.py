# 참고: https://www.jongung.com/292
# https://www.acmicpc.net/problem/16562
# 6728 ms
fCount, fRelCount, money = map(int, input().split())

fPriceList = [0]
fPriceList.extend(list(map(int, input().split())))

parent = [i for i in range(fCount + 1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(fRelCount):
    a, b = map(int, input().split())
    union(a, b)

subSet = []
visited = [0 for _ in range(fCount+1)]

for nodeIdx in range(fCount + 1):
    tempSet = []
    if visited[nodeIdx]:
        continue
    tempSet.append(nodeIdx)
    thisParentNode = find(nodeIdx)
    for nextNodeIdx in range(nodeIdx + 1, fCount + 1):
        if thisParentNode == find(nextNodeIdx):
            tempSet.append(nextNodeIdx)
            visited[nextNodeIdx] = 1
    visited[nodeIdx] = 1
    subSet.append(tempSet)

allFriendMoney = 0

for subElement in subSet[1:]:
    minMoney = float('inf')
    for friend in subElement:
        minMoney = min(minMoney, fPriceList[friend])
    allFriendMoney += minMoney

print(allFriendMoney if allFriendMoney <= money else 'Oh no')


# https://www.acmicpc.net/problem/16562
# 6748 ms
fCount, fRelCount, money = map(int, input().split())

fPriceList = [0]
fPriceList.extend(list(map(int, input().split())))

parent = [i for i in range(fCount + 1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(fRelCount):
    a, b = map(int, input().split())
    union(a, b)

subSet = []
visited = [0 for _ in range(fCount+1)]

for nodeIdx in range(fCount + 1):
    tempSet = []
    if visited[nodeIdx]:
        continue
    tempSet.append(nodeIdx)
    thisParentNode = find(nodeIdx)
    for nextNodeIdx in range(nodeIdx + 1, fCount + 1):
        if thisParentNode == find(nextNodeIdx):
            tempSet.append(nextNodeIdx)
            visited[nextNodeIdx] = 1
    visited[nodeIdx] = 1
    tempSet.sort(key=lambda a: fPriceList[a])
    subSet.append(tempSet)

allFriendMoney = 0

for subElement in subSet[1:]:
    allFriendMoney += fPriceList[subElement[0]]

print(allFriendMoney if allFriendMoney <= money else 'Oh no')
