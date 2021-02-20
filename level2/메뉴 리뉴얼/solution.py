from itertools import combinations

def solution(orders, course):
    ans = []
    for n in course:
        tot_lst = []
        for order in orders:
            tot_lst.extend(list(combinations(sorted(order), n)))
        tot_lst.sort()
        tot_set = set(tot_lst)
        m = 0
        tmp_lst = []
        for val in tot_set:
            cnt = tot_lst.count(val)
            if 1 < cnt and m < cnt:
                m = cnt
                tmp_lst = [''.join(val)]
            elif m == cnt:
                tmp_lst.append(''.join(val))
        ans.extend(tmp_lst)
    return sorted(ans)