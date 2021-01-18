def solution(num):
    n, m = 0, 1
    for _ in range(1, num):
        n, m = m, n+m
    return m % 1234567 if n else 0