# https://www.acmicpc.net/problem/17070
# 44 ms
N = int(input())

houseInfo = []
for _ in range(N):
    row = list(map(int, input().split()))
    houseInfo.append(row)

# 초기 아이디어
'''
각 탐색 점 별로 이전 (가로, 세로, 대각선)을 바탕으로 다음 (가로, 세로, 대각선)을 메모이제이션 한다
문제점: 이전 것을 참고한 뒤에 다음 것을 건드리려 하니 관리 포인트가 너무 많았음
'''

# 단방향 그래프 만드려고 한 시도
'''
문제점: 어차피 이것도 탐색하면서 다시 (가로, 세로, 대각선) 방향으로부터 온 갯수를 세야함
'''


def makeGraph():
    pipeInfo = [[[] for _ in range(N)] for _ in range(N)]
    pipeInfo[0][0].append((0, 1))

    for row in range(N):
        for col in range(1, N):

            # 대각선으로 가기
            diagSpace = [(row, col+1), (row + 1, col), (row + 1, col + 1)]
            if N > row + 1 and N > col + 1:
                hasWall = False
                for space in diagSpace:
                    if houseInfo[space[0]][space[1]] == 1:
                        hasWall = True
                        break
                if not hasWall:
                    prevDiagSpace = [
                        (row - 1, col), (row, col - 1), (row - 1, col - 1)]
                    if 0 <= row - 1 or 0 <= col - 1:
                        hasPrev = False
                        for space in prevDiagSpace:
                            if (row, col) in pipeInfo[space[0]][space[1]]:
                                hasPrev = True
                                break
                        if hasPrev:
                            pipeInfo[row][col].append((row + 1, col + 1))
            # 가로로 가기
            if N > col + 1 and col - 1 >= 0:
                if houseInfo[row][col + 1] != 1:
                    if (row, col) in pipeInfo[row][col - 1] or ((row, col) in pipeInfo[row - 1][col - 1] if row > 0 else False):
                        pipeInfo[row][col].append((row, col + 1))
            # 세로로 가기
            if N > row + 1 and row - 1 >= 0:
                if houseInfo[row+1][col] != 1:
                    if (row, col) in pipeInfo[row - 1][col] or ((row, col) in pipeInfo[row - 1][col - 1] if col > 0 else False):
                        pipeInfo[row][col].append((row + 1, col))

    for row in pipeInfo:
        print(*row)


def solution(N, house):
    DP = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
    # from hori, from verti, from diagonal
    DP[0][1] = [1, 0, 0]
    for r in range(N):
        for c in range(1, N):
            curSpot = houseInfo[r][c]
            if curSpot == 1:
                continue
            horiPrevR, horiPrevC = r, c - 1
            if 0 <= horiPrevC:
                horiDP = DP[horiPrevR][horiPrevC][0] + \
                    DP[horiPrevR][horiPrevC][2]
                DP[r][c][0] += horiDP

            vertiPrevR, vertiPrevC = r - 1, c
            if 0 <= vertiPrevR:
                vertiDP = DP[vertiPrevR][vertiPrevC][1] + \
                    DP[vertiPrevR][vertiPrevC][2]
                DP[r][c][1] += vertiDP

            diagPrevR, diagPrevC = r - 1, c - 1
            if 0 <= diagPrevR and 0 <= diagPrevC:
                if houseInfo[horiPrevR][horiPrevC] != 1 and houseInfo[vertiPrevR][vertiPrevC] != 1:
                    diagDP = sum(DP[diagPrevR][diagPrevC])
                    DP[r][c][2] += diagDP

    return sum(DP[N-1][N-1])


print(solution(N, houseInfo))
