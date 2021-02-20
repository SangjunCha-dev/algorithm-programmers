## 더 맵게

분류 : 힙(Heap)

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42626)

추가 Test Case

|scoville|K|return|
|---|---|---|
|[0, 0]|1|-1|

### 방법1

`heapq` : 이진 트리기반의 최소 힙 자료구조로 데이터를 정렬되게 저장하는 내장 모듈

1. heapq.heapify(heap)
    - 리스트를 힙으로 변환
2. heapq.heappush(heap, item)
    - heap 리스트에 item 원소추가
    - 이진 트리에 원소를 추가하므로 O(logN)의 시간 복잡도를 가짐
3. heapq.heappop(heap)`
    - heap_lst 최소값을 반환하고 해당 리스트에서 삭제함
    - 이진 트리에서 원소를 삭제하므로 O(logN)의 시간 복잡도를 가짐
4. 힙 삭제없이 최소값 얻기
    - `heap[0]` : list 자료형 인덱스 접근방식으로 삭제없이 값 획득 가능
    - 두번째 최소값은 heappop()함수로 첫번쨰 최소값을 삭제한뒤 heap[0] 접근하여 두번째 최소값을 얻을 수 있음
5. heapq.heappushpop(heap, item)
    - 힙에 item을 푸시한 다음, heap에서 가장 작은 항목 팝하고 반환

**2021-02-20**

> 정확성 테스트  
> min TaseCase : 0.00ms, 10.2MB  
> max TaseCase : 1.02ms, 10.2MB  

> 효율성 테스트  
> min TaseCase : 139.60ms, 15MB  
> max TaseCase : 2098.58ms, 51.9MB  

### 방법2

deque : 스택과 큐를 일반화 한 것

1. append(x)
    - 오른쪽에 x 추가
2. appendleft(x)
    - 왼쪽에 x 추가
3. pop()
    - 오른쪽에서 요소를 제거하고 반환
4. popleft()
    - 왼쪽에서 요소를 제거하고 반환
