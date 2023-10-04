N, K = map(int, input().split())
numbers = []
for _ in range(N):
    num = int(input())
    numbers.append(num)

numbers.sort()

start, end = numbers[0], numbers[-1]+K

answer = 0

while start <= end:
    mid = (start+end)//2

    total = 0
    for n in numbers:
        if n >= mid:
            break
        total += mid - n

    if total <= K:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
