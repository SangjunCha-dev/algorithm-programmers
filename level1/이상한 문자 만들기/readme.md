## 이상한 문자 만들기

분류 : 연습문제

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12930)

1. 문자열 길이만큼 for 반복문 실행
2. `even`변수 초깃값 `True`
3. `s[i]`번째 문자가 ` `이면
    - `answer`변수에 ` `추가하고 `even`변수 `True`값으로 수정
4. `s[i]`번째 문자가 ` `아니면서 `even`값이 `True`경우
    - `answer`변수에 `s[i]`대문자 추가하고 `even`변수 `False`값으로 수정
5. `s[i]`번째 문자가 ` `아니면서 `even`값이 `False`경우
    - `answer`변수에 `s[i]`소문자 추가하고 `even`변수 `True`값으로 수정

**2020-12-22**

> min TaseCase : 0.01ms, 10.1MB  
> max TaseCase : 0.04ms, 10.3MB  