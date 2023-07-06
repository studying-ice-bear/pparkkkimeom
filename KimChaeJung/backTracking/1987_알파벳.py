# https://www.acmicpc.net/problem/1987
# 시간초과

# pypy 6944 ms
import sys
input = sys.stdin.readline
R, C = map(int, input().split())

boardInfo = [[] for _ in range(R)]
for r in range(R):
    row = list(input().strip())

    def convertToNum(string):
        return ord(string)-65

    boardInfo[r] = list(map(convertToNum, row))


'''
alpha라는 리스트를 backtracking 인자로 넘겨 append, pop -> 시간초과
alpha를 문자열로 관리하지 않고 list index로 관리하기 위해 ord mapping 추가
26일 때 더 이상 가지 않고 Return -> 시간초과
count 대신 maxAlphaCount로 일일이 더하기 -> pypy로 겨우 통과
'''
maxAlphaCount = 0
alphaCount = 0

visitedNum = [0 for _ in range(26)]
visitedNum[boardInfo[0][0]] = 1


def backtracking(r, c):
    global visitedNum, boardInfo, maxAlphaCount, alphaCount
    alphaCount += 1
    maxAlphaCount = max(alphaCount, maxAlphaCount)

    if maxAlphaCount == 26:
        return

    dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]

    for i in range(4):
        nextR, nextC = r + dr[i], c + dc[i]

        if nextR < 0 or R <= nextR or nextC < 0 or C <= nextC:
            continue

        nextAlpha = boardInfo[nextR][nextC]

        if visitedNum[nextAlpha] == 1:
            continue

        if visitedNum[nextAlpha] == 0:
            visitedNum[nextAlpha] = 1

            backtracking(nextR, nextC)
            alphaCount -= 1

            visitedNum[nextAlpha] = 0


backtracking(0, 0)

print(maxAlphaCount)
