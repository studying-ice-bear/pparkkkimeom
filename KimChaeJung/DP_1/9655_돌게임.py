# 44ms
dolCount = int(input())

winList = ['SK' if i%2==1 else 'CY' for i in range(1001)]

print(winList[dolCount])