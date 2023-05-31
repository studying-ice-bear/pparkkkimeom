# https://www.acmicpc.net/problem/20444

n, k = map(int, input().split())

# for i in range(1, n//2+1):
#     cutPaper = (i+1)*(n-i+1)
#     if cutPaper > k:
#         print('NO')
#         exit()
#     if cutPaper == k:
#         print('YES')
#         exit()
# print('NO')

pointer = n//2
pointerList = [pointer]
# while True:
#     possibleCut = (pointer + 1) * (n - pointer + 1)
#     if pointer > n//2 or 0 > pointer:
#         break
#     if possibleCut == k:
#         print('YES')
#         exit()
#     elif possibleCut > k:
#         pointer -= pointer//2
#     else:
#         pointer += pointer//2
#     if pointer in pointerList:
#         break
#     pointerList.append(pointer)

# print('NO')
start, end = 0, n//2
while start <= end:
    mid = (start + end) // 2
    possibleCut = (mid + 1) * (n - mid + 1)
    if possibleCut == k:
        print('YES')
        exit()
    elif possibleCut > k:
        end = mid - 1
    else:
        start = mid + 1

print('NO')
