def solution(arr1, arr2):
    answer = []
    for m, val1 in enumerate(arr1):
        arr_list = []
        for k in range(len(arr2[0])):
            total = 0
            for n, val2 in enumerate(arr2):
                total += val1[n] * val2[k]
            arr_list.append(total)
        answer.append(arr_list)
    return answer