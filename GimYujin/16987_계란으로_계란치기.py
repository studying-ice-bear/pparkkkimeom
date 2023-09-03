'''

1. 가장 왼쪽의 계란을 든다.

2.
손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다.
단, 손에 든 계란이 깨졌거나
깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다.

이후 손에 든 계란을 원래 자리에 내려놓고 3번 과정을 진행한다.

3.
가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행한다.
단, 가장 최근에 든 계란이
가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료한다.
'''

N = int(input())
eggs = []

for _ in range(N):
    d, w = map(int, input().split()) # 내구도, 무게
    eggs.append([d, w])

answer = 0

def bt(n, cnt):
    global answer
    # 현재 계란으로 다른 모든 계란을 내리쳤을 때
    if cnt == N:
        tmp = 0
        for j in range(N):
            if eggs[j][0] <= 0:
                tmp += 1

        answer = max(answer, tmp)
        return

    for i in range(N):
        if i == n:
            continue

        eggs[n][0] -= eggs[i][1]
        eggs[i][0] -= eggs[n][1]

        bt(n, cnt + 1)

        eggs[n][0] += eggs[i][1]
        eggs[i][0] += eggs[n][1]


bt(0, 0)
print(answer)
