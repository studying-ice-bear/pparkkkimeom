# https://www.acmicpc.net/problem/20437
# 520 ms
T = int(input())

for _ in range(T):
    W = input()
    K = int(input())

    # 알파벳별로 갯수 세는 리스트
    countList = [0 for _ in range(26)]
    # 알파벳별로 인덱스 리스트 관리하는 리스트
    alphaList = [[] for _ in range(26)]

    for idx in range(len(W)):
        countList[ord(W[idx])-97] += 1
        alphaList[ord(W[idx])-97].append(idx)

    hasAnswer = False
    for count in countList:
        if count >= K:
            hasAnswer = True
            break
    if not hasAnswer:
        print(-1)
        continue

    minLength = float('inf')
    maxLenght = float('-inf')

    for idx in range(26):
        if countList[idx] >= K:
            for eachIdx in range(K-1, len(alphaList[idx])):
                tempLength = alphaList[idx][eachIdx] - \
                    alphaList[idx][eachIdx - (K-1)] + 1
                minLength = min(minLength, tempLength)
                maxLenght = max(maxLenght, tempLength)

    print(minLength, maxLenght)
