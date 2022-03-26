def solution(n, k, cmd):
    # 초기 설정
    answer_dict = dict()
    for i in range(n):
        answer_dict[i] = [i-1, i+1]
    answer_dict[0][0] = None
    answer_dict[n-1][1] = None

    stack_del = list()

    for c in cmd:
        if c[0] == "U":  # Up
            move = int(c[2:])

            while move != 0:
                k = answer_dict[k][0]
                move -= 1

        elif c[0] == "D":  # Down
            move = int(c[2:])

            while move != 0:
                k = answer_dict[k][1]
                move -= 1

        elif c[0] == "C":  # 삭제
            stack_del.append([k, answer_dict[k]])

            front = answer_dict[k][0]
            back = answer_dict[k][1]

            if front != None:
                answer_dict[front][1] = back
            if back != None:
                answer_dict[back][0] = front

            k = back if back != None else front

        elif c[0] == "Z":  # 복구
            recovery = stack_del.pop()
            answer_dict[recovery[0]] = recovery[1]

            key = recovery[0]
            front = recovery[1][0]
            back = recovery[1][1]

            if front != None:
                answer_dict[front][1] = key
            if back != None:
                answer_dict[back][0] = key

    # 정답
    answer = ['O' for _ in range(n)]
    for key, _ in stack_del:
        answer[key] = 'X'
    answer = ''.join(answer)

    return answer