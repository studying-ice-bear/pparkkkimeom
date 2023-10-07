# https://www.acmicpc.net/problem/6503
# 2884 ms
while True:
    num = int(input())
    if num == 0:
        break
    inputStr = list(input())

    keyboardDict = {}
    idx = 0
    while len(keyboardDict.keys()) < num:
        if idx >= len(inputStr): break
        currStr = inputStr[idx]
        if currStr in keyboardDict.keys():
            keyboardDict[currStr] += 1
        else:
            keyboardDict[currStr] = 1
        idx += 1
    
    answer = idx

    start = 0
    while start < idx:
        if idx >= len(inputStr): break
        if inputStr[idx] not in keyboardDict.keys():
            while True:
                if keyboardDict[inputStr[start]] == 1:
                    del keyboardDict[inputStr[start]]
                    start += 1
                    break
                else:
                    keyboardDict[inputStr[start]] -= 1
                    start += 1
            keyboardDict[inputStr[idx]] = 1
        else:
            keyboardDict[inputStr[idx]] += 1

        answer = max(answer, idx - start + 1)
        idx += 1

    print(answer)
        

    
