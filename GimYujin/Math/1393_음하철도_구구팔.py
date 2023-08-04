'''
https://hini7.tistory.com/75
https://0902.tistory.com/63
문제 이해 참고: https://flreauniverse.tistory.com/4
1. 증가하는 방향
(2, 4) -> (1, 2)만큼 증가한다.
=> 최대공약수로 나눠야 한다.

2. 정류장과 가장 가까운 위치에서 다시 멀어지면 아무 의미 없다.
'''
import math

sx, sy = map(int, input().split())    # 정류장의 위치
# (ex, ey) 현재 열차 위치, 1초마다 증가 방향으로 dx, dy
ex, ey, dx, dy = map(int, input().split())


def gcd(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1

    while n2 > 0:
        n1, n2 = n2, n1 % n2

    return n1

if dx != 0 and dy != 0:
    N = gcd(dx, dy)
    dx, dy = dx//N, dy//N

cx, cy = ex, ey
while True:
    curr = math.sqrt((cx - sx) ** 2 + (cy - sy) ** 2)
    diff = math.sqrt(((cx+dx) - sx) ** 2 + ((cy+dy) - sy) ** 2)

    if curr > diff:
        cx += dx
        cy += dy
    else:
        print(cx, cy)
        break

'''
-3 -3
2 1 -4 -2

50 721
0 0 7 3
ans: 70 30
'''