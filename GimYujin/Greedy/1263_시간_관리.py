N = int(input())
arr = []
# t: 걸리는 시간, e: 기한
for _ in range(N):
    t, e = map(int, input().split())
    arr.append((e, t))

# 마감 기한이 가장 여유로운 일부터 해야하나? v
# 마감 기한이 촉박한 일부터 해야하나?
arr.sort(reverse=True)

# 가장 늦게까지 한 일부터 시작해서 갱신하기
fe, ft = arr[0][0], arr[0][1]
start = fe-ft

cannot = False
for i in range(1, N):
    ee, tt = arr[i][0], arr[i][1]
    if start > ee-tt >= 0:
        start = ee-tt
    else:
        cannot = True
        break

if cannot:
    print(-1)
else:
    print(start)
