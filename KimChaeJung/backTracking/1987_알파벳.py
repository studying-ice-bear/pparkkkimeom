# https://www.acmicpc.net/problem/1987
# 시간초과
import sys
input = sys.stdin.readline
R, C = map(int, input().split())

boardInfo = [[] for _ in range(R)]
for r in range(R):
    row = list(input().strip())

    def convertToNum(string):
        return ord(string)-65

    boardInfo[r] = list(map(convertToNum, row))

maxAlphaCount = 0

visitedNum = [0 for _ in range(26)]
visitedNum[boardInfo[0][0]] = 1


def backtracking(r, c):
    global visitedNum, boardInfo, maxAlphaCount

    maxAlphaCount = max(visitedNum.count(1), maxAlphaCount)

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

            visitedNum[nextAlpha] = 0


backtracking(0, 0)

print(maxAlphaCount)
