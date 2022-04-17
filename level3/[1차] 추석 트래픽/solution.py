import datetime as dt

def solution(lines):
    answer = 0

    # 기준시간 선별
    base_list = [dt.datetime.strptime(line.split()[1], '%H:%M:%S.%f') + dt.timedelta(seconds=1) for line in lines]
    # 요청 시작시간 선별
    start_list = [dt.datetime.strptime(line.split()[1], '%H:%M:%S.%f') - dt.timedelta(seconds=float(line.split()[2][:-1]) - 0.001) for line in lines]

    for i in range(len(lines)):
        cnt = 1
        base_time = base_list[i]
        for start_time in start_list[i+1:]:
            # 기준시간보다 요청 시작시간이 빠를경우 개수체크
            if start_time < base_time:
                cnt += 1
            # 기준시간보다 요청 시작시간이 오래되었으면 반복문 종료
            elif (base_time + dt.timedelta(seconds=3)) < start_time:
                break
        # 구간내 최대 요청수 비교
        answer = answer if cnt < answer else cnt

    return answer