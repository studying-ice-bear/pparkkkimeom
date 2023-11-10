import copy

r, c, k = map(int, input().split())

A = []
for _ in range(r):
    A.append(list(map(int, input().strip().split())))

arr = copy.deepcopy(A)


for _ in range(100):
    if A[r-1][c-1] == k:
        break
    if len(arr) >= len(arr[0]):
        
