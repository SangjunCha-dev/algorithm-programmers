## 프린터

분류 : 스택/큐

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42587)

1. 우선순위 `priorities` 리스트의 최댓값을 `num_max`변수에 대입
2. `cursor`변수에 `priorities[0]`값 추출하여 대입
3. `cursor` 값이 최댓값 일때 `cnt` 1증가
4. 이때 `location`값이 0이면 break
5. `cursor` 값이 최댓값 아닐때 리스트 맨뒤에 `cursor` 값 추가
6. 이때 `location`값이 0이면 `location`변수에 `priorities`길이값 대입
7. `location` 1 감소
8. 위의 순서를 `location` 0 이상일때 while문 반복실행

**2020-12-22**

> min TaseCase : 0.00ms, 10MB  
> max TaseCase : 0.99ms, 10.1MB  