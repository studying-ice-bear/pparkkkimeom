import sys
input = sys.stdin.readline

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

answer = []

def div(x, y, N):
    c = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if c != paper[i][j]:
                div(x, y, N//2)
                div(x, y + N // 2, N//2)
                div(x + N//2, y, N//2)
                div(x + N//2, y + N//2, N//2)
                return
    if c == 0:
        answer.append(0)
    else:
        answer.append(1)

div(0, 0, n)
print(answer.count(0))
print(answer.count(1))