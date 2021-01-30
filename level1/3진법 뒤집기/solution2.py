def solution(n):
    m = ''
    while 2 < n:
        n, m = n//3, m + str(n%3)
    return int(m + str(n), 3)