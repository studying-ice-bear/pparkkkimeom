# https://www.acmicpc.net/problem/1323
N, K = map(int, input().split())


def isOutOfDoveHouse(n, k):
    dividable = False
    doveHouse = [0 for _ in range(k)]
    count = 1
    curLeft = n % k
    while True:
        if curLeft == 0:
            dividable = True
            break
        if doveHouse[curLeft] == 1:
            break
        doveHouse[curLeft] = 1
        curLeft = (curLeft*(10**len(str(n))) + n) % k
        count += 1
    return dividable, count


if N % K == 0:
    print(1)
elif N % 2 == 1 and K % 2 == 0:
    print(-1)
else:
    dividable, count = isOutOfDoveHouse(N, K)
    if dividable:
        print(count)
    else:
        print(-1)
