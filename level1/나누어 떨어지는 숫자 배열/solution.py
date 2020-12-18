def solution(arr, divisor):
    answer = []
    
    for e in arr:
        if not e%divisor:
            answer.append(e)
        
    return sorted(answer) if answer else [-1]