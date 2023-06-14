from collections import deque
N, M = map(int, input().split())    # N: 사다리 개수, M: 뱀의 개수
gameBoard = [i for i in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    gameBoard[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    gameBoard[u] = v

board = [0 for _ in range(101)]
visited = [False for _ in range(101)]


def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        at = queue.popleft()
        if at == 100:
            print(board[100])
            break

        for i in range(1, 7):
            to = at + i

            if to > 100 or visited[to]:
                continue

            if to != gameBoard[to]:
                to = gameBoard[to]

            if not visited[to]:
                visited[to] = True
                board[to] = board[at] + 1
                queue.append(to)


bfs(1)

'''
dp로 풀어보려 했지만 이 글(https://www.acmicpc.net/board/view/99625)의 3번 조건 떄문에 안됨 
dice = [i // 6 + 1 if i % 6 != 0 else i // 6 for i in range(101)]
dice[0] = 1

for i in range(1, 101):
    if i < gameBoard[i]:    # 사다리
        dice[gameBoard[i]] = dice[i]
        for j in range(gameBoard[i], 101):
            dice[j] = min(dice[j], dice[i]+(j-gameBoard[i])//6+1 if j % 6 != 0 else dice[i]+(j-gameBoard[i])//6)

    elif i > gameBoard[i]:
        dice[gameBoard[i]] = i

print(dice[100])
'''
