import sys
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

visited = [False for _ in range(N)]
combination = []
answer = []


def dfs(cnt):
    if cnt == M:
        if combination not in answer:
            answer.append(combination.copy())
        return

    last = 0
    for i in range(N):
        if not visited[i] and last != numbers[i]:
            visited[i] = True
            last = numbers[i]

            combination.append(numbers[i])
            dfs(cnt+1)
            visited[i] = False
            combination.pop()


dfs(0)

answer.sort()
for a in answer:
    print(*a)

