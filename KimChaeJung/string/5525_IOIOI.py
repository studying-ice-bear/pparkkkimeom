# https://www.acmicpc.net/problem/5525

# 50점
N = int(input())
length = int(input())
target = input()

oList = []

for charIdx in range(1, length-1):
    if target[charIdx] == 'O':
        if target[charIdx+1] == 'O':
            continue
        if target[charIdx-1] == 'O':
            continue
        oList.append(charIdx)

answer = 0

if len(oList) == 0:
    print(0)
    exit()

for startIdx in range(len(oList)-N+1):
    eachRow = oList[startIdx:startIdx+N]
    isIOI = True
    if (eachRow[-1] != eachRow[0] + 2*(N-1)):
        isIOI = False
    if isIOI:
        answer += 1

print(answer)

# 100점

N = int(input())
length = int(input())
target = input()

oList = []

for charIdx in range(1, length-1):
    if target[charIdx] == 'O':
        if target[charIdx+1] == 'O':
            continue
        if target[charIdx-1] == 'O':
            continue
        oList.append(charIdx)

answer = 0

if len(oList) == 0:
    print(0)
    exit()

for startIdx in range(len(oList)-N+1):
    if (oList[startIdx+N-1] != oList[startIdx] + 2*(N-1)):
        continue
    answer += 1

print(answer)
