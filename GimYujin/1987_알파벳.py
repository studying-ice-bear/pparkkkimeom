import sys
input = sys.stdin.readline
R, C = map(int, input().split())
board = []
for _ in range(R):
    string = input()
    board.append(list(s for s in string))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = 0
max_answer = 0
alphabet = [False for _ in range(26)]   # 65: A


def dfs(x, y):
    global answer, max_answer
    alphabet[ord(board[x][y])-65] = True
    answer += 1
    max_answer = max(max_answer, answer)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            j = ord(board[nx][ny]) - 65
            if not alphabet[j]:
                dfs(nx, ny)
                alphabet[j] = False
                answer -= 1


dfs(0, 0)
print(max_answer)

'''
from collections import deque

def bfs(start):
    que = deque()
    que.append(start)
    alphabet = [False for _ in range(26)]   # 65: A
    alphabet[ord(board[start[0]][start[1]])-65] = True
    visited = [[0 for _ in range(C)] for _ in range(R)]
    answer = 0

    while que:
        x, y, z = que.popleft()
        answer += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                j = ord(board[nx][ny]) - 65
                if not alphabet[j]:
                    alphabet[j] = True
                    que.append((nx, ny))

    return answer


print(bfs((0, 0)))
'''