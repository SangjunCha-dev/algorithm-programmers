import re
p1 = re.compile(r'\d{1,2}')
p2 = re.compile(r'[SDT][*|#]?')

def solution(dartResult):
    answer = []
    arr1, arr2 = re.findall(p1, dartResult), re.findall(p2, dartResult)
    for i in range(len(arr1)):
        squ = 2 if arr2[i][0] == 'D' else 3 if arr2[i][0] == 'T' else 1
        mul = 2 if arr2[i][-1] == '*' else -1 if arr2[i][-1] == '#' else 1
        answer.append((int(arr1[i]) ** squ) * mul)
        if 1 < len(answer) and arr2[i][-1] == '*':
            answer[i-1] *= 2
    return sum(answer)