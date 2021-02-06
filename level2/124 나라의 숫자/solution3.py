def solution(n):
    num = ['1','2','4']
    ans = ''
    while 0 < n:
        n -= 1
        ans = num[n % 3] + ans
        n //= 3
    return ans