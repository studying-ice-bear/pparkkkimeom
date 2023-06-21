# https://www.acmicpc.net/problem/2302

# 48ms

N = int(input())
M = int(input())

VIP = []

for _ in range(M):
    VIP.append(int(input()))

movableList = []


def fibo(dpList, until):
    while True:
        if len(dpList) > until:
            break
        dpList.append(dpList[len(dpList)-1]+dpList[len(dpList)-2])


movableDP = [1, 1, 2, 3]
wayCount = 1

if len(VIP) == 0:
    fibo(movableDP, N)
    print(movableDP[N])
    exit()
elif len(VIP) == N:
    print(1)
    exit()
else:
    for i in range(M+1):
        if M == 0:
            break
        if i == 0:
            movableList.append(VIP[i]-1)
            continue
        if i == M:
            movableList.append(N-VIP[i-1])
            continue
        movableList.append(VIP[i]-VIP[i-1]-1)
    for group in movableList:
        fibo(movableDP, group)
        wayCount *= movableDP[group]
    print(wayCount)
