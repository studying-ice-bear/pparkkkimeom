money = int(input())
stock = list(map(int, input().split()))
N = len(stock)

jun = money
jun_stock = 0
sung = money
sung_stock = 0

for i in range(14):
    s = stock[i]
    if jun // s > 0:
        jun_stock += jun // s
        jun -= (jun//s)*s

diff = [0] * 15
for i in range(1, 14):
    diff[i] = stock[i]-stock[i-1]

count = 0
for i in range(14):
    s = stock[i]

    if diff[i] > 0:
        if count < 0:
            count = 0
        count += 1
    elif diff[i] < 0:
        if count > 0:
            count = 0
        count -= 1

    if count >= 3:   # 매도
        sung += sung_stock * s
        sung_stock = 0
    if count <= -3:     # 매수
        sung_stock += (sung // s)
        sung = sung - (sung // s) * s

last = stock[-1]
jun += jun_stock * last
sung += sung_stock * last

if jun == sung:
    print("SAMESAME")
elif jun > sung:
    print("BNP")
else:
    print("TIMING")

'''
1. 준현이는 가능한 많이 산다.
2. 성민이는 33매매법
- 3일 연속 가격이 전일 대비 하락하는 주식은 다음날 무조건 가격이 상승한다고 가정
3. 준현 vs 성민
    현금 + 1월 14일의 주가 * 주식 수
    - 준현이 이기면 BNP
    - 성민이 이기면 TIMING
    - 둘의 자산이 같다면 "SAMESAME"
'''