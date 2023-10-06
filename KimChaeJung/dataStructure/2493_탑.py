# https://www.acmicpc.net/problem/2493
# 928 ms
import sys
input = sys.stdin.readline
n = int(input())
towerList = list(map(int, input().split()))
answer = [0]
stack = [[0, towerList[0]]]
for i in range(1, n):
    noReceived = False
    curr = towerList[i]
    receivedTower = answer[-1]
    while True:
        if len(stack) == 0:
            answer.append(0)
            noReceived = True
            break
        if stack[-1][1] <= curr:
            stack.pop()
        else:
            receivedTower = stack[-1][0]
            break
    stack.append([i, towerList[i]])
    if not noReceived:
        answer.append((receivedTower + 1))

print(*answer)
