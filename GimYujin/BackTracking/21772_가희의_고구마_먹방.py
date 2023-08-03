R, C, T = map(int, input().split())
board = []

for i in range(R):
    board.append(list(s for s in input()))
    for j in range(C):
        if board[i][j] == 'G':
            start = (i, j)
            board[i][j] = '.'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_g = 0
goguma = 0
def dfs(x, y, cnt):
    global max_g, goguma
    if cnt == T:
        if max_g < goguma:
            max_g = goguma
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] == '.':
                dfs(nx, ny, cnt+1)
            elif board[nx][ny] == 'S':
                goguma += 1
                board[nx][ny] = '.'
                dfs(nx, ny, cnt+1)
                goguma -= 1
                board[nx][ny] = 'S'


dfs(start[0], start[1], 0)
print(max_g)

'''
5 5 10
##S##
##S##
SSG##
##S##
##S##
6
'''