N, M = map(int, input().split())
board = []
for i in range(N):
    s = input()
    tmp = []
    for j in range(M):
        if s[j] == 'B':
            tmp.append(1)
        else:
            tmp.append(0)
    board.append(tmp)

# 첫 째 칸이 'W'인 경우
new_w = [[0 for _ in range(8)] for _ in range(8)]
for i in range(8):
    if i % 2 == 0:
        for j in range(8):
            if j % 2 != 0:
                new_w[i][j] = 1
    else:
        for j in range(8):
            if j % 2 == 0:
                new_w[i][j] = 1

# 첫 째 칸이 'B'인 경우
new_b = [[0 for _ in range(8)] for _ in range(8)]
for i in range(8):
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0:
                new_b[i][j] = 1

    else:
        for j in range(8):
            if j % 2 != 0:
                new_b[i][j] = 1


w_ans = 0
b_ans = 0
if N != 8 and M != 8:
    for start in range(N-7):
        for end in range(M-7):
            print(start, end)
            for i in range(start, start+9):
                for j in range(end, end+9):
                    if board[i][j] != new_w[i-start][j-end]:
                        w_ans += 1
                    if board[i][j] != new_b[i-start][j-end]:
                        b_ans += 1
else:
    for i in range(N):
        for j in range(M):
            if board[i][j] != new_w[i][j]:
                w_ans += 1
            if board[i][j] != new_b[i][j]:
                b_ans += 1

answer = min(w_ans, b_ans)
print(answer)

'''
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]

[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
45
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
85
45

Process finished with exit code 0

'''