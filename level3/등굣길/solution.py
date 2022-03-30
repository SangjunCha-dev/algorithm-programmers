def solution(m, n, puddles):
    INF = int(1e9)

    dp = [[[INF,0] for _ in range(m)] for _ in range(n)]

    # puddles 위치 indexr에 맞도록 수정 (입력값 위치(x, y) 주의!)
    puddles = [[puddle[0]-1, puddle[1]-1] for puddle in puddles]

    for h in range(n):
        for w in range(m):           

            # 침수 지역일 경우 다음 단계로
            if [h,w] in puddles:
                continue

            if 0 <= h-1 < n:
                value_y = dp[h-1][w][0]+1
            else:
                value_y = INF

            if 0 <= w-1 < m:
                value_x = dp[h][w-1][0]+1
            else:
                value_x = INF
            
            # 최단 경로의 개수
            if value_y < value_x:
                value = value_y
                count = dp[h-1][w][1]
            elif value_x < value_y:
                value = value_x
                count = dp[h][w-1][1]
            else:
                value = value_y
                count = dp[h-1][w][1] + dp[h][w-1][1]

            # 처음위치일 경우
            if (value_x is INF) and (value_y is INF):
                value = 0
                count = 1

            dp[h][w] = [value, count]

    return dp[n-1][m-1][1] % 1000000007