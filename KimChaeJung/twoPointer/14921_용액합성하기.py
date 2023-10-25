# https://www.acmicpc.net/problem/14921
# 72ms
n = int(input())
A = list(map(int, input().split()))

start = 0
end = n - 1
answer = A[start] + A[end]
while start < end:
    currSum = A[start] + A[end]
    if abs(currSum) < abs(answer):
        answer = currSum

    if currSum > 0:
        end -= 1
    elif currSum < 0:
        start += 1
    else:
        break

print(answer)