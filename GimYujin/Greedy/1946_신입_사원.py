import sys
input = sys.stdin.readline
T = int(input())    # 테스트 케이스

for _ in range(T):
    N = int(input())  # 지원자 수
    score = []
    for i in range(N):
        x, y = map(int, input().split())
        score.append((x, y))

    score.sort()
    answer = 1
    min_score = score[0][1]

    for i in range(1, N):
        if min_score > score[i][1]:
            answer += 1
            min_score = score[i][1]

    print(answer)

'''
다른 모든 지원자와 비교했을 때 
서류심사 성적과 면접시험 성적 중 
적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 
어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 선발X
'''