# https://www.acmicpc.net/problem/26069
# 80 ms
pplCount = int(input())

pplInfo = {}


def addValue(a, b):
    if a in pplInfo:
        pplInfo[a].append(b)
    else:
        pplInfo[a] = [b]
    if b in pplInfo:
        pplInfo[b].append(a)
    else:
        pplInfo[b] = [a]


for _ in range(pplCount):
    a, b = input().split()
    if a == 'ChongChong' or b == 'ChongChong':
        addValue(a, b)
        continue
    if a in pplInfo or b in pplInfo:
        addValue(a, b)
        continue

print(len(pplInfo.keys()))
