def solution(n, lost, reserve):
    answer = 0

    lost_2 = list(set(lost)-set(reserve))
    reserve_2 = list(set(reserve)-set(lost))
    lost, reserve = lost_2, reserve_2
    
    l_len, r_len = len(lost) - 1, len(reserve) - 1
    lost.sort()
    reserve.sort()

    while 0 <= l_len and 0 <= r_len:
        if reserve[r_len] - 1 <= lost[l_len] <= reserve[r_len] + 1:
            del lost[l_len], reserve[r_len]
            l_len -= 1
            r_len -= 1
        elif lost[l_len] > reserve[r_len] + 1:
            l_len -= 1
        elif lost[l_len] < reserve[r_len] - 1:
            r_len -= 1

    answer = n - len(lost)

    return answer