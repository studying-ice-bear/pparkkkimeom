# https://www.acmicpc.net/problem/1629
# 1234567 1234567 12344321 : 5205370
# 시간 초과 코드
'''
a, b, c = map(int, input().split())


def getLeft(ax, bx, cx):
    answer = 0
    if bx % 2 == 0:
        dividedAx = ax**(bx//2)
        answer = dividedAx**2 % cx
    else:
        dividedAx = ax**(bx//2)
        answer = ((dividedAx**2)*ax) % cx
    return answer


print(getLeft(a, b, c))
'''
# 360 ms
a, b, c = map(int, input().split())


def getLeft(ax, bx, cx):

    bxSqrt = getSquareRoot(bx)
    bxLeft = bx - bxSqrt*bxSqrt

    left_dividedAx = ax**(bxSqrt) % cx
    left_leftDividedAx = ax**(bxLeft) % cx
    answer = (left_dividedAx ** bxSqrt) * left_leftDividedAx
    if answer >= cx:
        answer = answer % cx

    return answer


def getSquareRoot(x):
    if (x == 0 or x == 1):
        return 1
    start = 1
    end = x//2
    while (start <= end):
        mid = (start + end) // 2

        if (mid**2 == x):
            return mid

        if (mid**2 < x):
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

    return ans


print(getLeft(a, b, c))
