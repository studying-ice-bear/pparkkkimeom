import sys
input = sys.stdin.readline

def f(a):
    global cache
    
    if a in cache:
        return cache[a]
    elif a <= 1:
        return 1
    else:
        cache[a] = a * f(a-1)
        return cache[a]
    
    return a * f(a - 1) if a > 1 else 1

n, m = map(int, input().split())

cache = {}

if m == 0:
    print(1)
    exit()

r = n - m

print(f(n) // (f(m) * f(r)))