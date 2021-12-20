def solution(lottos, win_nums):
    win_cnt, zero_cnt = 0, 0
    for lotto in lottos:
        if lotto in win_nums:
            win_cnt += 1
        elif not lotto:
            zero_cnt += 1

    max_rank = 7-(win_cnt+zero_cnt) if 1 < (win_cnt+zero_cnt) else 6
    min_rank = 7-win_cnt if 1 < win_cnt else 6

    answer = [max_rank, min_rank]
    return answer