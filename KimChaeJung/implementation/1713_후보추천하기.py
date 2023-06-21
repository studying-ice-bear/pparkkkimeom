# https://www.acmicpc.net/problem/1713

# 76ms

N = int(input())
recCount = int(input())
recList = list(map(int, input().split()))

frameList = [[recList[0], 1]]
studentList = [0 for _ in range(101)]
studentList[recList[0]] += 1


def findMinimumVal(targetList):
    minimumVal = float('inf')
    for value in targetList:
        if value == 0:
            continue
        if value < minimumVal:
            minimumVal = value
    return minimumVal


for student in recList[1:]:
    if studentList[student] == 0:
        if len(frameList) >= N:
            for recIdx in range(len(frameList)):
                minimumRecCount = findMinimumVal(studentList)
                if frameList[recIdx][1] == minimumRecCount:
                    outStudent = frameList.pop(recIdx)
                    studentList[outStudent[0]] = 0
                    break
        frameList.append([student, 1])
        studentList[student] += 1
    else:
        for recIdx in range(len(frameList)):
            if frameList[recIdx][0] == student:
                frameList[recIdx][1] += 1
                studentList[student] += 1
                break

answer = []
for frameStudentInfo in frameList:
    answer.append(frameStudentInfo[0])
print(*sorted(answer))


# 80ms
anotherAnswer = [x[0] for x in sorted(frameList, key=lambda x: x[0])]
print(*anotherAnswer)
