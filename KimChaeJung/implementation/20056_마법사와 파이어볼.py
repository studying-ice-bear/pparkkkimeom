# https://www.acmicpc.net/problem/20056
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

# [m, s, d]
boardInfo = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    boardInfo[r-1][c-1].append([m, s, d])

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def move(board):
    global dr, dc
    boardSize = len(board)
    newBoard = [[[] for _ in range(boardSize)] for _ in range(boardSize)]
    fireballCount = 0
    iterateDone = False
    for r in range(boardSize):
        if iterateDone:
            break
        for c in range(boardSize):
            if fireballCount == M:
                iterateDone = True
                break
            if len(board[r][c]) == 0:
                continue
            for singleFireball in board[r][c]:
                m, s, d = singleFireball
                # 6, 1 => 9, -2
                # tobe => 1, 5
                # now => 1, 0
                nextR, nextC = r + s*dr[d], c + s*dc[d]
                if nextR < 0:
                    nextR = boardSize - (abs(nextR) % boardSize)
                if nextC < 0:
                    nextC = boardSize - (abs(nextC) % boardSize)
                if boardSize <= nextR:
                    nextR = nextR % boardSize
                if boardSize <= nextC:
                    nextC = nextC % boardSize
                newBoard[nextR][nextC].append([m, s, d])
    return newBoard


'''
파이어볼은 4개의 파이어볼로 나누어진다.
나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
질량이 0인 파이어볼은 소멸되어 없어진다.
'''


def merge(board):
    boardSize = len(board)
    newBoard = [[[] for _ in range(boardSize)] for _ in range(boardSize)]
    for r in range(boardSize):
        for c in range(boardSize):
            fireballCount = len(board[r][c])
            if fireballCount < 2:
                newBoard[r][c] = board[r][c]
                continue
            mass = 0
            speed = 0
            directionCount = 0
            for singleFireball in board[r][c]:
                m, s, d = singleFireball
                mass += m
                speed += s
                directionCount += 0 if d % 2 == 1 else 1
            mass = mass // 5
            if mass == 0:
                continue
            speed = speed // fireballCount
            direction = [0, 2, 4, 6] if directionCount in [
                0, fireballCount] else [1, 3, 5, 7]
            for newDir in direction:
                newBoard[r][c].append([mass, speed, newDir])
    return newBoard


def getMass(board):
    totalMass = 0
    boardSize = len(board)
    for r in range(boardSize):
        for c in range(boardSize):
            if board[r][c] == []:
                continue
            for singleFireball in board[r][c]:
                totalMass += singleFireball[0]
    return totalMass


for _ in range(K):
    boardInfo = move(boardInfo)
    boardInfo = merge(boardInfo)


print(getMass(boardInfo))
