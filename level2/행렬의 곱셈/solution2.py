def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for m, val1 in enumerate(arr1):
        for k in range(len(arr2[0])):
            for n, val2 in enumerate(arr2):
                answer[m][k] += val1[n] * val2[k]
    return answer