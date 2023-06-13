import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().strip()

cursor, count, result = 0, 0, 0

while cursor < (M - 1):
    if S[cursor:cursor + 3] == 'IOI':
        count += 1
        cursor += 2
        if count == N:
            result += 1
            count -= 1
    else:
        cursor += 1
        count = 0

print(result)
# P = 'IOI'
# for _ in range(N-1):
#     P += 'OI'
#
# cnt = 0
# for i in range(M-len(P)+1):
#     if S[i:i+3] == 'IOI':
#         flag = True
#         for j in range(3, len(P)):
#             if P[j] != S[i+j]:
#                 flag = False
#                 break
#
#         if flag:
#             cnt += 1
# print(cnt)
'''
참조: https://wayhome25.github.io/python/2017/06/14/time-complexity/
Slice의 시간복잡도
	l[a:b]  ->   O(b-a)	
    l[:] : O(len(l)-0) = O(N)
'''