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

def binary_search(data, target):
    low = 0
    high = len(data)

    while low < high:
        mid = (high+low)//2
        if target <= data[mid]:
            high = mid
        else:
            low = mid + 1
    return low

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
        data.insert(binary_search(data=data, target=score), score)

    for v in query:
        v = v.split(' and ')
        v[-1], score = v[-1].split(' ')
        score = int(score)
        q_bit = (mask[v[0]] << 9) + (mask[v[1]] << 6) + (mask[v[2]] << 3) + mask[v[3]]

        cnt = 0
        for i_bit in i_info:
            if not (q_bit & i_bit):
                i_data = i_info[i_bit]
                cnt += len(i_data) - binary_search(data=i_data, target=score)
        answer.append(cnt)
    
    return answer