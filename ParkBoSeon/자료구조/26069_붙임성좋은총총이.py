import sys
input = sys.stdin.readline

n = int(input())

flag = False
chongDict = dict()
for i in range(n):
    a, b = input().split()
    
    if a == "ChongChong":
        chongDict["ChongChong"] = 1
        chongDict[b] = 1
        flag = True
        continue
    elif b == "ChongChong":
        chongDict["ChongChong"] = 1
        chongDict[a] = 1
        flag = True
        continue
 
    if flag:
        if a in chongDict:
            chongDict[b] = 1
        elif b in chongDict:
            chongDict[a] = 1

print(len(chongDict))
        