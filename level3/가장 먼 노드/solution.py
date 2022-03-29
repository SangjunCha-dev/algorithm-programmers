import heapq

def dijkstra(start, distance, graph):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solution(n, edge):
    answer = 0
    start = 1
    INF = int(1e9)

    graph = [[] for _ in range(n+1)]
    distance = [INF for _ in range(n+1)]
    
    for i, j in edge:
        graph[i].append((j, 1))
        graph[j].append((i, 1))

    dijkstra(start, distance, graph)

    distance_list = []
    for i in range(1, n+1):
        if distance[i] == INF: continue
        distance_list.append(distance[i])

    answer = distance_list.count(max(distance_list))

    return answer