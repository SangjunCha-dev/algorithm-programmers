## 다리를 지나는 트럭

분류 : 스택/큐

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42583)

변수 정의
- bridge_length : 다리길이
- weight : 다리 설계하중
- truck_weights : 다리를 건널 트럭의 무게(값)와 순서(index)
- answer : 경과한 시간
- bredge_list : 다리를 건너는 중인 트럭의 목록과 위치 ex) [[트럭 무게, 트럭 위치], [트럭 무게, 트럭 위치], ...]
- cnt : 한 번에 이동할 거리

1. `bredge_list`리스트 값이 있을 때
    - `bredge_list[0][1]`값이 `bridge_length`보다 크다면
        - `weight`값에 `bredge_list[0][0]`값 추가
        - 첫 번째 트럭이 다리를 다 지나갔다면 다리가 견딜 수 있는 하중을 복구
        - `bredge_list[0]`삭제
        - 리스트에서 첫 번째 트럭 정보 삭제
2. `truck_weights`리스트 값이 있을 때
    - `truck_weights[0]`값(첫 번째 트럭)을 `truck`변수에 저장
    - `weight` - `truck`값이 0 이상 일 때
        - `weight`값에서 `truck`만큼 뺄셈
        - 견딜 수 있는 다리 하중 줄어듦
        - `bredge_list`리스트에 `[truck, 1]`값 추가
        - 다리를 건너는 중인 트럭 정보 추가 `무게`와 `위치`
        - `truck_weights[0]` 삭제
        - 진입 대기 중인 트럭 목록에서 첫 번째 트럭 정보 삭제
    - 다리에 트럭이 추가로 진입할 수 없을 때
        - `bredge_list[0][1]`값이 `bridge_length`보다 크기 위한 `cnt`값 구하기
        - 다리에 진입한 맨 앞의 트럭이 다리를 건너기 위해 덧셈할 값
3. `bredge_list`리스트의 트럭 위치값에 `cnt`값 덧셈
    - 다리에 진입한 트럭들의 위치 이동
4. `answer`값에 `cnt`값 덧셈
    - 다리에서 이동한 거리만큼 시간이 경과하였기에 `cnt`값으로 덧셈
5. `bredge_list`, `truck_weights` 둘 중 하나라도 값이 있으면 while 반복 실행

**2020-12-23**

> min TaseCase : 0.02ms, 10.3MB  
> max TaseCase : 27.21ms, 10.3MB  