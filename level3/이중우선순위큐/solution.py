import heapq

def solution(operations):
    answer = []
    count = 0
    values_min, values_max = [], []

    for operation in operations:
        op, value = operation.split()
        value = int(value)

        if op == 'I':
            # pyhton은 최소힙으로 기본 동작
            heapq.heappush(values_min, value)
            heapq.heappush(values_max, -value)
            count += 1

        elif op == 'D' and (0 < count):
            if value < 0:
                heapq.heappop(values_min)
            else:
                heapq.heappop(values_max)
            count -= 1

            # 모두 삭제된 경우로 초기화
            if count == 0:
                values_min, values_max = [], []

    if 0 < count:
        answer = [-heapq.heappop(values_max), heapq.heappop(values_min)]
    else:
        answer = [0, 0]

    return answer