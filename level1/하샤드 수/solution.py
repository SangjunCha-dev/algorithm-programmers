def solution(x):
    sum, n = 0, x
    while 0 < n:
        sum += n%10
        n //= 10
    return True if (x%sum==0) else False