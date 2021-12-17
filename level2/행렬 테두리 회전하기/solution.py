def solution(rows, columns, queries):
    answer = []
    
    data = []
    cnt = 0
    for y in range(rows):
        temp = []
        for x in range(columns):
            cnt += 1
            temp.append(cnt)
        data.append(temp)

    for query in queries:
        pos_temp = []
        for x in range(query[1]-1, query[3]-1): pos_temp.append(data[query[0]-1][x])
        for y in range(query[0]-1, query[2]-1): pos_temp.append(data[y][query[3]-1])
        for x in range(query[3]-1, query[1]-1, -1): pos_temp.append(data[query[2]-1][x])
        for y in range(query[2]-1, query[0]-1, -1): pos_temp.append(data[y][query[1]-1])

        answer.append(min(pos_temp))

        value = pos_temp.pop(-1)
        pos_temp.insert(0, value)

        for x in range(query[1]-1, query[3]-1): data[query[0]-1][x] = pos_temp.pop(0)
        for y in range(query[0]-1, query[2]-1): data[y][query[3]-1] = pos_temp.pop(0)
        for x in range(query[3]-1, query[1]-1, -1): data[query[2]-1][x] = pos_temp.pop(0)
        for y in range(query[2]-1, query[0]-1, -1): data[y][query[1]-1] = pos_temp.pop(0)

    return answer