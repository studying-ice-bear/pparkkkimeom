import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    alphabet = [0 for _ in range(27)]

    W = input().strip()
    K = int(input())

    alphabet = [0 for _ in range(27)]
    locations = [[] for _ in range(27)]
    min_length = 10000
    max_length = 0
    result = []

    for i in range(len(W)):
        word = W[i]
        j = ord(word)-97
        alphabet[j] += 1
        locations[j].append(i)

        if alphabet[j] >= K:
            start = locations[j][-K]
            end = locations[j][-1]
            result.append(W[start: end+1])

            min_length = min(min_length, end-start+1)
            max_length = max(max_length, end-start+1)

    if min_length == 10000 and max_length == 0:
        print(-1)
    else:
        print(min_length, max_length)

    # words = []
    # min_length = 10001
    # min_word = W
    # same = dict()
    # for i in range(len(W)-1):
    #     for j in range(i+1, len(W)):
    #         if W[i] == W[j] and j-i+1 >= K:
    #             print(W[i:j+1], j-i+1)
    #             tmp = W[i:j+1]
    #             words.append(tmp)
    #             if tmp not in same.keys():
    #                 same[tmp] = {}
    #
    #             if j-i+1 < min_length:
    #                 min_length = j-i+1
    #                 min_word = tmp
    #
    # words = list(set(words))
    # words.sort()
    # print("min_word", min_word)
    # print(words)
    #
    # min_length2 = 10001
    # w_list = []
    # for i in range(len(W)-1):
    #     for j in range(i+1, len(W)):
    #         tmp = str(W[i:j])
    #         if min_word in tmp and min_word != tmp:
    #             if tmp[0] == tmp[-1]:
    #                 w_list.append(tmp)
    #                 min_length2 = min(len(tmp), min_length2)
    #
    # w_list.sort()
    # print("w_list", w_list)
    # if min_length != 10001:
    #     print(min_length, min_length2)
    # else:
    #     print(-1)
