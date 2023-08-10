# https://www.acmicpc.net/problem/2174
# 64 ms
def main():
    A, B = map(int, input().split())
    N, M = map(int, input().split())

    robot = [[]]
    for _ in range(N):
        DIRECT_INFO = {'N': 0, 'W': 3, 'E': 1, 'S': 2}
        x, y, direction = input().split()
        robot.append([abs(int(y)-B), int(x)-1, DIRECT_INFO[direction]])

    order = []
    for _ in range(M):
        robotName, orderType, repeat = input().split()
        order.append([int(robotName), orderType, int(repeat)])

    def isCrashedOnTheWall(r, c):
        if r < 0 or B <= r or c < 0 or A <= c:
            return True
        return False

    def isCrashedIntoRobot(r, c, name, robot):
        for (robotIdx, eachRobot) in enumerate(robot):
            if robotIdx == name or robotIdx == 0:
                continue
            x, y, direction = eachRobot
            if x == r and y == c:
                return (True, robotIdx)
        return (False, name)

    def operateRobotbyOrder(name, type, robot):
        DIRECTION_LIST = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        curX, curY, curDir = robot[name]
        nextX, nextY, nextDir = curX, curY, curDir
        if type == 'L':
            nextDir = (curDir - 1) % 4
        elif type == 'R':
            nextDir = (curDir + 1) % 4
        else:
            nextDirInfo = DIRECTION_LIST[curDir]
            nextX, nextY = curX + nextDirInfo[0], curY + nextDirInfo[1]
        result01, robotIdx01 = isCrashedIntoRobot(nextX, nextY, name, robot)
        robot[name] = [nextX, nextY, nextDir]

        if result01:
            return (False, robotIdx01, robot)
        result02 = isCrashedOnTheWall(nextX, nextY)

        if result02:
            return (False, name, robot)
        return (True, name, robot)

    for singleOrder in order:
        robotName, orderType, repeat = singleOrder
        for _ in range(repeat):
            (isSucceed, detailInfo, robot) = operateRobotbyOrder(
                robotName, orderType, robot)
            if not isSucceed:
                if detailInfo == robotName:
                    # print('Robot {0} crashes into the wall'.format(robotName))
                    return ('Robot {0} crashes into the wall'.format(robotName))
                else:
                    # print('Robot {0} crashes into robot {1}'.format(
                    # robotName, detailInfo))
                    return ('Robot {0} crashes into robot {1}'.format(
                        robotName, detailInfo))

    return 'OK'


print(main())
