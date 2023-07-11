# https://www.acmicpc.net/problem/18111
# 반례 참고: https://www.acmicpc.net/board/view/104293
import sys
input = sys.stdin.readline


# row -col 순으로 가지 말고 팔 애들 먼저 다 파고 인벤토리 체크해야함

# pypy 680 ms
def solution():
    def flattenBlock(mapInfo, height, inventory):
        time = 0
        for row in mapInfo:
            # time += sum(list(map(lambda x: abs(x-height) if x <
            #             height else 2*abs(x-height), row)))
            # inventory += sum(list(map(lambda x: (x - height), row)))
            for cell in row:
                if cell < height:
                    time += (height - cell)
                    inventory -= (height - cell)
                elif cell > height:
                    time += 2 * (cell - height)
                    inventory += (cell - height)
        if inventory < 0:
            return [False, time]
        return [True, time]
    N, M, B = map(int, input().split())

    minHeight = 256
    maxHeight = 0

    targetHeight = -1
    targetTime = float('inf')

    blockMap = []

    for _ in range(N):
        blockRow = list(map(int, input().split()))
        minHeight = min(minHeight, min(blockRow))
        maxHeight = max(maxHeight, max(blockRow))
        blockMap.append(blockRow)
    for height in range(minHeight, maxHeight+1):
        possible, possibleTime = flattenBlock(blockMap, height, B)
        if possible:
            if targetTime >= possibleTime:
                targetTime = possibleTime
                targetHeight = height

    return (targetTime, targetHeight)

# python 112 ms


def solution2():
    N, M, B = map(int, input().split())

    heightList = [0 for _ in range(257)]
    minHeight = 256
    maxHeight = 0
    for _ in range(N):
        blockRow = list(map(int, input().split()))
        for cell in blockRow:
            heightList[cell] += 1
        minHeight = min(minHeight, min(blockRow))
        maxHeight = max(maxHeight, max(blockRow))

    targetHeight = -1
    targetTime = float('inf')

    for height in range(minHeight, maxHeight+1):
        time = 0
        inventory = B
        for i in range(minHeight, maxHeight+1):
            if i < height:
                time += (height - i) * heightList[i]
                inventory -= (height - i) * heightList[i]
            else:
                time += 2 * (i - height) * heightList[i]
                inventory += (i - height) * heightList[i]
        if inventory >= 0:
            if targetTime >= time:
                targetTime = time
                targetHeight = height

    return (targetTime, targetHeight)


# print(*solution())
print(*solution2())
