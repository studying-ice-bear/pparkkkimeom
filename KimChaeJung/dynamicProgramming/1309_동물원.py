# https://www.acmicpc.net/problem/1309
# 92 ms
N = int(input())

'''
P(n)
0 = 3 (1, 1, 1)   (2, 1)
1 =   (*2, *2, *3) (2*2, 1*3) -> (2+1*2, 3)
(a, b) -> (a+2*b,a+b)
'''


def DP(N):
    P = [[2, 1]]
    for _ in range(1, N):
        a, b = P[-1]
        nextA, nextB = (a + 2*b) % 9901, (a+b) % 9901
        P.append([nextA, nextB])
    return sum(P[-1]) % 9901


print(DP(N))
