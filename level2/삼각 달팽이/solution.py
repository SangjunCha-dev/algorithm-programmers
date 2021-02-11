def solution(n):
    m, n = (n**2 + n) // 2, 2
    ans = [0 for _ in range(m)]
    pos, val, cnt = 0, 0, 1
    direct = True
    for i in range(1, m+1):
        if direct:
            if pos + val < m:  # 증가
                pos += val
                val += 1
            else:  # 초과
                pos += 1
                if pos == m-1:
                    m = pos - val
                    direct = False
        else:
            if n <= pos - val:  # 감소
                pos -= val
                val -= 1
            else:  # 미만
                n += 2 + cnt * 4
                cnt += 1
                pos += val
                val += 1
                direct = True
        ans[pos] = i
    return ans