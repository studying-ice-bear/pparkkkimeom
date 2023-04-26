# 시간 초과 - 완전 탐색
import sys
input = sys.stdin.readline

N, sumCount = map(int, input().split())

cellList = []
for _ in range(N):
    rowList = list(map(int, input().split()))
    cellList.append(rowList)

dotList = []
for _ in range(sumCount):
    x1, y1, x2, y2 = map(int, input().split())
    dotList.append([(x1, y1), (x2, y2)])

for firstDot, secondDot in dotList:
    x1, y1 = firstDot
    x2, y2 = secondDot
    sum = 0
    for rowIdx in range(N):
        if x1-1 <= rowIdx and x2-1 >= rowIdx:
            for colIdx in range(N):
                if y1-1 <= colIdx and y2-1 >= colIdx:
                    sum += cellList[rowIdx][colIdx]
    print(sum)


# 시간 초과
import sys
input = sys.stdin.readline

N, sumCount = map(int, input().split())

cellList = []
for _ in range(N):
    sumSum = 0
    rowList = list(map(int, input().split()))
    sumSumList = []
    for num in rowList:
        sumSum += num
        sumSumList.append(sumSum)
    cellList.append(sumSumList)

dotList = []
for _ in range(sumCount):
    x1, y1, x2, y2 = map(int, input().split())
    dotList.append([(x1, y1), (x2, y2)])

for firstDot, secondDot in dotList:
    x1, y1 = firstDot
    x2, y2 = secondDot
    sum = 0
    for rowIdx in range(x1-1, x2):
        if y1 == 1:
            sum += cellList[rowIdx][y2-1]
        else:
            sum += cellList[rowIdx][y2-1] - cellList[rowIdx][y1-2]
        
    print(sum)

