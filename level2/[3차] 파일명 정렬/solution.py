def solution(files):
    file_list = []
    for filename in files:
        head, number = '', ''
        is_digit = False
        # head, number, tail 추출
        for s in filename:
            if s.isdigit():  # number
                number += s
                is_digit = True
            elif is_digit:  # tail
                break
            else:  # head
                head += s

        head = head.lower()
        number = int(number)

        # head, number, originname 저장
        file_list.append([head, number, filename])

    # head, number 순으로 정렬
    file_list.sort(key=lambda x: (x[0], x[1]))
    answer = [x[2] for x in file_list]

    return answer