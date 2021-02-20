import heapq

def solution(scoville, K):
    ans, size = 0, len(scoville)
    heapq.heapify(scoville)
    n = heapq.heappop(scoville)
    while 1 < size:
        m = heapq.heappop(scoville)
        n = heapq.heappushpop(scoville, n + m * 2)
        ans, size = ans + 1, size - 1
        if K <= n:
            return ans
    return -1