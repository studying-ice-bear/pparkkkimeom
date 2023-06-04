import copy
N, K = map(int, input().split())
S = [0] + list(map(int, input().split()))
D = [0] + list(map(int, input().split()))
P = [0] * (N + 1)

for k in range(K):
    for i in range(1, N+1):
        P[D[i]] = S[i]
    S = copy.copy(P)

print(*S[1:], sep=" ")

'''
Di는 P(Di)값을 i번째로 가지고 온다.

# 0
5 1
4 3 1 2 5
-> 1 4 5 3 2


# 1
D: 4 3 1 2 5
P: 1 4 5 3 2
-> 3 5 1 4 2

'''