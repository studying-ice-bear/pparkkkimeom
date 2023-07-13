# https://www.acmicpc.net/problem/5397
from collections import deque
TC = int(input())


def wrong(TC):
    for _ in range(TC):
        keyInput = input()
        index = 0
        password = []
        for key in keyInput:
            if key == '<':
                index = max(0, index - 1)

            elif key == '>':
                index = min(len(password), index + 1)

            elif key == '-':
                if len(password) == 0:
                    index = 0
                    continue
                else:
                    if index == (len(password) - 1):
                        password.pop()
                    else:
                        del password[index-1]
                        # password = password[:index-1] + password[index:]
                index -= 1
            else:
                if index == (len(password)):
                    password.append(key)
                else:
                    password.insert(index, key)
                index += 1

        print(''.join(password))

# 672 ms


def solution(TC):
    for _ in range(TC):
        keyInput = input()
        left = []
        right = deque([])
        for key in keyInput:
            if key == '<':
                if len(left) != 0:
                    right.appendleft(left.pop())
            elif key == '>':
                if len(right) != 0:
                    left.append(right.popleft())
            elif key == '-':
                if len(left) != 0:
                    left.pop()
            else:
                left.append(key)
        left.extend(right)

        print(''.join(left))


solution(TC)
