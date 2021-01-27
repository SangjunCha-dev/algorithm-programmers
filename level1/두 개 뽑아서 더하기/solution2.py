from itertools import combinations

def solution(numbers):
    answer = []
    for val in set(combinations(numbers, 2)):
        answer.append(sum(val))
    return sorted(set(answer))