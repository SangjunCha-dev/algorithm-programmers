## 단속카메라

분류 : 탐욕법(Greedy)

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42884)

1. routes를 `진입지점 <= 진출지점` 되도록 정렬한다.
2. 저장된 진출지점보다 현재 진입지점이 뒤에 위치할 경우 새로운 단속 카메라 설치한다.
3. 이때 현재 진출지점이 저장된 진출지점보다 앞에 위치할 경우 저장된 진출지점을 재설정한다.

**추가한 테스트**

|routes|return|
|---|---|---|
|[[10,50],[15,20],[40,60]]|2|

**2022-04-03**

> **정확성**  
> min TaseCase : 0.01ms, 10.3MB  
> max TaseCase : 0.03ms, 10.1MB  

> **효율성**  
> min TaseCase : 0.48ms, 10.2MB  
> max TaseCase : 1.07ms, 10.6MB  