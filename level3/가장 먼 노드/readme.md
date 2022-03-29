## 가장 먼 노드

분류 : 그래프

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/49189)

1. 우선순위 큐를 적용한 다익스트라 최단 거리 알고리즘을 사용한다.
2. 다익스트라 알고리즘은 간선의 방향성을 체크하므로 무방향성을 위해 입력받은 vertex 연결 정보를 양방향으로 만들고 진행한다.

**2022-03-29**

> min TaseCase : 0.03ms, 10.2MB  
> max TaseCase : 120.05ms, 27.2MB  