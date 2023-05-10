# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 케이스 5번 시간 초과
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridgeQueue = deque([0 for _ in range(bridge_length)])

    for truck in truck_weights:
        while True:
            if sum(bridgeQueue) - bridgeQueue[-1] + truck <= weight:
                break
            bridgeQueue.appendleft(0)
            bridgeQueue.pop()
            answer += 1
        bridgeQueue.appendleft(truck)
        bridgeQueue.pop()
        answer += 1
    if sum(bridgeQueue) > 0:
        while True:
            if sum(bridgeQueue) == 0:
                break
            bridgeQueue.appendleft(0)
            bridgeQueue.pop()
            answer += 1
        '''
        이게 더 느려요
        for idx in range(len(bridgeQueue)):
            if bridgeQueue[idx] != 0:
                answer += len(bridgeQueue) - idx
                break
        '''
    return answer


# 통과

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridgeQueue = deque([0 for _ in range(bridge_length)])
    totalWeight = 0
    for truck in truck_weights:
        while True:
            if totalWeight - bridgeQueue[-1] + truck <= weight:
                break
            bridgeQueue.appendleft(0)
            totalWeight -= bridgeQueue.pop()
            answer += 1
        bridgeQueue.appendleft(truck)
        totalWeight -= bridgeQueue.pop()
        totalWeight += truck
        answer += 1

    if sum(bridgeQueue) > 0:
        while True:
            if sum(bridgeQueue) == 0:
                break
            bridgeQueue.appendleft(0)
            bridgeQueue.pop()
            answer += 1
    return answer
