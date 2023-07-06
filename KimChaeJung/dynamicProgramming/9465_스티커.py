# https://www.acmicpc.net/problem/9465

import sys
input = sys.stdin.readline

TC = int(input())

# 틀렸습니다
'''
def DP(info):
    answer = 0
    # Pn = [P(n-1)+ 마지막과 떨어진 것], [P(n-2)+마지막과 떨어지지 않은 것]
    Pn = [0 for _ in range(len(info[0]))]
    # 0: lower, 1: upper, 2: same, 3: pass
    PnPoint = [-1 for _ in range(len(info[0]))]

    for idx in range(len(info[0])):
        upperNumber = info[0][idx]
        lowerNumber = info[1][idx]
        secondFlag = 2
        if upperNumber > lowerNumber:
            secondFlag = 0
        elif upperNumber < lowerNumber:
            secondFlag = 1

        case01 = []
        if 0 <= idx - 1:
            prevSecondFlag = PnPoint[idx-1]
            if prevSecondFlag == 3 and secondFlag == 2:
                Pn[idx] = Pn[idx-1] + upperNumber
                PnPoint[idx] = secondFlag
                continue
            if secondFlag == 2:
                case01 = [Pn[idx-1]+upperNumber, 1-prevSecondFlag]
            elif prevSecondFlag + secondFlag == 1:
                case01 = [Pn[idx-1]+max(upperNumber, lowerNumber), secondFlag]
            else:
                case01 = [Pn[idx-1] +
                          min(upperNumber, lowerNumber), 1-secondFlag]

        case02 = []
        if 0 <= idx - 2:
            case02 = [Pn[idx-2]+max(upperNumber, lowerNumber), secondFlag]

        if len(case01) == 0:
            Pn[idx] = max(upperNumber, lowerNumber)
            PnPoint[idx] = secondFlag
            continue

        if len(case02) == 0:
            Pn[idx] = case01[0]
            PnPoint[idx] = case01[1]
            continue

        if case01[0] > case02[0]:
            Pn[idx] = case01[0]
            PnPoint[idx] = case01[1]
        else:
            PnPoint[idx-1] = 3
            Pn[idx] = case02[0]
            PnPoint[idx] = case02[1]
        # print(Pn)
        # print(PnPoint)
    answer = Pn[-1]
    if 3 in PnPoint:
        startWithUpper = 0
        startWithLower = 0
        for idx in range(len(info[0])):
            if idx % 2 == 0:
                startWithUpper += info[0][idx]
                startWithLower += info[1][idx]
            else:
                startWithUpper += info[1][idx]
                startWithLower += info[0][idx]
        answer = max(answer, startWithUpper, startWithLower)

    return answer
'''
# 틀렸습니다
'''
def DP(info, col):
    # P(n) = max(P(n-1) + K(n)_n-1과 반대편 것, P(n-2) + K(n)_n-1과 같은편 것
    P = [0 for _ in range(col)]
    K = [-1 for _ in range(col)]

    for idx in range(col):
        upperVal = info[0][idx]
        lowerVal = info[1][idx]
        sizeFlag = 2
        if upperVal > lowerVal:
            sizeFlag = 0
        elif upperVal < lowerVal:
            sizeFlag = 1

        if idx == 0:
            P[idx] = max(info[0][idx], info[1][idx])
            K[idx] = sizeFlag
            continue
        if idx == 1:
            down = info[0][0] + info[1][1]
            up = info[1][0] + info[0][1]
            if down == up:
                P[idx] = down
                K[idx] = 2
                continue
            else:
                if K[0] + sizeFlag == 1 or K[0] == 2:
                    P[idx] = P[0] + max(info[0][idx], info[1][idx])
                    K[idx] = sizeFlag
                else:
                    P[idx] = P[0] + info[1-K[0]][idx]
                    K[idx] = 1-K[0]
                continue

        infoIdx = K[idx-1]
        first, second = 0, 0

        if infoIdx == 2:
            if sizeFlag == 2:
                first = P[idx-1] + info[0][idx]
                second = P[idx-2] + info[0][idx]
            else:
                first = P[idx-1] + info[sizeFlag][idx]
                second = P[idx-2] + info[sizeFlag][idx]
        else:
            first = P[idx-1] + info[1 - infoIdx][idx]
            if K[idx-2] == infoIdx:
                second = P[idx-2] + info[1-infoIdx][idx-1] + info[infoIdx][idx]
            else:
                second = P[idx-2] + info[infoIdx][idx]

        if first == second:
            P[idx] = first
            K[idx] = 2
        else:
            if infoIdx + sizeFlag == 1 or infoIdx == 2:
                P[idx] = max(first, second)
                K[idx] = sizeFlag
            else:
                if first > second:
                    P[idx] = first
                    K[idx] = 1 - infoIdx
                else:
                    P[idx] = second
                    K[idx] = infoIdx

            # if first > second:
            #     P[idx] = first
            #     K[idx] = 1 - infoIdx
            # elif first < second:
            #     P[idx] = second
            #     K[idx] = infoIdx

        # print(P)
        # print(K)

    return P[-1]
'''

# 764 ms


def DP(info, col):
    P = [[0 for _ in range(col)], [0 for _ in range(col)]]
    for idx in range(col):
        if idx == 0:
            P[0][idx] = info[0][idx]
            P[1][idx] = info[1][idx]
            continue
        if idx == 1:
            P[0][idx] = P[1][0] + info[0][idx]
            P[1][idx] = P[0][0] + info[1][idx]
            continue

        zero_not_jump = P[1][idx-1] + info[0][idx]
        zero_jump = P[1][idx-2] + info[0][idx]
        one_not_jump = P[0][idx-1] + info[1][idx]
        one_jump = P[0][idx-2] + info[1][idx]
        P[0][idx] = max(zero_not_jump, zero_jump)
        P[1][idx] = max(one_not_jump, one_jump)

    return max(P[0][-1], P[1][-1])


def withoutDP(info, col):
    startWithUpper = 0
    startWithLower = 0
    swUIdx = 0
    swLIdx = 1
    for idx in range(col):
        startWithUpper += info[swUIdx][idx]
        startWithLower += info[swLIdx][idx]
        swUIdx = 1 - swUIdx
        swLIdx = 1 - swLIdx
    return max(startWithUpper, startWithLower)


for _ in range(TC):
    col = int(input())
    upperSticker = list(map(int, input().split()))
    lowerSticker = list(map(int, input().split()))
    stickerInfo = [upperSticker, lowerSticker]
    DPVal = DP(stickerInfo, col)
    notDPVal = withoutDP(stickerInfo, col)
    print(max(DPVal, notDPVal))
