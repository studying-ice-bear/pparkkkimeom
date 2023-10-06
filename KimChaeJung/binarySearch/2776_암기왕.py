# https://www.acmicpc.net/problem/2776

# 시간초과
'''
import sys, math
input = sys.stdin.readline
TC = int(input())

for _ in range(TC):
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))
    note1.sort()
    
    for num in note2:
        isCorrect = False
        start, end = [0,len(note1)-1]
        while start <= end:
            mid =  math.floor((start + end)/2)
            if note1[mid] > num:
                end = mid - 1
            elif note1[mid] < num:
                start = mid + 1
            else:
                isCorrect = True
                print(1)
                break
        if isCorrect == False:
            print(0)
'''
# 1528ms
import sys
input = sys.stdin.readline
TC = int(input())

for _ in range(TC):
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))
    setNote1 = set(note1)
    for num in note2:
        if num in setNote1: 
            print(1)
        else:
            print(0)