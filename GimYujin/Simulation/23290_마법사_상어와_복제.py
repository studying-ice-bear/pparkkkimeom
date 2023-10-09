import copy
from collections import deque
M, S = map(int, input().split())

fish_que = deque()
sea = [[[] for _ in range(5)] for _ in range(5)]
fish_direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
shark_direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for _ in range(M):
    fx, fy, d = map(int, input().split())
    fish_que.append((fx, fy, d-1))
    sea[fx][fy].append(d-1)

sx, sy = map(int, input().split())
sea[sx][sy].append(-2)

shark_moves = []
def getSharkMoves(cnt, move):
    if cnt == 3:
        shark_moves.append(move.copy())
        return

    for i in range(4):
        move.append(shark_direction[i])
        getSharkMoves(cnt+1, move)
        move.remove(shark_direction[i])

getSharkMoves(0, [])


answer = 0
visited = [[True for _ in range(4)] for _ in range(4)]


def fishMove(fishs, graph):
    global sx, sy   # 상어 위치

    while fishs:
        fish_x, fish_y, fish_d = fishs.popleft()
        graph[fish_x][fish_y].remove(fish_d)

        for i in range(8):
            nd = fish_d-i if fish_d - i > 0 else 8 - fish_d - i
            nx = fish_x + fish_direction[nd][0]
            ny = fish_y + fish_direction[nd][1]

            if nx != sx and ny != sy:
                if 0 < nx < 5 and 0 < ny < 5:
                    graph[nx][ny].append(nd)
                    break

    return graph



# print(*fishMove([(-1, 0), (-1, 0), (-1, 0)], fish, sea.copy()), sep="\n")

# new_x = fishMove(fish_que, copy.deepcopy(sea))
# print(*sea, sep="\n")
# print()
# print(*new_x, sep="\n")
def getFishQue(graph):
    que = deque()
    for i in range(6):
        for j in range(6):
            if graph[i][j]:
                for d in graph[i][j]:
                    que.append((i, j, d))

    return que


def moveShark(d, fish_que=fish_que):
    fish_count = 0
    new_sea = fishMove(fish_que, copy.deepcopy(sea))
    fish_que = getFishQue(new_sea)

    tmp_sx, tmp_sy = sx, sy
    for i in range(3):
        new_sx = tmp_sx + shark_direction[d][0]
        new_sy = tmp_sy + shark_direction[d][1]

        if 0 < new_sx < 5 and 0 < new_sy < 5:
            if new_sea[new_sx][new_sy]:
                fish_count += len(new_sea[new_sx][new_sy])
                new_sea[new_sx][new_sy] = [-2]  # 물고기 냄새

            tmp_sx = new_sx
            tmp_sy = new_sy

    return new_sea


def copyMagic(cnt, sea_graph, fish_count):
    global answer
    if cnt == S:
        answer = max(answer, fish_count)
        return

    for i in range(64):
        new_graph = moveShark(shark_moves[i])
        copyMagic(cnt+1, new_graph, fish_count)


fishMove(fish_que, sea)
