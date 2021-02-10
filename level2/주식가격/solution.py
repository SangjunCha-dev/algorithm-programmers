def solution(prices):
    ans = []
    for i in range(len(prices)):
        val = prices[i]
        for j in range(i+1, len(prices)):
            if prices[j] < val:
                break
        ans.append(j-i)
    return ans