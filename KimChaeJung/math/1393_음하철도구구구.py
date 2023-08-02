# https://www.acmicpc.net/problem/1393
import math


# 56ms

def solution():
    xs, ys = map(int, input().split())
    xe, ye, dx, dy = map(int, input().split())

    distance = (xs - xe)**2 + (ys - ye)**2

    after1SecDistance = (xe + dx - xs)**2 + (ye + dy - ys)**2

    if after1SecDistance > distance:
        print(xe, ye)
    elif dx == 0 and dy == 0:
        print(xe, ye)
    else:
        if dy == 0:
            print(xs, ye)
        elif dx == 0:
            print(xe, ys)
        else:
            shortestX = ((dx*dy)/(dy**2 + dx**2)) * \
                (dx/dy*xs + ys + dy/dx*xe - ye)
            shortestY = (dy/dx)*shortestX - (dy/dx*xe) + ye
            print(int(shortestX), int(shortestY))

# solution()


# 틀렸습니다.

def wrong():
    xs, ys = map(int, input().split())
    xe, ye, dx, dy = map(int, input().split())

    distance = (xs - xe)**2 + (ys - ye)**2

    after1SecDistance = (xe + dx - xs)**2 + (ye + dy - ys)**2

    if after1SecDistance > distance:
        print(xe, ye)
    elif dx == 0 and dy == 0:
        print(xe, ye)
    else:
        if dy == 0:
            print(xs, ye)
        elif dx == 0:
            print(xe, ys)
        else:
            slop = dy/dx
            counterSlop = dx/dy
            shortestX = (1/(slop + counterSlop)) * \
                (counterSlop*xs + ys + slop*xe - ye)
            shortestY = slop*(shortestX - xe) + ye
            print(int(shortestX), int(shortestY))


# 40ms

def optimize():
    xs, ys = map(int, input().split())
    xe, ye, dx, dy = map(int, input().split())

    if dx == 0 and dy == 0:
        print(xe, ye)
        exit()

    def getDeg(v1, v2):
        sizeV1 = math.sqrt(v1[0]**2 + v1[1]**2)
        sizeV2 = math.sqrt(v2[0]**2 + v2[1]**2)

        # v1*v2
        innerProduct = v1[0]*v2[0] + v1[1]*v2[1]

        # |v1|*|v2|
        sizeMultiply = sizeV1 * sizeV2

        angleDeg = math.degrees(math.acos(innerProduct/sizeMultiply))
        return angleDeg

    angleDeg = getDeg([xs-xe, ys-ye], [dx, dy])

    if angleDeg < 90:
        if dy == 0:
            print(xs, ye)
        elif dx == 0:
            print(xe, ys)
        else:
            shortestX = ((dx*dy)/(dy**2 + dx**2)) * \
                (dx/dy*xs + ys + dy/dx*xe - ye)
            shortestY = (dy/dx)*shortestX - (dy/dx*xe) + ye
            print(int(shortestX), int(shortestY))

    else:
        print(xe, ye)


optimize()
