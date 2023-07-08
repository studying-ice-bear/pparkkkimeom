'''
첫 번째 틀린 이유
fireball에 넣는 게 반복되는데 이전에는 i를 그대로 넣어주고,
다음 턴에선 i-1을 넣어주었다.

두 번째 틀린 이유
홀수로만 이루어진 경우와 짝수로만 이루어진 경우에 대해 합을 구해서 해당 합이 짝수인지 홀수인지에 따라
파이어볼 방향을 나누어주었는데
해당 명제는 두 가지 수일 때 참이다.

짝+홀+홀+짝 도 짝수다..
https://www.acmicpc.net/board/view/103292
'''

# N: 보드 크기, M: 파이어볼 개수, K:
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]

fireball = []
for _ in range(M):
    # fireball.append(list(map(int, input().split())))
    tmp = list(map(int, input().split()))
    fireball.append([tmp[0]-1, tmp[1]-1, tmp[2], tmp[3], tmp[4]])

dd = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
#  1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.


def firemove(array):
    result = [[[] for _ in range(N)] for _ in range(N)]
    while array:
        r, c, m, s, d = fireball.pop()
    # for i in range(M):
    #     r, c, m, s, d = fireball[i][0], fireball[i][1], fireball[i][2], fireball[i][3], fireball[i][4]
        dr = (r + dd[d][0] * s) % N
        dc = (c + dd[d][1] * s) % N
        result[dr][dc].append((m, s, d))
    return result


def fireburn():
    result = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                continue
            elif len(board[i][j]) >= 2:
                totalMass = 0
                totalSpeed = 0

                evenDirection = 0
                oddDirection = 0

                fireLength = len(board[i][j])

                for l in range(fireLength):
                    m, s, d = board[i][j][l][0], board[i][j][l][1], board[i][j][l][2]
                    totalMass += m
                    totalSpeed += s

                    if d % 2 == 0:
                        evenDirection += 1
                    else:
                        oddDirection += 1

                direction = False
                if (evenDirection != 0 and oddDirection == 0) or (evenDirection == 0 and oddDirection != 0):
                    direction = True

                mass = totalMass // 5
                speed = totalSpeed//fireLength

                if mass <= 0:
                    result[i][j] = []
                else:
                    if direction: # 모두 홀수이거나 짝수는 합이 짝수
                        for nd in range(8):
                            if nd % 2 == 0:
                                result[i][j].append((mass, speed, nd))
                                fireball.append((i, j, mass, speed, nd))
                    else:
                        for nd in range(8):
                            if nd % 2 != 0:
                                result[i][j].append((mass, speed, nd))
                                fireball.append((i, j, mass, speed, nd))
            else:
                result[i][j].append(board[i][j][0])
                fireball.append((i, j, board[i][j][0][0], board[i][j][0][1], board[i][j][0][2]))

    return result


def getTotalMass(graph):
    result = 0
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) > 0:
                for fire in graph[i][j]:
                    result += fire[0]

    return result

#
# board = fireMove(fireball)
# print(*board, sep="\n")
# print()
#
# print("불태우기")
# board = fireBurn()
# print(*board, sep="\n")
#
# print(getTotalMass(board))
# fireball = [(0, 2, 2, 1, 0), (0, 2, 2, 1, 2), (0, 2, 2, 1, 4), (0, 2, 2, 1, 6)]

# board = [[[], [(2, 1, 4)], [], []],
# [[], [], [], []],
# [[], [(2, 1, 0)], [], []],
# [[(2, 1, 6)], [], [(2, 1, 2)], []]]

for k in range(K):
    board = firemove(fireball)
    # print(k)
    # print("fireMove")
    # print(*board, sep="\n")

    board = fireburn()
    # print("after fire burn")
    # print(*board, sep="\n")
    # print("new fireballs")
    # print(fireball)
    # print()

print(getTotalMass(board))

'''
4 2 3
1 1 5 2 2
1 4 7 1 6

5 2 2
2 3 5 1 7
2 2 5 1 0
'''