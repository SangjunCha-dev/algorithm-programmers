def solution(progresses, speeds):
    answer = []
    m, cnt = 0, 0
    for i, j in zip(progresses, speeds):
        n = (100-i)//j + 1 if (100-i) % j else (100-i)//j
        if not m:
            m = n

        if m < n:
            answer.append(cnt)
            m = n
            cnt = 1
        else:
            cnt += 1
    
    return answer if sum(answer) == len(speeds) else answer + [cnt]