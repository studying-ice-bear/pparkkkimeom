# https://www.acmicpc.net/problem/14430

# 116ms

N, M = map(int, input().split())
area = []
summedArea = []
for i in range(N):
    row = list(map(int, input().split()))
    if i == 0:
        firstRowValue = 0
        for idx in range(M):
            firstRowValue += row[idx]
            row[idx] = firstRowValue
    summedArea.append(row)

for row in range(1, N):
    newSummedRow = []
    for idx in range(M):
        prevRowValue = summedArea[row-1][idx]
        currentValue = summedArea[row][idx]
        if idx == 0:
            newSummedRow.append(
                prevRowValue+currentValue)
        else:
            prevValue = newSummedRow[idx-1]
            newSummedRow.append(
                max(prevRowValue, prevValue)+currentValue)
    summedArea[row] = newSummedRow

print(summedArea[N-1][M-1])
