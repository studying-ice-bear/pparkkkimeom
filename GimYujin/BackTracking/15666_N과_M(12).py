'''
last의 위치 scope 확인하기 -> 같은 수를 여러 번 선택해도 된다.
arr의 어느 index부터 시작하는지 보기 ->
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
comb = []


def dfs(start):
    if len(comb) == M:
        print(*comb)
        return

    last = 0
    for i in range(start, N):
        if last != arr[i]:
            comb.append(arr[i])
            last = arr[i]
            dfs(i)
            comb.remove(arr[i])


dfs(0)
