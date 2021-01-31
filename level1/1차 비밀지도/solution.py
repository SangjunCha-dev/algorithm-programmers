def solution(n, arr1, arr2):
    answer = [[' ' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        val1 = str(bin(arr1[i]))[2:]
        val2 = str(bin(arr2[i]))[2:]
        while len(val1) < n:
            val1 = '0' + val1
        while len(val2) < n:
            val2 = '0' + val2

        for j in range(n):
            if val1[j] == '1' or val2[j] == '1':
                answer[i][j] = '#'
    
    return [''.join(answer[i]) for i in range(n)]