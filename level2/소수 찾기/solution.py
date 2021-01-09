from itertools import permutations

def solution(numbers):
    answer = 0
    numbers_list = []

    # 모든 정수형 리스트 만들기
    for i in range(1, len(numbers)+1):
        num_list = list(permutations(list(numbers), i))

        for num in num_list:
            numbers_list.append(int(''.join(list(num))))

    # 중복제거
    numbers_list = list(set(map(int, numbers_list)))
    
    # 소수 판별후 갯수 체크
    for n in numbers_list:
        if prime_number(n):
            answer += 1
    
    return answer

def prime_number(n):
    if n == 2:
        return True
    elif (n % 2 == 0) or (n < 2):
        return False

    sqrt = int(n**0.5)+1
    for i in range(3,sqrt+1,2):
        if n % i == 0:
            return False
    return True