## 순위 검색

분류 : 2021 KAKAO BLIND RECRUITMENT

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/72412#)

### 방법1

풀이방법 : 재귀함수, 이진탐색 사용

**2021-05-18**

> 정확성 테스트  
> min TaseCase : 0.24ms, 10.4MB  
> max TaseCase : 10.82ms, 10.7MB  

> 효율성 테스트  
> min TaseCase : 1146.27ms, 35.9MB  
> max TaseCase : 5534.78ms, 36.2MB  

### 방법2

풀이방법 : Bit field 연산, 이진탐색 알고리즘 수정

**2021-05-18**

> 정확성 테스트  
> min TaseCase : 0.11ms, 10.4MB  
> max TaseCase : 9.42ms, 11MB  

> 효율성 테스트  
> min TaseCase : 887.34ms, 35.8MB  
> max TaseCase : 3955.15ms, 35.9MB  

### 방법3

풀이방법 : 이진탐색 부분을 내장함수 사용  

- 배열 이진 분할 알고리즘 bisect 라이브러리
- `insort(a, x)` : a에 x를 정렬된 순서로 추가
- `bisect_left(a, x)` : 정렬된 순서를 유지하면서 a에 x를 추가할 위치 반환 

**2021-05-18**

> 정확성 테스트  
> min TaseCase : 0.09ms, 10.4MB  
> max TaseCase : 5.63ms, 10.7MB  

> 효율성 테스트  
> min TaseCase : 446.87ms, 35.7MB  
> max TaseCase : 1198.31ms, 35.9MB  