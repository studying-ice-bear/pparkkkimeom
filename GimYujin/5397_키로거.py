'''
백스페이스를 입력했다면, '-'가 주어진다
 이때 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지운다.

화살표의 입력은 '<'와 '>'로 주어진다.
소문자 97~122
대문자 65~90
0: 48
1: 49
...
9: 57

BPACd
<
<
B
BP
B<P
BA|P
BAP||
BAPCd
BAPC

'''
import sys
input = sys.stdin.readline
from collections import deque
T = int(input())

for _ in range(T):
    L = input()
    left = deque()
    right = deque()

    for l in L:
        if l == '<':
            if left:
                right.appendleft(left.pop())
        elif l == '>':
            if right:
                left.append(right.popleft())
        elif l == '-':
            if left:
                left.pop()
        else:
            left.append(l)


    print(''.join(left+right))


'''
1
Abcd-

1
12Aa<<b
'''