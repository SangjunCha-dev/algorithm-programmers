def extra_str(text):
    '''
    유효한 2글자 집합 추출
    '''
    text_list = []
    temp_str = None

    for s in text:
        if s.isalpha():
            if temp_str:
                text_list.append(temp_str + s)
            temp_str = s
        else:
            temp_str = None

    return text_list

def solution(str1, str2):
    answer = 0

    str1 = extra_str(str1.lower())
    str2 = extra_str(str2.lower())

    if (len(str1) == 0) and (len(str2) == 0):
        return 65536

    str1_set = []
    str2_set = []
    union_set = []
    for s in str1:
        try:
            # 같은 값을 가진 경우 교집합에 포함
            i = str2.index(s)
            union_set.append(str2.pop(i))
        except ValueError:
            # 같은 값을 가지지 못한 경우 합집합에 포함
            str1_set.append(s)            
    str2_set = str2

    # 교집합
    intersection_count = len(union_set)
    # 합집합
    union_count = intersection_count + len(str1_set) + len(str2_set)
    
    answer = int(intersection_count/union_count*65536)
    return answer