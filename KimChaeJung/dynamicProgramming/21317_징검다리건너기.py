# https://www.acmicpc.net/problem/21317

# 40 ms
N = int(input())
stoneJumpList = [[0, 0]]
K = 0
for i in range(N):
    if i == N - 1:
        K = int(input())
        break
    small, big = map(int, input().split())
    stoneJumpList.append([small, big])


'''
DP[N] = min(DP[N-1] + SJL[N-1][0], DP[N-2] + SJL[N-2][1], DP[N-3] + K)
'''


def DPmemo():
    DPList = []
    for getKIdx in range(4, N+1):
        DP = [0, 0, stoneJumpList[1][0]]
        for dpIdx in range(3, N+1):
            value = min(DP[dpIdx - 1] + stoneJumpList[dpIdx - 1][0],
                        DP[dpIdx - 2] + stoneJumpList[dpIdx - 2][1])
            if getKIdx == dpIdx:
                value = min(value, DP[dpIdx - 3] + K)
            DP.append(value)
        DPList.append(DP)
    return DPList


def getSolution(DPList):
    if N == 1:
        print(0)
    elif N == 2:
        print(stoneJumpList[1][0])
    elif N == 3:
        print(min(stoneJumpList[1][0] +
              stoneJumpList[2][0], stoneJumpList[1][1]))
    else:
        answer = float('inf')

        for dpRow in DPList:
            answer = min(answer, dpRow[-1])

        print(answer)


DPList = DPmemo()
getSolution(DPList)
