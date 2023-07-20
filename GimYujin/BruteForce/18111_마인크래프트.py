'''
참고: https://codecollector.tistory.com/678

건물을 쌓으려면 내가 블록을 뺀 것과 가지고있는 블록이 쌓아야하는 건물의 높이보다 커야 가능하다.
remove: 내가 블록을 뺀 것
B: 가지고 있는 블록의 수
build: 쌓아야 하는 블록의 수

if B + remove - build >= 0:
'''
import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

time = sys.maxsize
height = 0

for h in range(257):
    remove = 0
    build = 0
    for i in range(N):
        for j in range(M):
            if h <= board[i][j]:
                remove += board[i][j] - h
            else:
                build += h - board[i][j]

    if B + remove - build >= 0:
        tmp = (2 * remove) + build

        if tmp <= time:
            time = tmp
            height = h

print(time, height)
