import sys
input = sys.stdin.readline

n = int(input())

maxPrice = 0
total = 0
cnt = 1

for i in range(n):
    limit, price = map(int, input().split())
    
    if total <= limit:
        total += price
        if price > maxPrice:
            maxPrice = price
    elif total - maxPrice > limit or maxPrice < price:
        cnt -= 1
    else:
        cnt -= 1
        total -= maxPrice
        total += price
    if cnt < 0:
        print('Zzz')
        exit()

print("Kkeo-eok")
    
    
