from bisect import insort, bisect_left

field = {
    "cpp": 1, "java": 2, "python": 4,
    "backend": 1, "frontend": 2,
    "junior": 1, "senior": 2, 
    "chicken": 1, "pizza": 2,
    "-": 7,
}

mask = {
    "cpp": 6, "java": 5, "python": 3,
    "backend": 6, "frontend": 5,
    "junior": 6, "senior": 5, 
    "chicken": 6, "pizza": 5,
    "-": 0,
}

def solution(info, query):
    answer = []

    i_info = {}
    for v in info:
        v = v.split(' ')
        i_bit = (field[v[0]] << 9) + (field[v[1]] << 6) + (field[v[2]] << 3) + field[v[3]]
        
        if i_bit in i_info:
            data = i_info[i_bit]
        else:
            data = i_info[i_bit] = []
        
        score = int(v[4])
        insort(data, score)

    for v in query:
        v = v.split(' and ')
        v[-1], score = v[-1].split(' ')
        score = int(score)
        q_bit = (mask[v[0]] << 9) + (mask[v[1]] << 6) + (mask[v[2]] << 3) + mask[v[3]]

        cnt = 0
        for i_bit in i_info:
            if not (q_bit & i_bit):
                i_data = i_info[i_bit]
                cnt += len(i_data) - bisect_left(i_data, score)
        answer.append(cnt)
    
    return answer