## 조이스틱

분류 : 탐욕법(Greedy)

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42860)

변수 정의
- move_cnt : 조이스틱이 움직인 횟수
- text_len : 입력받은 문자열 길이
- alphabet : 조이스틱 위아래 움직인 횟수에 따른 알파벳 문자목록
- tf_list : 문자 'A'를 제외한 다른문자 여부목록
- distance_r : 기준위치 오른쪽으로 `True` 까지의 거리
- distance_l : 기준위치 왼쪽으로 `True` 까지의 거리

1. 필요한 변수 선언 및 초기화
2. 문자열 길이만큼 for 반복문을 실행
    - alphabet리스트에서 `name[i]`값의 위치를 `index`변수에 대입
    - `B~N`까지는 조이스틱 위로 이동한것으로 `index` + `move_cnt`값을 `move_cnt`변수에 대입
    - `Z~O`까지는 조이스틱 아래로 이동한것으로 `index-13` + `move_cnt`값을 `move_cnt`변수에 대입
    - 해당 문자로 변환하기까지의 조이스틱 움직인 횟수를 구함
3. `tf_list`리스트에서 `True`값이 있을때만 while 반복문 실행
    - 1부터 `text_len`까지 반복하여 `tf_list[(i+j)%text_len]`값에 `True`값 나올때까지 `distance_r`변수 1증가
        - 기준위치 오른쪽으로 `True`값 까지의 거리
    - 1부터 `text_len`까지 반복하여 `tf_list[(i-j)%text_len]`값에 `True`값 나올때까지 `distance_l`변수 1증가
        - 기준위치 왼쪽으로 `True`값 까지의 거리
    - `distance_l`값보다 `distance_r`값이 클때 `(i-1)%text_len`값을 `i`변수에 대입
        - 기준위치 왼쪽으로 1이동
    - `distance_l`값보다 `distance_r`값이 작거나 같을때 `(i+1)%text_len`값을 `i`변수에 대입
        - 기준위치 오른쪽으로 1이동
    - 거리 확인한 `tf_list[i]`값은 `False`값 대입하고 `move_cnt`변수 1증가

**2020-12-28**

> min TaseCase : 0.01ms, 10.1MB  
> max TaseCase : 0.03ms, 10.3MB  