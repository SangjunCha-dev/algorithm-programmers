def solution(board, moves):
    answer = 0
    queue = []

    for i in moves:
        i -= 1
        for row in board:
            if row[i]:
                queue.append(row[i])
                row[i] = 0
                break
        if (1 < len(queue)) and (queue[-2] == queue[-1]):
            answer += 2
            queue.pop()
            queue.pop()
    
    return answer