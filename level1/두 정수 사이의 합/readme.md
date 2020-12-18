## 두 정수 사이의 합

분류 : 연습문제

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12912)

1. 입력값 `a`, `b` 중 작은 값을 `num_min`변수에 큰 값을 `num_max`변수에 대입
2. 값이 같으면 `a` 반환
3. 가우스의 덧셈 공식을 이용하여 각 `num_min-1`, `num_max` 변수까지의 합을 구한다.
    - 자연수 1부터 N까지의 합 = N(N+1)/2
4. (큰 값 - 작은 값) 값 반환

**2020-12-18**

> min TaseCase : 0.00ms, 10MB  
> max TaseCase : 0.00ms, 10.3MB  

```
(abs(a-b)+1)*(a+b)//2
```
위의 공식을 사용하면 한줄로 코드 작성 가능하다.
