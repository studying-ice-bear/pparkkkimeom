# 회전 초밥 벨트에 놓인 접시의 수 N,
# 초밥의 가짓수 d,
# 연속해서 먹는 접시의 수 k,
# 쿠폰 번호 c
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))

answer = 0
start = 0

while start < N:
    end = start + k
    tmp = set()
    tmp.add(c)

    for i in range(start, end):
        i = i % N
        tmp.add(sushi[i])

    answer = max(answer, len(tmp))
    start += 1

print(answer)

'''bruteForce 코드
eat = []
complete = False

for i in range(N):
    tmp = set()
    same = 0
    coupon = False

    if i+k > k:
        for j in range(k):
            s = sushi[(i+j) % N]
            tmp.add(s)
    else:
        tmp = set(sushi[i:i+k])

    tmp.add(c)
    answer = max(answer, len(tmp))

print(answer)
'''
