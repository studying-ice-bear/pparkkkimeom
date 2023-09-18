import sys
import math
input = sys.stdin.readline


xs, ys = map(int, input().split())

xe, ye, dx, dy = map(int, input().split())
answer = [0, 0]
dis = 1000001
r = math.gcd(dx, dy)

a, b = dx // r, dy // r

while True:
    
    temp = math.sqrt(((xe - xs) ** 2) + ((ye - ys) ** 2))
    if dis > temp:
        answer[0] = xe
        answer[1] = ye
    
    xe += a
    ye += b
    
    if math.sqrt(((xe - xs) ** 2) + ((ye - ys) ** 2)) > temp:
        break
    
print(*answer)