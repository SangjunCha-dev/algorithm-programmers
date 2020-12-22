def solution(priorities, location):
    cnt = 1
    while True:
        num_max = max(priorities)
        cursor = priorities.pop(0)
        if cursor == num_max:
            if location == 0:
                return cnt
            cnt += 1
        else:
            priorities.append(cursor)
            if location == 0:
                location = len(priorities)
        location -= 1