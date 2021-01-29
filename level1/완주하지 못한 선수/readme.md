## 완주하지 못한 선수

분류 : 해시

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42576)

### 방법1

1. 두개의 리스트 정렬 후 순서대로 비교하여 다른 문자열일때 해당 participant 리스트의 문자열 반환

**2021-01-29**

> 정확성 테스트  
> min TaseCase : 0.01ms, 10.1MB  
> max TaseCase : 0.65ms, 10.3MB  

> 효율성 테스트  
> min TaseCase : 36.78ms, 18MB  
> max TaseCase : 86.29ms, 26.3MB  

### 방법2

zip(*iterable) : 두개이상의 자료형을 묶어주는 함수

**2021-01-29**

> 정확성 테스트  
> min TaseCase : 0.01ms, 10.2MB  
> max TaseCase : 0.63ms, 10.4MB  

> 효율성 테스트  
> min TaseCase : 36.12ms, 18.1MB  
> max TaseCase : 82.59ms, 26.3MB  