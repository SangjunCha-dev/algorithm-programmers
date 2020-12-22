def solution(n, m):
    answer = [1, 1]
    dict1 = prime(n)
    dict2 = prime(m)
    # 최대공약수
    for num in dict1:
        if num in dict2:
            answer[0] *= (num ** min(dict1[num], dict2[num]))
    # 최소공배수
    answer[1] = n * m / answer[0]
    return answer

def prime(num):
    num_dict = {}
    i = 2
    while i <= num:
        if num%i == 0:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1
            num //= i
        else:
            i += 1
    return num_dict