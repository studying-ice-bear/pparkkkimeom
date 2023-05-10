# https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    resultList = [numbers[0], -numbers[0]]

    for i in range(1, len(numbers)):
        deleteNum = len(resultList)
        for j in range(len(resultList)):
            preNum = resultList[j]
            resultList.append(preNum+numbers[i])
            resultList.append(preNum-numbers[i])

        del resultList[:deleteNum]

    answer = resultList.count(target)
    return answer

# DFS 풀이 방식


def solution(numbers, target):
    numberCount = len(numbers)

    global answer
    answer = 0

    def dfs(i, now):
        global answer
        if i == numberCount:
            if now == target:
                answer += 1
        else:
            dfs(i+1, now + numbers[i])
            dfs(i+1, now - numbers[i])

    dfs(1, numbers[0])
    dfs(1, -numbers[0])

    return answer
