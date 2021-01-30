def solution(n):
    m = ''
    while 2 < n:
        n, m = n//3, m + str(n%3)
    n, m = 0, int(m + str(n))
    c = 0
    while m:
        n, m, c = n + (m%10 * 3**c), m//10, c+1
    return n