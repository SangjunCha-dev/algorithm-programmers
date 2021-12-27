## 다단계 칫솔 판매

분류 : 2021 Dev-Matching: 웹 백엔드 개발자(상반기)

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/77486)

### 방법1

**2021-12-20**

> min TaseCase : 0.08ms, 10.2MB  
> max TaseCase : 167.55ms, 22.2MB  

### 방법2

1. 동일한 index에 접근하는 두개의 리스트는 zip함수로 묶어서 동시에 처리한다.
2. 원하는 값을 바로 반환할수 있게 dict자료형을 2개로 분할한다.
3. while문 동작을 do-while문처럼 동작시킨다.

**2021-12-27**

> min TaseCase : 0.01ms, 10.3MB  
> max TaseCase : 92.37ms, 21.2MB  