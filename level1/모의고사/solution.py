def solution(answers):
    answer = []

    answer_cnt = [0, 0, 0]
    answer_list = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 정답 매칭
    for i in range(len(answers)):
        ans = answers[i]
        if ans == answer_list[0][i%5]: answer_cnt[0] += 1
        if ans == answer_list[1][i%8]: answer_cnt[1] += 1
        if ans == answer_list[2][i%10]: answer_cnt[2] += 1

    # 최다 정답자 추출
    max_cnt = max(answer_cnt)
    for i, cnt in enumerate(answer_cnt):
        if max_cnt == cnt:
            answer.append(i+1)
    
    return answer