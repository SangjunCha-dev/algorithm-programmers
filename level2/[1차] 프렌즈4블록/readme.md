## [1차] 프렌즈4블록

분류 : 2018 KAKAO BLIND RECRUITMENT

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/17679)

1. 2x2크기의 블럭이 동일한 문자로 구성되어있다면 해당 위치들을 `is_equal_list`에 저장한다.
2. `is_equal_list`에서 True 값을 찾아 board에서 동일한 위치 값을 공백값으로 덮어쓴다.
    - 공백값으로 바꾼 횟수의 합을 마지막에 반환한다.
3. 해당 블럭의 아래 블럭이 공백이면 값이 나오기 전까지 아래쪽으로 블럭값을 이동시킨다.
4. 1~3과정에서 제거된 블럭이 있으면 while문을 반복하고 없다면 종료한다.

**2022-04-19**

풀이시간 : 96분

> min TaseCase : 0.03ms, 10.5MB  
> max TaseCase : 113.78ms, 10.3MB  