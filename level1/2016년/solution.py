def solution(a, b):
    day_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    month_dict = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    days = 4  # 2016년 1월 1일 금요일 시작
    for month in range(1, a):
        days += month_dict[month]
    days += b
    return day_list[days%7]