import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

    

ioi = input().strip()
answer = 0
cnt = 0
i = 0

while i < m - 1:
    if ioi[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            answer += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(answer)