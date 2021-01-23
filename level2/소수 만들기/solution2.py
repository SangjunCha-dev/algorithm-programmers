from itertools import combinations

def solution(nums):
    cnt = 0
    for n_list in combinations(nums, 3):
        if prime(sum(n_list)):
            cnt += 1
    return cnt

def prime(n):
    if n == 2:
        return True
    elif (n % 2 == 0) or (n < 2):
        return False

    sqrt = int(n**0.5)+1
    for i in range(3,sqrt+1,2):
        if n % i == 0:
            return False
    return True