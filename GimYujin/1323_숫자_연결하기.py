import sys
input = sys.stdin.readline
N, K = map(int, input().split())

pattern = [False for _ in range(K)]
cnt = 0
number = N
while True:
    if not pattern[number % K]:
        pattern[number % K] = True
    else:
        print(-1)
        break

    if number % K == 0:
        print(cnt+1)
        break

    number = int(str(number % K)+str(N))
    # number += N*10**cnt
    cnt += 1
    # print(number)
'''
참고한 블로그
https://khu98.tistory.com/96
https://ddggblog.tistory.com/155
'''