# 184 ms
N = int(input())

studentList = []

sittingList = [[0 for _ in range(N)] for _ in range(N)]

injupList = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(N**2):
    studentList.append(list(map(int, input().split())))

# 첫 번째 학생 세팅
sittingList[1][1] = studentList[0][0]
news = [(-1, 0), (0, 1), (0, -1), (1, 0)]
for injup in news:
    injupList[1+injup[0]][1+injup[1]].append(studentList[0][0])

def findByCondition01(fullSeat, injupList, likedStudents):
    possibleSeat = []
    for rowIdx in range(len(injupList)):
        for colIdx in range(len(injupList[0])):
            likeCount = 0
            if fullSeat[rowIdx][colIdx] != 0: 
                continue
            for likeStudent in likedStudents:
                if likeStudent in injupList[rowIdx][colIdx]:
                    likeCount += 1
            possibleSeat.append([likeCount, rowIdx, colIdx])
    possibleSeat.sort(key=lambda x: x[0], reverse=True)
    filteredSeat = list(filter(lambda x: x[0] == possibleSeat[0][0], possibleSeat))
    # [[X, Y],...]
    return list(map(lambda x:x[1:], filteredSeat))

def findByCondition02(sittingList, possibleSeat):
    possibleSeatBy02 = []
    for seat in possibleSeat:
        x, y = seat
        emptyCount = 0
        for injup in news:
            if 0 > x+injup[0] or N <= x+injup[0] or 0 > y+injup[1] or N <= y+injup[1]:
                continue
            if sittingList[x+injup[0]][y+injup[1]] == 0:
                emptyCount += 1
        possibleSeatBy02.append([emptyCount, x, y])
    possibleSeatBy02.sort(key=lambda x: x[0], reverse=True)
    filteredSeat = list(filter(lambda x: x[0] == possibleSeatBy02[0][0], possibleSeatBy02))
    # [[X, Y], ...]
    return list(map(lambda x:x[1:], filteredSeat))

def findByCondition03(possibleSeat):
    possibleSeat.sort(key = lambda x:(x[0], x[1]))
    return possibleSeat[0]

def setStudent(seat, injupSeat, targetStudent, possibleSeat):
    x, y = possibleSeat
    seat[x][y] = targetStudent
    for injup in news:
        if 0 > x+injup[0] or N <= x+injup[0] or 0 > y+injup[1] or N <= y+injup[1]:
            continue
        injupSeat[x+injup[0]][y+injup[1]].append(targetStudent)
    return (seat, injupSeat)

# 그 이후 학생 세팅
def settingStudents(students, seat, injup):
    fullSeat = seat
    injupSeat = injup

    for studentInfo in students[1:]:
        possibleSeat = []
        targetStudent = studentInfo[0]
        likedStudents = studentInfo[1:]
        possibleSeat01 = findByCondition01(fullSeat, injupSeat, likedStudents)
        if len(possibleSeat01) == 1:
            possibleSeat = possibleSeat01[0]
        else:
            possibleSeat02 = findByCondition02(fullSeat, possibleSeat01)
            if len(possibleSeat02) == 1:
                possibleSeat = possibleSeat02[0]
            else:
                possibleSeat = findByCondition03(possibleSeat02)
        fullSeat, injupSeat = setStudent(fullSeat, injupSeat, targetStudent, possibleSeat)

    return (fullSeat, injupSeat)

seatResult, injupResult = settingStudents(studentList, sittingList, injupList)

def calculateSatisfaction(seatResult, studentList):
    totalSatisfaction = 0
    for rowIdx in range(len(seatResult)):
        for colIdx in range(len(seatResult[0])):
            target = seatResult[rowIdx][colIdx]
            for studentInfo in studentList:
                likedCount = 0
                targetStudent = studentInfo[0]
                likedStudents = studentInfo[1:]
                if target == targetStudent:
                    for injup in news:
                        if 0 > rowIdx+injup[0] or N <= rowIdx+injup[0] or 0 > colIdx+injup[1] or N <= colIdx+injup[1]:
                            continue
                        if seatResult[rowIdx+injup[0]][colIdx+injup[1]] in likedStudents:
                            likedCount += 1
                # 1이면 1, 2이면 10, 3이면 100, 4이면 1000
                totalSatisfaction += 10 ** (likedCount - 1) if likedCount > 0 else 0
    return totalSatisfaction

print(calculateSatisfaction(seatResult, studentList))