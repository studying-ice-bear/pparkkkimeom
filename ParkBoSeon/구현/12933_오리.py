import sys
input = sys.stdin.readline

# def check(d):
#     for i in range(len(d)):
        
    

quack = list(input().strip())

if quack[0] != 'q':
    print(-1)
    exit()

ducks = [quack[0]]

for s in quack[1:]:
    for i in range(len(ducks)):
        if s == 'q':
            if ducks[i][-1] == 'k':
                ducks[i] = ducks[i] + 'q'
                break
            elif i == len(ducks) - 1 and ducks[i][-1] != 'k':
                ducks.append('q')
                break
        elif s == 'u' and ducks[i][-1] == 'q':
            ducks[i] = ducks[i] + 'u'
            break
        elif s == 'a' and ducks[i][-1] == 'u':
            ducks[i] = ducks[i] + 'a'
            break
        elif s == 'c' and ducks[i][-1] == 'a':
            ducks[i] = ducks[i] + 'c'
            break
        elif s == 'k' and ducks[i][-1] == 'c':
            ducks[i] = ducks[i] + 'k'
            break
        elif i == len(ducks) - 1:
            print(-1)
            exit()

for i in range(len(ducks)):
    if len(ducks[i]) % 5 != 0:
        print(-1)
        exit()
print(len(ducks))