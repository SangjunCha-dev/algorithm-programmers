def solution(msg):
    answer = []
    dictionary = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4,'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'I': 9,'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14,'O': 15,
        'P': 16, 'Q': 17, 'R': 18, 'S': 19,'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24,'Y': 25,
        'Z': 26,
    }
    dict_number = 27

    w = ''
    length = len(msg)
    for i in range(length):
        s = msg[i]
        w += s

        if i+1 < length:
            c = msg[i+1]

            if w+c in dictionary:
                continue
            else:
                answer.append(dictionary[w])

                dictionary[w+c] = dict_number
                w = ''
                dict_number += 1
        else:
            # 마지막 순서일때
            if w in dictionary:
                answer.append(dictionary[w])
            else:
                answer.append(dictionary[s])

    return answer