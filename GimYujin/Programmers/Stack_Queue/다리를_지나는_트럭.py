from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_weight = 0
    time = 0
    bridge = deque()
    trucks = deque(truck_weights)

    while trucks or bridge:
        # print(time, trucks, bridge)
        if len(bridge) >= bridge_length:
            b = bridge.pop()
            bridge_weight -= b

        if trucks:
            time += 1
            truck = trucks[0]
            bridge_weight += truck

            if bridge_weight > weight:
                bridge.appendleft(0)
                bridge_weight -= truck
            else:
                bridge.appendleft(truck)
                trucks.popleft()
        else:
            for i in range(len(bridge)):
                if bridge[i] != 0:
                    break
            time += bridge_length - i
            return time

    answer = time

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
