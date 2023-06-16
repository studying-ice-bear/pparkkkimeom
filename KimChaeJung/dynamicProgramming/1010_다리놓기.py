# https://www.acmicpc.net/problem/1010

# 52ms

import sys
input = sys.stdin.readline

siteInfo = [[1 if m == n else 0 for m in range(31)] if n != 1 else [
    i for i in range(31)] for n in range(31)]

caseCount = int(input())


def memoSiteInfo(n, m):
    if siteInfo[n][m] == 0:
        result = 0
        for k in range(1, m-n+2):
            result += memoSiteInfo(n-1, (m-k))
        siteInfo[n][m] = result
    return siteInfo[n][m]


for _ in range(caseCount):
    n, m = map(int, input().split())
    memoSiteInfo(n, m)
    print(siteInfo[n][m])


'''
n, m
k (1, n-1)
(n-1, m-1 * 1) + (n-1, m-2 * 2) + , ... , + (n-1, m-k * k)
'''

# 44ms
# https://www.acmicpc.net/source/59844548
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    total = 1
    for j in range(N):
        total *= M-j
    for j in range(N):
        total //= j+1
    print(int(total))
