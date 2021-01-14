def solution(clothes):
    clothes_dict = {}
    # 카테고리명과 해당 카테고리 갯수 추출
    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 1
    # 조합 연산
    answer = 1
    for cloth in clothes_dict.values():
        answer *= cloth+1
    return answer-1