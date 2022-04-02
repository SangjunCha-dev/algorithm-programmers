from collections import deque

def solution(people, limit):
    answer = 0

    # 몸무게 순으로 정렬
    people.sort()
    # 데크 자료형으로 변환
    deq = deque(people)

    light_weight, heavy_weight = 0, 0
    while deq or light_weight or heavy_weight:
        # 가장 작은 몸무게와 가장 큰 몸무게 선별
        if deq and (not light_weight):
            light_weight = deq.popleft()
        if deq and (not heavy_weight):
            heavy_weight = deq.pop()

        if (light_weight + heavy_weight) <= limit:
            light_weight = 0
        heavy_weight = 0
        answer += 1

    return answer