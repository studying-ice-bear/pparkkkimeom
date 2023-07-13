# https://www.acmicpc.net/problem/15666


N, M = map(int, input().split())
numList = list(set((map(int, input().split()))))

numList.sort()


def backtracking(start, answer):
    global numList

    if len(answer) == M:
        # 48 ms
        print(' '.join(map(lambda x: str(numList[x]), answer)))
        '''
        52 ms
        readyToPrint = []
        for num in answer:
            readyToPrint.append(numList[num])
        print(*readyToPrint)
        '''
        return

    for i in range(start, len(numList)):
        answer.append(i)
        backtracking(i, answer)
        answer.pop()


backtracking(0, [])
