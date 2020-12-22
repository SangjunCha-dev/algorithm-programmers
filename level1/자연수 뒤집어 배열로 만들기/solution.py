def solution(n):
    answer = []
    while 0 < n:
        answer.append(n%10)
        n = n//10
    return answer