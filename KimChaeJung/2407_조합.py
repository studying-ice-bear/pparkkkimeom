# 52ms
import sys
input = sys.stdin.readline

siteInfo = [[1 if m == n else 0 for m in range(101)] if n != 1 else [i for i in range(101)] for n in range(101)]

def memoSiteInfo(n, m):
    if siteInfo[n][m] == 0:
        result = 0
        for k in range(1, m-n+2):
            result += memoSiteInfo(n-1, (m-k)) 
        siteInfo[n][m] = result
    return siteInfo[n][m]


n, m = map(int, input().split())
memoSiteInfo(m, n)
print(siteInfo[m][n])
