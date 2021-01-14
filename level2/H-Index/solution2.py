def solution(citations):
    citations.sort(reverse=True)
    for i, num in enumerate(citations, start=1):
        if num < i: return i-1
    return i