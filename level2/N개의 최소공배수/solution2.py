def solution(arr):
    answer = arr[0]
    for i in arr[1:]:
        answer = lcm(answer, i)
    return answer

def lcm(m, n):
    return m * n // gcd(m, n)

def gcd(m, n):
    while n != 0:
       t = m % n
       (m,n) = (n,t)
    return m