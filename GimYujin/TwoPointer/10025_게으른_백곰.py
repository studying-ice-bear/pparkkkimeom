N, K = map(int, input().split())

ice = [0] * 1000001
end = 0
for _ in range(N):
    g, x = map(int, input().split())
    ice[x] = g
    end = max(end, x)

step = 2 * K + 1
window = sum(ice[:step])
answer = window
for i in range(step, end+1):
    window += ice[i] - ice[i-step]
    answer = max(answer, window)

print(answer)

# for i in range(N):
#     s, e, cnt = 0, 0, 0
#     total = 0
#     while s <= e:
#         dis = abs(ice[s][0] - ice[e][0])
#         if dis <= K:
#             total += ice[e][0]
#             e += 1
#         else:
#             s += 1

'''
좌표: 0 <= x <= 1000000
좌우: 1 <= K <= 2000000
- 최적의 자리를 골랐을 때 얼음의 합
얼음 합의 최댓값

참고한 코드: https://kimmeh1.tistory.com/404
슬라이딩 윈도우 공부하기!!

'''