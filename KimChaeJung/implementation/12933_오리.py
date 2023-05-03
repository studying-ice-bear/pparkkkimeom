# https://www.acmicpc.net/problem/12933
# 76ms
recordedSound = input()

recordedStack = [0 for _ in range(501)]

duckCount = 0

for sound in recordedSound:
    checkFlag = False
    for idx in range(1, 501):
        if sound == 'q' and recordedStack[idx] == 0:
            recordedStack[idx] += 1
            checkFlag = True
            break
        if sound == 'q' and recordedStack[idx] == 5:
            recordedStack[idx] = 1
            checkFlag = True
            break
        if sound == 'u' and recordedStack[idx] == 1:
            recordedStack[idx] += 1
            checkFlag = True
            break
        if sound == 'a' and recordedStack[idx] == 2:
            recordedStack[idx] += 1
            checkFlag = True
            break
        if sound == 'c' and recordedStack[idx] == 3:
            recordedStack[idx] += 1
            checkFlag = True
            break
        if sound == 'k' and recordedStack[idx] == 4:
            recordedStack[idx] += 1
            checkFlag = True
            break
    if checkFlag == False:
        print(-1)
        exit()

for stack in recordedStack[1:]:
    if stack == 0:
        break
    if stack == 5:
        duckCount += 1
    if stack != 5:
        duckCount = -1
        break

print(duckCount)