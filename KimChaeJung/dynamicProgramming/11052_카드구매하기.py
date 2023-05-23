# https://www.acmicpc.net/problem/11052
cardCount = int(input())
cardPrice = list(map(int, input().split()))
cardPrice.insert(0, 0)
cardMaxPrice = [0 for _ in range(cardCount + 1)]

for idx in range(1, len(cardPrice)):
    maxSum = cardPrice[idx]
    for childIdx in range(1, idx):
        maxSum = max(cardMaxPrice[childIdx] +
                     cardMaxPrice[idx-childIdx], maxSum)

    cardMaxPrice[idx] = maxSum

print(cardMaxPrice[-1])
