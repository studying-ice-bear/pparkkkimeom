import sys
input = sys.stdin.readline
N, M = map(int, input().split())

train = [[0] * 21 for _ in range(N+1)]

for _ in range(M):
    order = list(map(int, input().split()))
    if order[0] == 1:
        train[order[1]][order[2]] = 1
    elif order[0] == 2:
        train[order[1]][order[2]] = 0
    elif order[0] == 3:
        for i in range(20, 1, -1):
            train[order[1]][i] = train[order[1]][i - 1]
        train[order[1]][1] = 0
    elif order[0] == 4:
        for i in range(1, 21):
            train[order[1]][i-1] = train[order[1]][i]
        train[order[1]][20] = 0
        train[order[1]][0] = 0

cnt = 0
check = []
for i in range(1, N+1):
    if train[i] not in check:
        check.append(train[i])
        cnt += 1

print(cnt)
print(*train, sep="\n")
print()
print(*check, sep="\n")


'''
참조: https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-15787-%EA%B8%B0%EC%B0%A8%EA%B0%80-%EC%96%B4%EB%91%A0%EC%9D%84-%ED%97%A4%EC%B9%98%EA%B3%A0-%EC%9D%80%ED%95%98%EC%88%98%EB%A5%BC-%EA%B5%AC%ED%98%84

2 3
1 1 1
1 2 1
3 1

2 3
1 1 20
1 2 20
4 1

2 21
1 1 1
1 1 2
1 1 3
1 1 4
1 1 5
1 1 6
1 1 7
1 1 8
1 1 9
1 1 10
1 1 11
1 1 12
1 1 13
1 1 14
1 1 15
1 1 16
1 1 17
1 1 18
1 1 19
1 1 20
3 1

2 41
1 1 1
1 1 2
1 1 3
1 1 4
1 1 5
1 1 6
1 1 7
1 1 8
1 1 9
1 1 10
1 1 11
1 1 12
1 1 13
1 1 14
1 1 15
1 1 16
1 1 17
1 1 18
1 1 19
1 1 20
4 1
1 2 1
1 2 2
1 2 3
1 2 4
1 2 5
1 2 6
1 2 7
1 2 8
1 2 9
1 2 10
1 2 11
1 2 12
1 2 13
1 2 14
1 2 15
1 2 16
1 2 17
1 2 18
1 2 19
1 2 20
4 2
'''