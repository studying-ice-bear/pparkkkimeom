N = int(input())
competition = []
for _ in range(N):
    x, p = map(int, input().split())
    competition.append([x, p])

cnt = 1
maxPrize = 0
total = 0

for limit, prize in competition:
    if total <= limit:
        total += prize
        maxPrize = max(maxPrize, prize)
    elif total - maxPrize > limit or maxPrize < prize:
        cnt -= 1
    else:
        cnt -= 1
        total -= maxPrize
        total += prize

    if cnt < 0:
        break

if cnt < 0:
    print("Zzz")
else:
    print("Kkeo-eok")

'''
https://viyoung.tistory.com/121
https://lucas-jang.github.io/BOJ-19582-SUAPC-2020-1.PS-Naruto/#fn:2
'''



'''
어떤 대회를 참가하기 전까지 모은 상금의 합이 그 대회의 상금 상한을 초과한다면 
그 대회는 참가할 수 없다. 

대회가 열리는 순서는 정해져 있고 대회들의 시간은 겹치지 않는다.
'''