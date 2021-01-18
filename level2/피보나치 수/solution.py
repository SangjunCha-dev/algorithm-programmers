def solution(n):
    num_list = [0, 1] + [0] * (n-1)
    for i in range(2, len(num_list[2:])+2):
        num_list[i] = num_list[i-2] + num_list[i-1]
    return num_list[-1]%1234567 if n else 0