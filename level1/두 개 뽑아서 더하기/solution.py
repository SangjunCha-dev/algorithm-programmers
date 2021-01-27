def solution(numbers):
    answer = []
    for i, val1 in enumerate(numbers):
        for val2 in numbers[i+1:]:
            answer.append(val1+val2)
    return sorted(set(answer))