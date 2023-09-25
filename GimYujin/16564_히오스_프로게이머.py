
N, K = map(int, input().split())
arr = []
for _ in range(N):
    tmp = int(input())
    arr.append(tmp)

while K > 1:
    arr.sort()
    small = min(arr)

    cnt = 0

    for i in range(len(arr)):
        if arr[i] == small:
            cnt += 1
        else:
            break

    if cnt != 1:
        second = arr[cnt-1]
    else:
        second = arr[1]

    if second-small < K:
        if small == second:
            arr[0] += K//cnt
            K -= K//cnt
        else:
            arr[0] += second-small
            K -= second-small
    else:
        arr[0] += second - small

print(min(arr))
