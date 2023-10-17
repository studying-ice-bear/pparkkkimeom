import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())

play = dict()
guitars = set()

for _ in range(N):
    g, m = input().strip().split(' ')
    guitars.add(g)

    tmp = ""
    for mm in m:
        if mm == 'Y':
            tmp += "1"
        else:
            tmp += "0"

    play[g] = int(tmp, 2)

max_cnt, max_guitar = 0, 0

play = list(play.items())
play.sort()

'''비트마스킹 활용'''
for i in range(1, N+1):
    for combs in combinations(play, i):
        two = 0
        for g, a in combs:
            two |= a

        cnt = 0
        for j in range(M):
            if two & (1 << j):
                cnt += 1

        if max_cnt < cnt:
            max_cnt = cnt
            max_guitar = i


if max_guitar != 0:
    print(max_guitar)
else:
    print(-1)



'''dfs로 구현한 조합을 사용하면 시간초과 남

visited = [False for _ in range(N)]
total_combinations = []

def comb(cnt, ii, arr):
    global max_cnt, max_guitar
    if cnt == ii:
        arr.sort()
        if arr not in total_combinations:
            two = 0
            for a in arr:
                two |= a[1]

            cnt = 0
            for j in range(M):
                if two & (1 << j):
                    cnt += 1

            if max_cnt < cnt:
                max_cnt = cnt
                max_guitar = ii

            total_combinations.append(arr.copy())
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(play[i])
            comb(cnt + 1, ii, arr)
            visited[i] = False
            arr.pop()


# for i in range(1, N+1):
#     comb(0, i, [])
'''

'''

초창기 구현에서도 combinations 사용하면 통과됨(56ms)
비트 마스킹을 사용하면 (4ms) 감소

from itertools import combinations
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
play = dict()

for _ in range(N):
    guitar, music = input().strip().split(' ')
    play[guitar] = []
    for i, m in zip(range(1, M+1), [m for m in music]):
        if m == 'Y':
            play[guitar].append(i)


visited = [False for _ in range(N)]
arr = list(play.items())


answer = {}
most_played = 0

for i in range(1, N+1):
    for combination in combinations(arr, i):
        guitars = set()
        played_music = set()

        for c in combination:
            guitars.add(c[0])
            for cc in c[1]:
                played_music.add(cc)

        if most_played < len(played_music):
            most_played = len(played_music)
            if most_played not in answer.keys():
                answer[most_played] = []

            answer[most_played].append(len(combination))
            # answer = min(answer, len(combination))

answer = sorted(answer.items(), key=lambda x: x[0], reverse=True)
if answer:
    print(answer[0][1][0])
else:
    print(-1)
'''