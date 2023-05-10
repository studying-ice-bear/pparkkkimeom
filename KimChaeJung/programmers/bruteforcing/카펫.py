def getFactor(yellow):
    factorList = []
    if yellow == 1:
        return [(1, 1)]
    for i in range(yellow+1, 0, -1):
        share, reminder = divmod(yellow, i)
        if reminder == 0:
            factorList.append((i, share))
    return factorList


def solution(brown, yellow):
    answer = []
    possibleYellow = getFactor(yellow)
    for set in possibleYellow:
        row, col = set
        if (row+2)*(col+2) - yellow == brown:
            return [row+2, col+2]
    return [0, 0]
