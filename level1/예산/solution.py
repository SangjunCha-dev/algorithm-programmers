def solution(d, budget):
    d.sort()
    cnt = 0
    for n in d:
        budget -= n
        if budget < 0:
            break 
        cnt += 1
    return cnt