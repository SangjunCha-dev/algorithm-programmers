data = '0123456789ABCDEF'

def find_digit(n, t, m):
    digit_list = ''
    total_len = t*m
    
    for i in range(total_len):
        digit_list += convert_digit(i, n)

        if total_len < len(digit_list):
            break

    return digit_list

def convert_digit(number, n):
    q, r = divmod(number, n)
    return convert_digit(q, n) + data[r] if q else data[r]

def solution(n, t, m, p):
    digit_list = find_digit(n, t, m)
    answer = digit_list[p-1:t*m:m]

    return answer