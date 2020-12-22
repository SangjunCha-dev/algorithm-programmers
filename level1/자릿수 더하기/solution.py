def solution(n):
    answer = 0
    while 0 < n:
        answer += n%10
        n = n//10
    return answer