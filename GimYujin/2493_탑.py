
N = int(input())
towers = list(map(int, input().split()))
lazer = [0 for _ in range(N)]

stack = []

for i in range(N):
    while stack:
        if towers[stack[-1][0]] < towers[i]:
            stack.pop()
        else:
            lazer[i] = stack[-1][0] + 1
            break

    stack.append((i, towers[i]))

print(*lazer)

'''
참고: https://velog.io/@joniekwon/Python-%EB%B0%B1%EC%A4%80-2493%EB%B2%88-%ED%83%91
주의!!!break문이 있어야 시간초과가 나지 않는다!
'''