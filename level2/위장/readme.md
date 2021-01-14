## 위장

분류 : 해시

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42578)

추가 Test Case

|clothes(string[][])|Return |
|----               |----   |
|[['a', 'a'], ['b', 'b'], ['c', 'c']]                                                       |7|
|[[1, 'a'], [2, 'a'], [3, 'a'], [1, 'b'], [2, 'b'], [3, 'b'], [1, 'c'], [2, 'c'], [3, 'c']] |63|

1. 테스트 케이스 2번째 예시로 순열 `(3C0 + 3C1) * (3C0 + 3C1) * (3C0 + 3C1) - 1` 조합의 갯수이다.

**2021-01-14**

> min TaseCase : 0.00ms, 10.2MB  
> max TaseCase : 0.02ms, 10.2MB  