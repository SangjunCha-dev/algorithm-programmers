def solution(n):
    p_lst = [False, False, True] + [True, False] * (n//2-1)
    p_lst = p_lst if n%2 == 0 else p_lst + [True]
    for i in range(3, int(n**0.5)+1, 2):
        if not p_lst[i]:
            continue
        for j in range(i*2, n+1, i):
            p_lst[j] = False
    return p_lst.count(True)