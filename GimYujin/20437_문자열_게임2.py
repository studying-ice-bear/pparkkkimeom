T = int(input())

for _ in range(T):
    alphabet = [0 for _ in range(27)]

    W = input().strip()
    K = int(input())

    alphabet = [0 for _ in range(27)]
    for word in W:
        i = ord(word)-97
        alphabet[i] += 1

    print(alphabet)

    min_length = 10001

    for i in range(len(W)):
        for j in range(i, len(W)):
            if W[i] == W[j] and i != j:
                print(W[i:j+1])
                min_length = min(min_length, j-i+1)

    if min_length != 10001:
        print(min_length)
    else:
        print(-1)