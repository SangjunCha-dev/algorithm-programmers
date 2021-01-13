def solution(number, k):
    answer = number[0]
    for i in number[1:]:
        answer += i
        try:
            while k and answer[-2] < answer[-1]:
                answer = answer[:-2] + answer[-1]
                k -= 1
        except IndexError: pass
    return answer[:-k] if k else answer