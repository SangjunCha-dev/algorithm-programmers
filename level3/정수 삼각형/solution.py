import copy

def solution(triangle):
    n = len(triangle)
    dp = [0 for _ in range(len(triangle[-1]))]

    for i in range(n):
        array = copy.deepcopy(dp)
        for j, k in enumerate(triangle[i]):
            if j == 0:
                dp[j] += k
                continue

            dp[j] = max(array[j], array[j-1]) + k

    return max(dp)