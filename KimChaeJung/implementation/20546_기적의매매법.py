# https://www.acmicpc.net/problem/20546
# 44ms
init = int(input())
stockList = list(map(int, input().split()))

def calBNPResult(init, stockList):
    currentMoney = init
    currentStock = 0
    for stock in stockList:
        if currentMoney >= stock:
            buyedStock, left = divmod(currentMoney, stock)
            currentMoney = left
            currentStock += buyedStock
    return currentMoney + stockList[-1] * currentStock

def cal33Result(init, stockList):
    currentMoney = init
    currentStock = 0
    isIncreseQueue = [0]
    isDecreaseQueue = [0]
    for idx in range(1, len(stockList)):
        if stockList[idx] > stockList[idx-1]:
            isIncreseQueue.append(idx)
            isDecreaseQueue = []
        if stockList[idx] < stockList[idx-1]:
            isDecreaseQueue.append(idx)
            isIncreseQueue = []
        if len(isDecreaseQueue) >= 3:
            if currentMoney > stockList[idx]:
                buyedStock, left = divmod(currentMoney, stockList[idx])
                currentMoney = left
                currentStock += buyedStock
        if len(isIncreseQueue) >= 3:
            currentMoney += currentStock * stockList[idx]
            currentStock = 0
    return currentMoney + stockList[-1] * currentStock

BNPResult = calBNPResult(init, stockList)
TIMINGResult = cal33Result(init, stockList)

if BNPResult > TIMINGResult:
    print('BNP')
elif BNPResult < TIMINGResult:
    print('TIMING')
else:
    print('SAMESAME')