from itertools import combinations
from collections import Counter

def solution(orders, course):
    ans = []
    for n in course:
        tot_lst = []
        for order in orders:
            tot_lst.extend(combinations(sorted(order), n))

        order_sorted = Counter(tot_lst).most_common()
        cnt_max = order_sorted[0][1]
        for arr, cnt in order_sorted:
            if 1 < cnt and cnt == cnt_max:
                ans += [''.join(arr)]
            else:
                break
    return sorted(ans)