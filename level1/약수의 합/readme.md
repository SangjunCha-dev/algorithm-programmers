## 약수의 합

분류 : 연습문제

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12928)

1. `i`변수 초깃값 `1`
2. `quot`변수에 `n/i`몫을 대입
3. `quot`변수가 정수형 일 때 검증 시작
4. `quot`변수가 `i`보다 작을 경우 약수 집합의 중간지점을 지났기에 while 반복문 종료
5. `quot`변수가 `i`와 같지 않을 때 (`quot` + `i`) 값을 `answer`변수에 덧셈
6. `quot`변수가 `i`와 같을 때 `i`값을 `answer`변수에 덧셈
7. `i`변수에 1 덧셈
8. `i`값이 `quot`값보다 크면 while 반복문 종료

**2020-12-22**

> min TaseCase : 0.00ms, 10.1MB  
> max TaseCase : 0.02ms, 10.2MB  