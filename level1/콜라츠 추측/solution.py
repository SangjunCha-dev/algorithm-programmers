def solution(num):
    cnt = 0
    while cnt < 500:
        if num == 1: 
            return cnt
        num = num/2 if num%2==0 else num*3+1
        cnt += 1
    return -1