import sys
input = sys.stdin.readline
N = int(input())
'''
Boyer-Moore 과반수 투표 알고리즘
참조: https://sgc109.github.io/2020/11/30/boyer-moore-majority-vote-algorithm/
'''
def boye_moore_majority_vote(array):
    count = 0
    # 딕셔너리를 활용해 major 군대의 군인 수를 바로 구하도록 해보기 -> 6228ms, 6824ms
    # dict = {}
    for a in array:
        # if a not in dict:
        #     dict[a] = 1
        # else:
        #     dict[a] += 1

        if count == 0:
            major = a
            count = 1
        elif major == a:
            count += 1
        else:
            count -= 1

    # return [major, dict[major]]
    return major


def getArmyCount(array, major):
    count = 0
    for a in array:
        if a == major:
            count += 1
    return count


for i in range(N):
    # graph = list(map(int, input().split()))
    # M = graph[0]
    graph = input().split()     # str으로 활용, map 활용 X
    M = int(graph[0])
    army = graph[1:]

    majorArr = boye_moore_majority_vote(army)
    major = majorArr[0]
    major_army = majorArr[1]
    # major_army = getArmyCount(army, major)

    if major_army > M // 2:
        print(major)
    else:
        print("SYJKGW")


'''해시를 활용해 가장 많은 병사 수 찾기
for i in range(N):
    land = {}
    conquer = -1
    conquer_army = -1
    same = False
    M = graph[i][0]
    for j in range(1, M+1):
        if graph[i][j] not in land.keys():
            land[graph[i][j]] = 1
        else:
            land[graph[i][j]] += 1

        if conquer == land[graph[i][j]]:
            same = True

        elif conquer < land[graph[i][j]]:
            same = False
            conquer = land[graph[i][j]]
            conquer_army = graph[i][j]

    if not same and conquer > M // 2:
        print(conquer_army)
    else:
        print("SYJKGW")
'''

'''
same conquer
0       0   -> X
0       1   -> O
1       0   -> X
1       1   -> X
'''