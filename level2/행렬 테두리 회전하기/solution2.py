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

    for y1, x1, y2, x2 in queries:
        pos_temp = []

        pos_temp.extend(data[y1-1][x1-1:x2-1]) 
        for y in range(y1-1, y2-1): pos_temp.append(data[y][x2-1])
        pos_temp.extend(data[y2-1][x2-1:x1-1:-1]) 
        for y in range(y2-1, y1-1, -1): pos_temp.append(data[y][x1-1])

        answer.append(min(pos_temp))

        value = pos_temp.pop(-1)
        pos_temp.insert(0, value)

        data[y1-1][x1-1:x2-1] = pos_temp[:x2-x1]
        del pos_temp[:x2-x1]
        for y in range(y1-1, y2-1): data[y][x2-1] = pos_temp.pop(0)
        data[y2-1][x2-1:x1-1:-1] = pos_temp[:x2-x1]
        del pos_temp[:x2-x1]
        for y in range(y2-1, y1-1, -1): data[y][x1-1] = pos_temp.pop(0)

    return answer