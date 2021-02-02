def solution(arr, divisor):
    answer = [e for e in arr if not e % divisor]
    return sorted(answer) if answer else [-1]