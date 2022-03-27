## 거리두기 확인하기

분류 : 2021 카카오 채용연계형 인턴십

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/81302)

- 맨해튼 거리: 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, 맨해튼 거리는 |r1 - r2| + |c1 - c2| 이다.

**추가 테스트 케이스**

```python
places = [
    [
        "OOOXP",
        "OOOPO",
        "OOOOO",
        "OOOOO",
        "OOOOO",
    ],
    [
        "OOOOP",
        "OOOPX",
        "OOOOO",
        "OOOOO",
        "OOOOO",
    ]
]

result = [0, 0]
```

풀이방법 : 맨해튼 거리를 활용하여 대각선위치를 검증한다.

**2022-03-27**

> min TaseCase : 0.01ms, 10.2MB  
> max TaseCase : 0.05ms, 10.3MB  