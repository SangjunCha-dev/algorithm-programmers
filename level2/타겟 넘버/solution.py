def solution(numbers, target):
    global max
    global n_list
    max = len(numbers)
    n_list = numbers

    return calc(target, 0)

def calc(tot, n):
    cnt = 0
    if n < max:
        cnt += calc(tot + n_list[n], n+1)
        cnt += calc(tot - n_list[n], n+1)
    elif tot == 0:
        cnt = 1
    return cnt