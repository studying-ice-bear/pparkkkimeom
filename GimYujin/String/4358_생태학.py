import sys
input = sys.stdin.readline
eco = dict()
cnt = 0

while True:
    tree = input().strip()
    if tree == "":
        break
    cnt += 1
    if tree in eco:
        eco[tree] += 1
    else:
        eco[tree] = 1


eco = sorted(eco.items(), key=lambda x: x[0])

for key, value in eco:
    result = round((value / cnt) * 100, 4)
    print("{} {:.4f}".format(key, result))
