# https://www.acmicpc.net/problem/2467
# 140ms
n = int(input())
A = list(map(int, input().split()))

start = 0
end = n - 1
value = A[start] + A[end]
answer = [A[start], A[end]]
while start < end:
    currSum = A[start] + A[end]
    if abs(currSum) < abs(sum(answer)):
        value = currSum
        answer[0] = A[start]
        answer[1] = A[end]

    if currSum > 0:
        end -= 1
    elif currSum < 0:
        start += 1
    else:
        break

print(*answer)