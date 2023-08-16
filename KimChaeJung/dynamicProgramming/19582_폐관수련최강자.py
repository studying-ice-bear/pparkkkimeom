# https://www.acmicpc.net/problem/19582

# 시간 초과
'''
import sys
input = sys.stdin.readline
N = int(input())

contest = []
for _ in range(N):
    x, p = map(int, input().split())
    contest.append([x, p])


DP = [0 for _ in range(N)]
notParticipateCount = [0 for _ in range(N)]

goToSleep = False

for (idx, [x, p]) in enumerate(contest):
    for nextIdx in range(idx+1, N):
        nextX, nextP = contest[nextIdx]
        if nextX >= DP[nextIdx] + p:
            DP[nextIdx] += p
        else:
            notParticipateCount[nextIdx] += 1
        if nextIdx == (N-1):
            if notParticipateCount[nextIdx] > 1:
                goToSleep = True
    if goToSleep:
        break


if goToSleep:
    if notParticipateCount.count(0) == N-1:
        goToSleep = False

if goToSleep:
    print('Zzz')
else:
    print('Kkeo-eok')
'''
# 248 ms
import sys
input = sys.stdin.readline
N = int(input())

answer = 'Kkeo-eok'

contest = []
perfectSum = [0]

for idx in range(N):
    x, p = map(int, input().split())
    contest.append([x, p])

    perfectSum.append(p + perfectSum[idx])

firstFailedContest = -1

for (idx, accum) in enumerate(perfectSum[:-1]):
    if accum > contest[idx][0]:
        firstFailedContest = idx
        break


secondFailed = False
if firstFailedContest != -1:
    for (idx, accum) in enumerate(perfectSum[:-1]):
        if idx > firstFailedContest:
            excluded = accum - contest[firstFailedContest][1]
            if excluded > contest[idx][0]:
                secondFailed = True
                break


if secondFailed:
    maxIdx, maxP = -1, float('-inf')
    for idx in range(firstFailedContest):
        x, p = contest[idx]
        if p > maxP:
            maxIdx = idx
            maxP = p
    for (idx, accum) in enumerate(perfectSum[:-1]):
        if idx >= maxIdx:
            excluded = accum - contest[maxIdx][1]
            if excluded > contest[idx][0]:
                answer = 'Zzz'
                break


print(answer)

'''

4
10000 6000
6000 2000
3000 3000
5000 10000
Kkeo-eok

4
10000 3000
6000 2000
3000 3001
5000 10000
Kkeo-eok

3
100 100
10 200
100 10
Kkeo-eok

1
1500 32000
Kkeo-eok

7
10000 2000
6000 1000
3000 2000
5000 10000
7000 2000
7000 3000
9000 500
Zzz

7
10000 6000
6000 20000
26000 3000
29000 1000
30000 2000
12000 4000
17000 2000
Kkeo-eok

3
10000 6000
6000 2000
1000 3000
Kkeo-eok

4
1500 4000
3000 1000
1000 2000
3000 4000
'''
