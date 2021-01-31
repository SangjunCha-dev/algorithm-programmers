def solution(numbers, hand):
    answer = ''
    l_pos, r_pos, n_pos = [0, 0], [0, 0], [0, 0]
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            l_pos = [3-n//3, 0]
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            r_pos = [4-n//3, 0]
        else:
            n_pos = [3-n//3, 1] if n != 0 else [0, 1]
            
            l_val = abs(n_pos[0] - l_pos[0]) + abs(n_pos[1] - l_pos[1])
            r_val = abs(n_pos[0] - r_pos[0]) + abs(n_pos[1] - r_pos[1])
            
            if l_val < r_val:
                l_pos = n_pos
                answer += 'L'
            elif r_val < l_val:
                r_pos = n_pos
                answer += 'R'
            elif hand == 'left':
                l_pos = n_pos
                answer += 'L'
            else:
                r_pos = n_pos
                answer += 'R'
    return answer