import sys
input = sys.stdin.readline

money = int(input())
MachineDuck = list(map(int, input().split()))


def BNP(m, md):
    cnt = 0
    
    for stock in md:
        if m >= stock:
            cnt += (m // stock)
            m = m % stock

    return m + (md[-1] * cnt)
    
    


def TIMING(m, md):
    increase = 0
    decrease = 0
    
    cnt = 0
    
    prev = md[0]
    
    for stock in md[1:]:        
        if stock < prev:
            decrease += 1
            increase = 0
        elif stock > prev:
            increase += 1
            decrease = 0
            
        prev = stock
        
        if decrease == 3:
            cnt += (m // stock)
            m = m % stock
            decrease -= 1
        elif increase == 3 and cnt > 0:
            m += (cnt * stock)
            cnt = 0
            increase -= 1
    
    return m + (cnt * md[-1])
    
bnp = BNP(money, MachineDuck)
timing = TIMING(money, MachineDuck)


if bnp > timing:
    print("BNP")
elif bnp < timing:
    print("TIMING")
elif bnp == timing:
    print("SAMESAME")