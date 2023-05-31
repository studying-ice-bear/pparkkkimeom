# https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    applicant = int(input())
    applicantInfo = []
    hasSameGrade = False
    for _ in range(applicant):
        eachInfo = tuple(map(int, input().split()))
        applicantInfo.append(eachInfo)
    applicantInfo.sort(key=lambda x: (x[0], x[1]))

    answer = 0

    limitMax = 0
    for each in applicantInfo:
        if each[0] == 1:
            answer += 1
            limitMax = each[1]
            continue
        if each[0] == applicant:
            if limitMax > each[1]:
                answer += 1
            continue
        if limitMax < each[1]:
            continue
        if limitMax > each[1]:
            answer += 1
            limitMax = each[1]
            continue
        if each[0] == each[1]:
            limitMax = each[1]
            answer += 1
            continue

    print(answer)
