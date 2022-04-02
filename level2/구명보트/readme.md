## 구명보트

분류 : 탐욕법(Greedy)

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42885)

1. people list를 `작은 몸무게 순으로 정렬`한다.
2. 가장 작은 몸무게와 가장 큰 몸무게만 사용하므로 `deque 자료형`을 사용한다.
3. 가장 작은 값과 큰 값을 합쳤을때 limit 이내이면 같이 탈출 아니면 가장 큰값만 탈출시킨다. 

**2022-04-02**

> 정확성  
> min TaseCase : 0.03ms, 10.4MB  
> max TaseCase : 1.24ms, 10.2MB  

> 효율성  
> min TaseCase : 9.15ms, 10.7MB  
> max TaseCase : 9.82ms, 10.7MB  