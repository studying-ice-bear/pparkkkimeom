import sys
input = sys.stdin.readline
R, C = map(int, input().split())
board = []
for _ in range(R):
    string = input().strip()
    board.append(list(s for s in string))

# graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

'''dfs 풀이, pypy로 통과

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
answer = 1
# bfs 풀이?(python3): https://fre2-dom.tistory.com/245
def bfs():
    global answer
    que = set([(0, 0, board[0][0])])

    while que:
        x, y, z = que.pop()
        answer = max(answer, len(z))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in z:
                que.add((nx, ny, board[nx][ny]+z))

    return answer


print(bfs())
