def solution(n, a, b):
    cnt = 1
    while cnt <= 20:
        a = (a+1) // 2
        b = (b+1) // 2
        if a == b:
            break
        cnt += 1
    return cnt