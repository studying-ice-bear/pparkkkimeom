# https://www.acmicpc.net/problem/15787

# 228ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

passengerInfo = ['0b0' for _ in range(N)]

# 20개 좌석 처리
for _ in range(M):
    order = list(map(int, input().split()))
    type = order[0]
    train = order[1]
    targetTrain = passengerInfo[train-1]
    if type == 1:
        seat = order[2]
        passengerInfo[train-1] = bin(int(targetTrain, 2) | 2**(seat-1))
    elif type == 2:
        seat = order[2]
        passengerInfo[train-1] = bin(int(targetTrain, 2) & ~2**(seat-1))
    elif type == 3:
        movedSeat = bin(int(targetTrain, 2) << 1)
        if len(movedSeat) > 22:
            movedSeat = movedSeat[:2]+movedSeat[-20:]
        passengerInfo[train-1] = bin(int(movedSeat, 2))
    else:
        passengerInfo[train-1] = bin(int(targetTrain, 2) >> 1)

passableTrain = set(passengerInfo)
print(len(passableTrain))
