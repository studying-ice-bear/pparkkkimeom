import sys
from collections import deque
input = sys.stdin.readline

def bfs(b, q):
    global answer
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    
    while q:
        t, x, y = q.popleft()
        if t > -1 and b[x][y] != 'F' and (x == 0 or y == 0 or x == r - 1 or y == c -1):
            answer = t + 1
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c and b[nx][ny] != '#':
                
                if t > - 1 and b[nx][ny] == '.':
                    b[nx][ny] = '_'
                    q.append([t + 1, nx, ny])
                
                elif t == -1 and b[nx][ny] != 'F':
                    b[nx][ny] = 'F'
                    q.append([-1, nx, ny])
                    
                
    

    
r, c = map(int, input().split())
board = []
answer = 'IMPOSSIBLE'
queue = deque([])

for i in range(r):
    board.append(list(input().strip()))
    
    for j in range(c):
        if board[i][j] == 'J':
            queue.append([0, i, j])

for i in range(r):
    for j in range(c):
        if board[i][j] == 'F':
            queue.append([-1, i, j])
    
bfs(board, queue)

print(answer)
