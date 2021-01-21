def solution(arr):
    n_dict = {}
    for n in arr:
        for i, val in euclidean(n).items():
            if (not i in n_dict) or (n_dict[i] < val):
                n_dict[i] = val
    answer = 1
    for i, val in n_dict.items():
        answer *= (i**val)
    return answer

def euclidean(n):
    n_dict = {}
    i = 2
    while 1 < n:
        if not n % i:
            n //= i
            n_dict[i] = n_dict[i] + 1 if i in n_dict else 1
        else:
            i += 1
    return n_dict