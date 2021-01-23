def solution(nums):
    cnt = 0
    nums_list = []

    for i, val1 in enumerate(nums[:-2]):
        for j, val2 in enumerate(nums[i+1:-1], start=i+1):
            for val3 in nums[j+1:]:
                if prime(sum([val1, val2, val3])):
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