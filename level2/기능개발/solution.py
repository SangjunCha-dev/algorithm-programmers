def solution(progresses, speeds):
    answer = []
    
    while progresses:
        num = 0
        for i in range(1, 100):
            total = progresses[0]+(speeds[0]*i)
            if 100 <= total:
                num = i
                break
        
        for i in range(len(progresses)):
            progresses[i] += (speeds[i]*num)
        cnt = 0
        for _ in range(len(progresses)):
            if 100 <= progresses[0]:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            else:
                break
        answer.append(cnt)
            
    return answer