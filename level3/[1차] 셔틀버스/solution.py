from datetime import timedelta
from collections import deque

def solution(n, t, m, timetable):
    t = timedelta(minutes=t)
    shuttle = timedelta(hours=9)

    # 크루 도착시간 타입 변환 및 정렬
    timetable = [timedelta(hours=int(crew[:2]), minutes=int(crew[3:])) for crew in timetable]
    timetable.sort()
    queue = deque(timetable)

    arrival_time = board_shuttle(n, t, m, shuttle, queue)
    answer = time_to_string(arrival_time)
    return answer

def board_shuttle(n, t, m, shuttle, queue: deque):
    '''
    셔틀에 크루 탑승
    '''
    arrival_time = timedelta(minutes=0)

    for _ in range(n):
        remain_seat = m
        for _ in range(m):
            crew = queue.popleft()

            if crew <= shuttle:
                arrival_time = crew
                remain_seat -= 1
            else:
                queue.appendleft(crew)

            if not queue:
                break

        shuttle += t

    if remain_seat:
        # 좌석이 남은 경우
        arrival_time = shuttle - t
    else:
        # 좌석이 없는 경우
        arrival_time -= timedelta(minutes=1)

    return arrival_time

def time_to_string(t: timedelta):
    '''
    time 포맷을 문자열로 변환
    '''
    total_seconds = int(t.total_seconds())
    hours, remainder = total_seconds//3600, total_seconds%3600
    minutes = remainder//60

    return str(hours).zfill(2) + ':' + str(minutes).zfill(2)