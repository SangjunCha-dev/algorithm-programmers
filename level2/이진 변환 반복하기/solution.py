def solution(s):
    bin_cnt, zero_cnt = 0, 0
    while s != '1':
        cnt = s.count('0')
        s = str(bin(len(s)-cnt))[2:]
        bin_cnt += 1
        zero_cnt += cnt
    return [bin_cnt, zero_cnt]