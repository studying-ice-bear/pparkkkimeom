N = int(input())
A = list(map(int, input().split()))

start, end = 0, N-1
diff = A[start] + A[end]

while start < end:
    total = A[start] + A[end]

    if abs(total) < abs(diff):
        diff = total

    if total < 0:
        start += 1
    else:
        end -= 1

print(diff)
