from collections import deque


def get_div(number):
    result = set()
    for i in range(1, number + 1):
        if number % i == 0:
            result.add(i)

    return result


def solution(brown, yellow):
    answer = []
    set_yellow = get_div(yellow)

    for y in set_yellow:
        carpet = deque()
        for _ in range(yellow // y):
            carpet.append([1 for _ in range(y)])
        # print(carpet)

        h, w = len(carpet), len(carpet[0])
        # print(h, w, 2*(h+w+4) - 4)
        if brown == 2 * (h + w + 4) - 4:
            if h >= w:
                answer.append(h + 2)
                answer.append(w + 2)

    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
