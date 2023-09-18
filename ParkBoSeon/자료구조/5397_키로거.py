import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    keyboard = input().strip()
    pivot = 0
    password = []
    n = 0

    for p in keyboard:
        if p == '<':
            if pivot > 0:
                pivot -= 1
        elif p == '>':
            if pivot < n:
                pivot += 1
        elif p == '-':
            if pivot > 0 and n > 0:
                del password[pivot - 1]
                pivot -= 1
                n -= 1
        else:
            password.insert(pivot, p)
            pivot += 1
            n += 1
    print(''.join(password))