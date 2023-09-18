from itertools import combinations

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
for i in range(N):
    for c in combinations(numbers, i+1):
        if sum(c) == S:
            cnt += 1

print(cnt)

'''
N: 정수의 개수
1 <= N <= 20

반례:
5 1
1 0 1 0 1
'''