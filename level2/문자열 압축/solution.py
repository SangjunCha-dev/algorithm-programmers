def solution(s):
    ans = len(s)
    for i in range(1, ans//2 + 1):
        t_lst = [s[n:n+i] for n in range(0, len(s), i)]
        fix, tmp = '', t_lst[0]
        cnt = 0
        for txt in t_lst[1:]:
            cnt += 1
            if txt != tmp:
                fix = fix + str(cnt) + tmp if 1 < cnt else fix + tmp
                tmp, cnt = txt, 0
        else:
            fix = fix + str(cnt+1) + tmp if 0 < cnt else fix + tmp
        x = len(fix)
        ans = x if x < ans else ans
    return ans