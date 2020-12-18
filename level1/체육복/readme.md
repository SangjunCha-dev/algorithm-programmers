## 체육복

분류 - 탐욕법(Greedy)

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42862)

1. `reserve` 리스트에서 `lost` 리스트와 같은 원소를 삭제
    - 먼저 여분의 체육복을 가진 사람이 도난당한 경우를 고려
2. set함수로 정렬이 되지 않았으므로 `sort()` 정렬
3. `lost[l_len]` 원소 값 -1, +1 값이 `reserve[r_len]` 리스트에 있으면 두 원소를 삭제하고 `l_len`, `r_len` 값 -1
    - 도난당한 사람에 맞는 여유분 체육복 있음
4. `lost[l_len]` 원소 값이 `reserve[r_len]`보다 클 경우 `l_len`값 -1
    - 도난당한 사람에 맞는 여유분 체육복 없음
5. `lost[l_len]` 원소 값이 `reserve[r_len]`보다 작을 경우 `r_len`값 -1
    - 여유분 체육복에 맞는 도난당한 사람이 없음
6. 최종적으로 `lost`리스트의 길이 값을 반환
    - 체육복을 빌리지 못한 사람

**2020-12-18**

> min TaseCase : 0.01ms, 10.2MB  
> max TaseCase : 0.02ms, 10.3MB  