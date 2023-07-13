# https://www.acmicpc.net/problem/17070

N = int(input())

houseInfo = []
for _ in range(N):
    row = list(map(int, input().split()))
    houseInfo.append(row)

# from hori, from verti, from diagonal
DP = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
DP[0][1] = [1, 0, 0]
'''
DP[0][2] = [1, 0, 0]
DP[1][2] = [0, 0, 1]
'''
'''
curR, curC
가로
prevR = curR, prevC = curC -1 
1) nextR = curR, nextC = curC + 1
2) nextR = curR + 1, nextC = curC + 1
    if (curR + 1, curC), (curR, curC + 1) not wall
세로
prevR = curR - 1, prevC = curC
1) nextR = curR + 1, nextC = curC
2) nextR = curR + 1, nextC = curC + 1
    if (curR + 1, curC), (curR, curC + 1) not wall
대각선
prevR = curR -1, prevC = curC - 1
1) nextR = curR, nextC = curC + 1
2) nextR = curR + 1, nextC = curC
3) nextR = curR + 1, nextC = curC + 1
    if (curR + 1, curC), (curR, curC + 1) not wall
'''

for r in range(N):
    for c in range(N):
        if r == 0 and c == 0:
            continue
        curSpot = houseInfo[r][c]
        if curSpot == 1:
            continue
        horiNextR, horiNextC = r, c + 1
        vertiNextR, vertiNextC = r + 1, c
        diagNextR, diagNextC = r + 1, c + 1
        if r == 1 or r == 2 or c == 2 or c == 3:
            print(r, c, '-------------------')
        # 가로
        horiPrevR, horiPrevC = r, c - 1
        if 0 <= horiPrevR and horiPrevR < N and 0 <= horiPrevC and horiPrevR < N:
            horiDP = sum(DP[horiPrevR][horiPrevC])
            if horiPrevR == 0 and horiPrevC == 0:
                horiDP += 1
            print('hori', horiDP)
            if horiNextC < N and houseInfo[horiNextR][horiNextC] != 1:
                DP[horiNextR][horiNextC][0] += horiDP
                if diagNextR < N:
                    if houseInfo[r + 1][c] != 1 and houseInfo[r][c + 1] != 1:
                        DP[diagNextR][diagNextC][2] += horiDP
        # 세로
        vertiPrevR, vertiPrevC = r - 1, c
        if 0 <= vertiPrevR and vertiPrevR < N and 0 <= vertiPrevC and vertiPrevC < N:
            if DP[vertiPrevR][vertiPrevC][1] != 0 or DP[vertiPrevR][vertiPrevC][2] != 0:
                vertiDP = sum(DP[vertiPrevR][vertiPrevC])
                print('verti', vertiDP)
                if vertiNextR < N and houseInfo[vertiNextR][vertiNextC] != 1:
                    DP[vertiNextR][vertiNextC][1] += vertiDP
                    if diagNextC < N:
                        if houseInfo[r + 1][c] != 1 and houseInfo[r][c + 1] != 1:
                            DP[diagNextR][diagNextC][2] += vertiDP
        # 대각선
        diagPrevR, diagPrevC = r - 1, c - 1
        if 0 <= diagPrevR and diagPrevR < N and 0 <= diagPrevC and diagPrevC < N:

            diagDP = sum(DP[diagPrevR][diagPrevC])
            print('diag', diagDP)
            if diagNextC < N and houseInfo[diagNextR][diagNextC] != 1:
                DP[horiNextR][horiNextC][0] += diagDP
                if diagNextR < N:
                    DP[vertiNextR][vertiNextC][1] += diagDP
                    if houseInfo[r + 1][c] != 1 and houseInfo[r][c + 1] != 1:
                        DP[diagNextR][diagNextC][2] += diagDP
        if r == 1 or r == 2 or c == 2 or c == 3:
            print(r, c, '-------------------')
for row in DP:
    print(row)
print(DP[r][c])
