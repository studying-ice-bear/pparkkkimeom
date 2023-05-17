V, E = map(int, input().split())

weight = []

for _ in range(E):
    a, b, c = map(int, input().split())
    weight.append((c, a, b))

weight.sort()

union_find = [i for i in range(V+1)]
pick = []


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


total = 0
for w in weight:
    pick.append((w[1], w[2]))
    if find_parent(union_find, w[1]) != find_parent(union_find, w[2]):
        union_parent(union_find, w[1], w[2])
        total += w[0]
    # print(pick, union_find)
print(total)

'''
최소 스패닝 트리 특징
1. 간선의 가중치의 합이 최소
2. n개의 정점을 가지는 그래프에 대해 반드시 (n-1)개 간선만을 사용
3. 사이클이 포함 X
출처: https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html

1. 간선의 가중치의 합이 최소
(가중치, 시작점, 끝점)으로 배열을 만들어 sort
2. 사이클을 확인하면서 자연스럽게 만족됨.
3. 사이클 확인 방법들(https://sosoeasy.tistory.com/35)
- 유니온 파인드 활용(https://chiefcoder.tistory.com/55)
 
참고: https://hillier.tistory.com/54
- 현재 문제 풀이는 크루스칼 알고리즘을 사용한 경우
- 프림 알고리즘을 활용해야 하는 경우도 있다.

참고2: https://sosoeasy.tistory.com/47
dfs로도 사이클을 확인할 수 있지만 시간 초과 발생

'''

