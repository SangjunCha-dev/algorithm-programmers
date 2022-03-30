## 등굣길

분류 : 동적계획법(Dynamic Programming)

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42898)

### 방법1

1. 동적계획법 방식으로 문제풀이
2. 아래 풀이는 문제에서 요구한 최단경로의 갯수만 연산하는 최적화가 필요함

**2022-03-30**

> **정확성**  
> min TaseCase : 0.01ms, 10.3MB  
> max TaseCase : 0.21ms, 10.2MB  
>   
> **효율성**  
> min TaseCase : 2.56ms, 10.3MB  
> max TaseCase : 7.37ms, 10.9MB  

### 방법2

1. 오른쪽, 아래로만 이동가능하므로 무조건 최단경로를 만족하게됨
2. 최단경로 계산이 아닌 갈수 있는 경우의 수 연산으로 수정하면 최적화 가능