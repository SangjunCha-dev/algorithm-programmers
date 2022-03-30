## 이중우선순위큐

분류 : 힙(Heap)

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42628)

1. `이중` 우선순위 큐를 사용해야 하므로 heap 자료구조를 2개 선언하여 풀이한다.
    - python은 heap 라이브러리가 최소힙으로 동작한다.

**추가 테스트 케이스**

|operations|result|
|---|---|
|["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]|[6,5]|

**2022-03-30**

> min TaseCase : 0.02ms, 10.4MB  
> max TaseCase : 0.03ms, 10.4MB  