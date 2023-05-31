import sys
input = sys.stdin.readline
n, k = map(int, input().split())

start, end = 0, n-1
flag = True
while start <= end:
    mid = (start + end)//2
    total = (mid+1) * (n-mid+1)
    if total == k:
        print("YES")
        flag = False
        break
    elif total > k:
        end = mid-1
    else:
        start = mid+1

if flag:
    print("NO")


'''
이분 탐색 범위를 2/N만 확인해도 되는 이유
참고: https://david0506.tistory.com/34
'''