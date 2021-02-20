## 메뉴 리뉴얼

분류 : 2021 KAKAO BLIND RECRUITMENT

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/72411)

### 방법1

1. orders 리스트를 course 갯수별 조합생성
2. 조합내 중복제거한 리스트로 조합리스트 내 요소 카운트
3. 카운트값이 가장 높은 조합 목록을 반환

**2021-02-20**

> min TaseCase : 0.05ms, 10.2MB  
> max TaseCase : 124.96ms, 10.6MB  

### 방법2

1. collections.Counter()
    - 컨테이너에 동일한 값이 몇개인지를 `dictionary`로 반환하는 객체
    - 요소의 갯수가 내림차순으로 출력
2. collections.Counter().most_common(n)
    - 입력된 값의 요소들 중 빈도수(frequency)가 높은 순으로 상위 n개를 리스트 안의 `tuple`로 반환

**2021-02-20**

> min TaseCase : 0.07ms, 10.1MB  
> max TaseCase : 2.11ms, 10.4MB  