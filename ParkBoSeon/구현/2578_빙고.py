import sys
input = sys.stdin.readline

def DiagonalLCheck(v):
    l = [v[0][0], v[1][1], v[2][2], v[3][3], v[4][4]]
    
    if False in l:
        return False
    else:
        return True
    
def DiagonalRCheck(v):
    r = [v[0][4], v[1][3], v[2][2], v[3][1], v[4][0]]
    
    if False in r:
        return False
    else:
        return True

def RowCheck(v, x):
    if False in v[x]:
        return False

    return True

def ColCheck(v, y):
    temp = [v[0][y], v[1][y], v[2][y], v[3][y], v[4][y]]
    if False in temp:
        return False

    return True

bingo = dict()

for i in range(5):
    nums = list(map(int, input().split()))
    for j in range(5):
        bingo[nums[j]] = [i, j]

order = [list(map(int, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]

cnt = 0

d = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [0, 4], [1, 3], [2, 2], [3, 1], [4, 0]]

d_check=[]
r_check=[]
c_check=[]

digonalL = False
digonalR = False
row = False
col = False
bingo_cnt = 0
for i in range(5):
    for j in range(5):
        x, y = bingo[order[i][j]]
        visited[x][y] = True
        cnt += 1

        
        if 0 not in d_check:
            digonalL = DiagonalLCheck(visited)
        if 1 not in d_check:
            digonalR = DiagonalRCheck(visited)
        if x not in r_check:
            row = RowCheck(visited, x)
        if y not in c_check:
            col = ColCheck(visited, y)

        if digonalL:
            bingo_cnt += 1
            d_check.append(0)
            digonalL = False
        if digonalR:
            bingo_cnt += 1
            d_check.append(1)
            digonalR = False
        if row:
            bingo_cnt += 1
            r_check.append(x)
            row = False
        if col:
            bingo_cnt += 1
            c_check.append(y)
            col = False
        if bingo_cnt >= 3:
            print(cnt)
            exit()