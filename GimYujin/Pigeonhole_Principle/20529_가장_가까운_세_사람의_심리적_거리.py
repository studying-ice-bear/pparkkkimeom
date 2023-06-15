from itertools import combinations
import sys
input = sys.stdin.readline
T = int(input())

for t in range(T):
    N = int(input())
    mbti = list([c for c in s] for s in input().strip().split())
    if N > 32:
        print(0)
    else:
        distance = 12
        for A, B, C in combinations(mbti, 3):
            ab = 0
            for a, b in zip(A, B):
                if a != b:
                    ab += 1

            bc = 0
            for b, c in zip(B, C):
                if b != c:
                    bc += 1

            ac = 0
            for a, c in zip(A, C):
                if a != c:
                    ac += 1

            total = ab+bc+ac

            if distance > total:
                distance = total

        print(distance)

    # distance = []
    # for i in range(N):
    #     for j in range(i, N):
    #
    #         tmp = 0
    #         if i == j:
    #             continue
    #
    #         for a, b in zip(mbti[i], mbti[j]):
    #             if a != b:
    #                 tmp += 1
    #         print(mbti[i], mbti[j], tmp)
    #         distance.append(tmp)
    # distance.sort()
    # print(distance)
    # print(sum(distance[:3]))
