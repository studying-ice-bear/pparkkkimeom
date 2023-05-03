# https://www.acmicpc.net/problem/2578
# 40ms
chulsuTable = [list(map(int, input().split())) for _ in range(5)]
bingoCountTable = [[0]*5, [0]*5, [0]*2]
targetTable = []

def countBingo(x, y):
    bingoCountTable[0][x] += 1
    bingoCountTable[1][y] += 1
    if x == y:
        bingoCountTable[2][0] += 1
    if x+y == 4:
        bingoCountTable[2][1] += 1

def isBingoComplete(table):
    bingoCount = 0
    for row in table:
        bingoCount += row.count(5)
    if bingoCount >= 3:
        return True
    return False

def findIdx(writtenTable, targetNum):
    for rowIdx in range(5):
        for colIdx in range(5):
            if writtenTable[rowIdx][colIdx] == targetNum:
                return (rowIdx, colIdx)

for _ in range(5):
    targetNums = list(map(int, input().split()))
    targetTable.extend(targetNums)

for idx in range(len(targetTable)):
    x, y = findIdx(chulsuTable, targetTable[idx])
    countBingo(x, y)
    if isBingoComplete(bingoCountTable):
        print(idx + 1)
        break


# print(chulsuTable)
# print(targetTable)