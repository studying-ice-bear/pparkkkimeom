from collections import deque
N = int(input())
arr = list(map(int, input().split()))
balloons = [i for i in range(1, N + 1)]

que = deque()
que.append((arr[0], 1))

answer = []
curr = 0

while arr:
    # print("curr: ", curr)
    balloon = balloons.pop(curr)
    num = arr.pop(curr)
    answer.append(balloon)

    # print("after")
    # print(arr)
    # print(balloons)

    length = 0
    if len(arr) == 0:
        length = 1
    else:
        length = len(arr)

    if num < 0:
        next = (length + curr + num) % length
    else:
        next = (curr + num - 1) % length

    # print("next: ", next)
    curr = next
    # print()
    # print(answer)
    # print()

print(*answer)

''' deque, enumerate 사용
from collections import deque
n = int(input())
q = deque(enumerate(map(int,input().split())))
ans=[]

while q:
    idx,num = q.popleft()
    ans.append(idx+1)
    if num>0:
        q.rotate(-(num-1))
    elif num<0:
        q.rotate(-num)

print(' '.join(map(str,ans)))
'''
'''
5
-1 -1 -1 -1 -1

curr : 0
[3, 2, 1, -3, -1]
[1, 2, 3, 4, 5]
(3, 1)
next: 3
answer: [1]

curr: 3
[2, 1, -3, -1]
[2, 3, 4, 5]
(-3, 4)
next: (3-3)-1

(-3, 4) 
curr: 2 -3 = -1 => len(arr)-1=2
[2, 1, -1]
[2, 4, 5]

(-1, 5)
curr: -1
[2, 1]
[2, 4]
=> curr:(2-1)  % len(arr)

(2, 2)
[1]
[4]
curr: (2 + 2) % len(arr)

'''