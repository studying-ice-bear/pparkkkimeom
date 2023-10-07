# https://www.acmicpc.net/problem/2529
# 40ms
k = int(input())
signList = input().split()

def getMaxValue(k, signList):
    result=[9]
    for i in range(k):
        if signList[i] == '>':
            for num in range(result[i] - 1, -1, -1):
                if num in result:
                    continue
                else:
                    result.append(num)
                    break
        else:
            result.append(result[i])
            for j in range(i, -1, -1):
                if signList[j] == '>':
                    break
                result[j] -= 1
    print(''.join(map(str, result)))

def getMinValue(k, signList):
    result = [0]
    for i in range(k):
        if signList[i] == '<':
            for num in range(result[i] + 1, k+1):
                if num in result:
                    continue
                else:
                    result.append(num)
                    break
        else:
            result.append(result[i])
            for j in range(i, -1, -1):
                if signList[j] == '<':
                    break
                result[j] += 1
    print(''.join(map(str, result)))
            
getMaxValue(k, signList)
getMinValue(k, signList)