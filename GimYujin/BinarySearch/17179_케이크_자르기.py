
N, M, L = map(int, input().split())

canCut = [int(input()) for _ in range(M)] + [L]

for _ in range(N):
    x = int(input())
    cake = [0 for _ in range(x)]

    start, end = 1, L
    answer = 0

    while start <= end:
        mid = (start+end) // 2

        cnt = 0
        left = 0
        for right in canCut:
            if right - left >= mid:
                left = right
                cnt += 1

        if cnt <= x:
            end = mid - 1
        else:
            start = mid + 1
            answer = max(answer, mid)

    print(answer)


'''
[10, 10, 15, 20, 5, 10]

[5, 10, 10, 10, 15, 20]

3
start = 5
end = 70 // 3 = 23

'''