import copy
from collections import deque
M, S = map(int, input().split())

# start_fish = deque()
sea = [[[] for _ in range(5)] for _ in range(5)]
fish_direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
shark_direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for _ in range(M):
    fx, fy, d = map(int, input().split())
    # start_fish.append((fx, fy, d-1))
    sea[fx][fy].append(d-1)

sx, sy = map(int, input().split())
# sea[sx][sy].append(-1)

'''
get the best shark move
'''
def sharkMove(sea_graph, smell_graph, shark_x, shark_y, cnt, fish_cnt, move):
    global sx, sy
    global max_eaten
    if cnt == 3:
        if fish_cnt > max_eaten:
            max_eaten = fish_cnt
            shark_moves.append((fish_cnt, move.copy()))
        return

    for i in range(4):
        nx = shark_x + shark_direction[i][0]
        ny = shark_y + shark_direction[i][1]

        if 0 < nx < 5 and 0 < ny < 5:
            # if sea_graph[nx][ny] and sea_graph[nx][ny][0] < 0:
            #     continue

            move.append(shark_direction[i])
            tmp_arr = sea_graph[nx][ny]
            if smell_graph[nx][ny] == 0:
                # tmp_arr = []
                smell_graph[nx][ny] = 3
                sea_graph[nx][ny] = []

            sharkMove(copy.deepcopy(sea_graph), copy.deepcopy(smell_graph), nx, ny, cnt+1, fish_cnt+len(sea_graph[nx][ny]), move)
            # visited[nx][ny] = False
            move.remove(shark_direction[i])
            sea_graph[nx][ny] = tmp_arr


def fishMove(sx, sy, fishs, graph, smell_graph):
    # print("in fishMove()")

    while fishs:
        fish_x, fish_y, fish_d = fishs.popleft()
        # print(fish_x, fish_y, fish_d)
        for i in range(0, -8, -1):
            nd = fish_d + i if fish_d + i >= 0 else 8 + fish_d + i
            nx = fish_x + fish_direction[nd][0]
            ny = fish_y + fish_direction[nd][1]

            if nx == sx and ny == sy:
                continue

            if 0 < nx < 5 and 0 < ny < 5:
                if smell_graph[nx][ny]:
                    continue

                graph[nx][ny].append(nd)
                graph[fish_x][fish_y].remove(fish_d)
                graph[nx][ny].sort()
                graph[fish_x][fish_y].sort()
                break

    return graph


def getFishQue(graph):
    que = deque()
    for i in range(5):
        for j in range(5):
            for d in graph[i][j]:
                if d >= 0:
                    que.append((i, j, d))
    return que

def copyFish(que, graph):
    # print("copyFish")
    # print(que)
    while que:
        fx, fy, fd = que.popleft()
        graph[fx][fy].append(fd)
        graph[fx][fy].sort()
    return graph


smell = [[0 for _ in range(5)] for _ in range(5)]
for _ in range(S):
    print(_)
    fish_que = getFishQue(sea)
    # print(*sea, sep="\n")
    # print()
    print(sx, sy)
    sea = fishMove(sx, sy, fish_que.copy(), copy.deepcopy(sea), copy.deepcopy(smell))

    print("fish moved")
    print(*sea, sep="\n")
    print()
    shark_moves = []
    max_eaten = 0

    sharkMove(sea, smell, sx, sy, 0, 0, deque())
    # shark_moves.sort(reverse=True)
    print("shark_moves: ")
    print(*shark_moves)
    # print(*sea, sep="\n")
    # print()
    shark_eaten, moves = shark_moves[-1][0], shark_moves[-1][1]
    # print(*sea, sep="\n")
    # for i in range(1, 5):
    #     for j in range(1, 5):
    #         if sea[i][j] and sea[i][j][0] < 0:
    #             sea[i][j][0] += 1
    #         if sea[i][j] and sea[i][j][0] == -1:
    #             sea[i][j].remove(-1)

            # if sea[i][j]:
            #     print(i, j, len(sea[i][j]))
            # for k in range(len(sea[i][j])):
            #     print(sea[i][j], k)
            #     if sea[i][j][k] < 0:
            #         sea[i][j][k] += 1
            #     if sea[i][j][k] == -1:
            #         sea[i][j].remove(-1)

    # sea[sx][sy].remove(-1)

    while moves:
        dx, dy = moves.popleft()
        sx = sx + dx
        sy = sy + dy
        smell[sx][sy] = 3
        if sea[sx][sy]:
            sea[sx][sy] = []

    # sea[sx][sy].append(-1)
    # print("상어 이동 후")
    # print(*sea, sep="\n")
    # print()

    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1

    print(sx, sy)
    print("복제 마법")
    print(fish_que)
    sea = copyFish(fish_que.copy(), copy.deepcopy(sea))
    print(*sea, sep="\n")
    print()




answer = 0
# print(*sea, sep="\n")
for i in range(1, 5):
    for j in range(1, 5):
        answer += len(sea[i][j])
print(answer)


'''
5 4
4 3 5
1 3 5
2 4 2
2 1 6
3 4 4
4 2


1 1 1
2 1 7
'''