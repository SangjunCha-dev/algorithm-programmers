def solution(n):
    n = n**0.5 
    if int(n) == n:
        return (n+1)**2
    return -1