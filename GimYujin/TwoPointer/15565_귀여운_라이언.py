N, K = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
answer = 1000001
cnt = 0

for start in range(N):
    while end < N:
        if cnt == K:
            break

        if arr[end] == 1:
            cnt += 1

        end += 1

    if cnt == K and answer > end - start:
        answer = end - start

    if arr[start] == 1:
        cnt -= 1

if answer == 1000001:
    print(-1)
else:
    print(answer)

'''
10 3
1 2 2 2 1 2 1 2 2 1
6

5 2
1 1 2 2 1
2

10 3
1 1 1 2 1 2 1 2 2 1
3

반례
10 2
2 2 2 1 1 2 2 2 2 2
2
'''
