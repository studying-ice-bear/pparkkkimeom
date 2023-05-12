import copy
from collections import defaultdict
N, M = map(int, input().split())
notTogether = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    notTogether[a].append(b)
    notTogether[b].append(a)

result = []
for i in range(1, N+1):
    tmp = []
    tmp.append(i)
    for j in range(1, N+1):
        if i == j:
            continue

        if j in notTogether[i]:
            continue
        if i in notTogether[j]:
            continue

        tmp.append(j)

        for k in range(1, N+1):
            if k == i or k == j:
                continue

            if k in notTogether[i]:
                continue

            if k in notTogether[j]:
                continue

            if i in notTogether[k]:
                continue

            if j in notTogether[k]:
                continue

            tmp.append(k)

            new_tmp = copy.deepcopy(tmp)
            new_tmp.sort()

            if new_tmp not in result:
                result.append(new_tmp)

            tmp.pop()

        tmp.pop()

print(len(result))
