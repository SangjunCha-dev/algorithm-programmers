## 나누어 떨어지는 숫자 배열

분류 : 연습문제

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12910)

### 방법1

1. `arr` 리스트에 원소를 `divisor`나머지 연산하여 값이 없을 때 `answer`리스트에 추가
    - 조건문에 `==` 사용할 경우 `3.44ms`
    - 조건문에 `not` 사용할 경우 `2.64ms`
2. `answer`리스트에 값이 있으면 `정렬`하여 반환하고 없으면 `[-1]` 반환

**2020-12-18**

> min TaseCase : 0.00ms, 10.1MB  
> max TaseCase : 2.64ms, 13.3MB  

**2021-02-02**

> min TaseCase : 0.00ms, 10.2MB  
> max TaseCase : 2.92ms, 13.4MB  