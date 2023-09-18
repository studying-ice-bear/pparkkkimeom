# https://www.acmicpc.net/problem/1593

# 5068 Ms
from collections import Counter

wLength, sLength = map(int, input().split())
w = input()
wCounter = Counter(w)
s = input()

answer = 0

sliced = s[0: wLength]
slicedCounter = Counter(sliced)

for idx in range(0, sLength - wLength + 1):
    if idx == 0:
        if slicedCounter == wCounter:
            answer += 1
    else:
        slicedCounter[s[idx+wLength-1]] += 1
        slicedCounter[s[idx-1]] -= 1
        if slicedCounter[s[idx-1]] == 0:
            del slicedCounter[s[idx-1]]
        if slicedCounter == wCounter:
            answer += 1


print(answer)
