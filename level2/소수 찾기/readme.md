## 소수 찾기

분류 : 완전탐색

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42839)

1. 입력받은 `numbers` 문자열로 만들수 있는 모든 정수형 리스트 `numbers_list` 생성
    - permutations 라이브러리를 사용하여 조합할 수 있는 모든 값 생성
2. `numbers_list` 리스트 중복제거
3. `numbers_list` 리스트를 `prime_number`함수로 소수 판별
    - 숫자 num의 약수는 제곱근(num) 범위에 있다 원리를 이용하여 판별
4. 판별결과를 `answer`변수에 합산하여 반환

**2021-01-09**

> min TaseCase : 0.04ms, 10.4MB  
> max TaseCase : 13.19ms, 10.6MB  