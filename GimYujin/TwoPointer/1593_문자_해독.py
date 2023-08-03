import sys
input = sys.stdin.readline
g, length = map(int, input().split())
W = input().strip()
S = input().strip()

letter = [0 for _ in range(58)]
word = [0 for _ in range(58)]

for w in W:
    letter[ord(w)-65] += 1

count = 0
start, end = 0, 0

for i in range(length):
    word[ord(S[i]) - 65] += 1
    end += 1

    if end == g:
        if letter == word:
            count += 1
        word[ord(S[start])-65] -= 1
        start += 1
        end -= 1

print(count)

'''
4 11
cAda
AbrAcadAbRa

2
Acad
cadA
'''