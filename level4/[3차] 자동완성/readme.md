## [3차] 자동완성

분류 : 2018 KAKAO BLIND RECRUITMENT

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/17685)

1. 아래와 같은 문자열 값이 주어졌을때 convert_words 함수로 문자의 위치에 따른 문자 갯수와 다음순서의 문자의 딕셔너리 자료형을 저장한다.
    - 입력값
        ```
        go
        gone
        guild
        ```
    - 변환값
        ```json
        {
        "g": {
            "count": 3,
            "o": {
            "count": 2,
            "n": {
                "count": 1,
                "e": {
                "count": 1
                }
            }
            },
            "u": {
            "count": 1,
            "i": {
                "count": 1,
                "l": {
                "count": 1,
                "d": {
                    "count": 1
                }
                }
            }
            }
        }
        }
        ```

2. 변환된 자료형에서 count_word 함수로 count값이 모두 더한다. 이때 count값이 1인 경우 다음 문자를 탐색하지 않고 반환한다.

풀이시간 : 37분

**2022-05-07**

> min TaseCase : 0.01ms, 10MB  
> max TaseCase : 751.77ms, 183MB  