def solution(a, b):
    if a < b:
        num_min, num_max = a, b
    elif b < a:
        num_min, num_max = b, a
    else:
        return a
    return (num_max*(num_max+1) // 2) - (num_min*(num_min-1) // 2)