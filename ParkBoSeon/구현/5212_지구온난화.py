import sys
input = sys.stdin.readline


r, c = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

islands = []
temp = []

for i in range(r):
    l = list(input().strip())
    
    islands.append(l[:])
    temp.append(l[:])

for i in range(r):
    for j in range(c):
        cnt = 0
        if temp[i][j] == 'X':
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                
                if 0 <= nx < r and 0 <= ny < c:
                    if temp[nx][ny] == '.':
                        cnt += 1
                
                if cnt >= 3:
                    islands[i][j] = '.'
                    break

x = 0
y = 0

for i in range(r):
    if 'X' in islands[i]:
        x = i
        break

for i in range(c):

for i in range(r):
    print(islands[i])
    

    