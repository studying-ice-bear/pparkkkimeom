# https://www.acmicpc.net/problem/20529

# 564ms

import sys
from itertools import combinations
input = sys.stdin.readline

T = int(input())


def strTo2Base(mbti):
    isZero = ['E', 'S', 'T', 'J']
    answer = ''
    for tag in mbti:
        if tag in isZero:
            answer += '0'
        else:
            answer += '1'
    return answer


def getTotalSimliDistance(target1, target2, target3):
    answer = 0
    sumList = [(target1, target2), (target2, target3), (target1, target3)]
    for a, b in sumList:
        answer += bin(int(a, 2) ^ int(b, 2)).count('1')
    return answer


for _ in range(T):
    N = int(input())
    studentList = list(map(strTo2Base, input().strip().split(' ')))
    # 비둘기 집에 의해 중요한 조건
    if N >= 33:
        print(0)
        continue
    minDistance = float('inf')
    for a, b, c in combinations(studentList, 3):
        tempDistance = getTotalSimliDistance(a, b, c)
        minDistance = min(minDistance, tempDistance)
    print(minDistance)
