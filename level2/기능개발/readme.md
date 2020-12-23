## 기능개발

분류 : 스택/큐

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42586)

### 방법1

1. `progresses[0]+(speeds[0]*i)` 값이 100 이상 될 수 있는 `i`값을 `num`변수에 대입 후 for 문 break
2. `progresses`리스트 원소마다 `speeds[i]`*`num` 값 덧셈
3. 최대 `progresses`리스트 길이만큼 반복하여 `progresses[0]` 원소를 비교하는 for 문 실행
    - 해당 원소가 100 이상일 때 `cnt` 1증가 및 `progresses[0]`, `speeds[0]` 삭제,
    - 해당 원소가 100미만일 때 break
4. `cnt`변수값을 `answer`리스트에 추가
5. 위의 과정을 `progresses`리스트 값이 있다면 while 문 반복 실행

**2020-12-23**

> min TaseCase : 0.01ms, 10.2MB  
> max TaseCase : 0.12ms, 10.1MB  
