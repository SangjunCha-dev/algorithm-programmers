import heapq

def solution(jobs):
    answer = 0
    sequences = {}
    heap = []

    for job in jobs:
        if job[0] in sequences:
            sequences[job[0]].append(job[1])
        else:
            sequences[job[0]] = [job[1]]

    now_time, process_time = 0, 0
    while sequences or heap:
        # 디스크 작업 요청
        if now_time in sequences:
            for sequence in sequences[now_time]:
                heapq.heappush(heap, (sequence, now_time))
            del sequences[now_time]

        # 처리중인 작업이 없을 경우
        if (not process_time) and heap:
            process_time, request_time = heapq.heappop(heap)
            # 처리된 시간 = 현재시간 - 요청시간 + 소요시간
            answer += now_time - request_time + process_time

        if 0 < process_time:
            process_time -= 1
        now_time += 1

    answer = answer // len(jobs)
    return answer