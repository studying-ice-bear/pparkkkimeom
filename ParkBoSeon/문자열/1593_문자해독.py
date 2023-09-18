import sys
from collections import Counter
input = sys.stdin.readline

# answer = 0

# g, n = map(int, input().split())
# W = input().strip()
# S = input().strip()
# c = len(W)

# wHash = 0
# temp = 0

# for i in range(c):
#     wHash += hash(W[i])
#     temp += hash(S[i])

# if g == n:
#     if wHash == temp:
#         print(1)
#         exit()

# if temp == wHash:
#     answer += 1

# for i in range(c, n - c + 1):
#     temp -= hash(S[i - c])
#     temp += hash(S[i])
#     if temp == wHash:
#         answer += 1

# print(answer)


answer = 0

g, n = map(int, input().split())
W = input().strip()
S = input().strip()
wList = [0] * 58
sList = [0] * 58

for w in W:
    wList[ord(w) - 65] += 1
    
s, l = 0, 0

for i in range(n):
    sList[ord(S[i]) - 65] += 1
    l += 1
    
    if l == g:
        if sList == wList:
            answer += 1
        sList[ord(S[s]) - 65] -= 1
        s += 1
        l -= 1

print(answer)
        