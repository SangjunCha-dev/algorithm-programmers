def solution(n):
    answer = 0
    i = 1
    quot = n
    while i <= quot:
        quot = n/i
        if int(quot) == quot:
            if quot < i:
                break
            elif quot != i:
                answer += quot
            answer += i 
        i += 1
    return answer