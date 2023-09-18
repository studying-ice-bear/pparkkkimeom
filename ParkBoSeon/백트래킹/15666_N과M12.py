import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(set(list(map(int, input().split()))))
nums.sort()
queue = []

def dfs(s, q, c):
    if m == c:
        print(*q)
        return
    
    for i in range(s, len(nums)):
        q.append(nums[i])
        dfs(i, q, c + 1)
        q.pop()


dfs(0, queue, 0)

