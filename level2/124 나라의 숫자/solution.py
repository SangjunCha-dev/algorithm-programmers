def solution(n):
    ans = ''
    while 0 < n:
        n, m = n//3, n%3
        if not m: 
            n, m = n-1, 4 
        ans = str(m) + ans
    return ans