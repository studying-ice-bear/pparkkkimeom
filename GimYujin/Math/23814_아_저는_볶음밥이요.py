'''
참고: https://burningfalls.github.io/algorithm/boj-23814/
'''

D = int(input())
# 입력되는 정수의 범위가 넓어 32비트 정수형으로 처리할 수 없음에 유의하라.
# 짜장면, 짬뽕, 남은 사람 수
N, M, K = map(int, input().split())

# 군만두를 가장 많이 받을 수 있는 경우
# 볶음밥을 최대한 많이 시키자!
nq, nr = divmod(N, D)
mq, mr = divmod(M, D)
kq, kr = divmod(K, D)

# 볶음밥을 아예 옮기지 않는 경우
l = [(nq+mq+kq, K)]

# 남은 사람의 수와 비교
# N을 D의 배수로 만드는 경우 -> N을 D의 배수로 만듦.
if K >= D - nr:
    k2 = K - (D-nr)
    k2q, k2r = divmod(k2, D)
    l += [(nq+mq+k2q+1, k2)]

# M을 D의 배수로 만드는 경우
if K >= D - mr:
    k2 = K - (D-mr)
    k2q, k2r = divmod(k2, D)
    l += [(nq+mq+k2q+1, k2)]

# N과 M 둘 다 D의 배수로 만드는 경우
if K >= 2 * D - nr - mr:
    k2 = K - (2*D-nr-mr)
    k2q, k2r = divmod(k2, D)
    l += [(nq+mq+k2q+2, k2)]


print(l)
l.sort()
print(l)
print(l[-1][1])


'''C로 작성되었던 코드 참고:https://everydaywoogi.tistory.com/141
maxsize = (N+M+K) / D
arr = [0 for _ in range(4)]
size = [0 for _ in range(4)]

# N과 M 둘 다 D의 배수로 만드는 경우
arr[0] = N/D + M / D + K / D
size[0] = K

nn = N % D
mm = M % D

arr[1] = (N + (D-nn)/D) + (K-(D-mm)) / D
size[1] = K - (D-mm)

arr[2] = N/D + (M+(D-mm)) / D + (K-(D-mm))/D
size[2] = K - (D-mm)

arr[3] = (N+(D-nn)) / D + (M + (D-mm)) / D + (K-(D-nn) - (D-mm)) / D
size[3] = K - (D-nn) - (D-mm)
'''
