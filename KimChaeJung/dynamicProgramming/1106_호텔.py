# https://www.acmicpc.net/problem/1106

def wrong():
    minCustomer, cityCount = map(int, input().split())

    costList = [0 for _ in range(1101)]
    for _ in range(cityCount):
        cost, customer = map(int, input().split())
        costList[cost] = max(costList[cost], customer)

    DP = [0 for _ in range(1101)]

    for i in range(1, minCustomer + 1):
        maxCustomer = costList[i]
        for j in range(1, i):
            if DP[j] != 0 and DP[i-j] != 0:
                maxCustomer = max(maxCustomer, DP[j]+DP[i-j])
        DP[i] = maxCustomer

    print(DP[:100])
    for idx in range(len(DP)):
        if DP[idx] >= minCustomer:
            print(idx)
            break

# 204 ms


def solution():
    C, N = map(int, input().split())
    # 안됨
    # DP = [float('inf') for _ in range(1001)]
    # 됨
    DP = [float('inf') for _ in range(1101)]
    # [참고](https://www.acmicpc.net/board/view/107696)

    for _ in range(N):
        cost, customer = map(int, input().split())
        DP[customer] = min(DP[customer], cost)

    for i in range(1, len(DP)):
        for j in range(i):
            DP[i] = min(DP[i], DP[j] + DP[i-j])

    return min(DP[C:])


print(solution())
