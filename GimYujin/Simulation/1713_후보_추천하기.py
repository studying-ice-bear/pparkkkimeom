import sys
input = sys.stdin.readline
N = int(input())    # 사진틀의 개수
M = int(input())    # 전체 학생의 총 추천 횟수
arr = list(map(int, input().split()))   # 추천받은 학생을 나타내는 번호

recommend = [0 for _ in range(101)]
queue = []  # 사진틀
photo = set()

for i in range(M):
    recommend[arr[i]] += 1
    if arr[i] in photo:
        for x, y, z in queue:
            if z == arr[i]:
                queue.remove([x, y, z])
                queue.append([recommend[arr[i]], y, arr[i]])    # 추천받은 횟수, 입력받은 시기, 후보자 번호
                break
    else:
        if len(queue) >= N:
            queue.sort()
            x, y, z = queue.pop(0)
            photo.remove(z)
            recommend[z] = 0

        queue.append([recommend[arr[i]], i, arr[i]])
        photo.add(arr[i])


print(*sorted(photo))

'''
3
14
2 1 4 3 5 6 2 7 2 100 100 54 54 50
-> 
50 54 100

2
6
1 2 3 1 2 4


3
8
1 1 1 2 2 3 3 4
'''