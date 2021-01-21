## 행렬의 곱셈

분류 : 연습문제

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/12949)

|변수명|형식|크기|
|---|---|---|
|arr1|2차원리스트|m * k|
|arr2|2차원리스트|k * n|
|answer|2차원리스트|m * n|

list 자료형 for문 반복문에서 사용할때 일반적인 속도순서(위부터 빠름)
- for val in list:  
- for i in range(len(list)):  
- for i, val in enumerate(list):  

list 자료형 for문 반복문에서 사용할때 list 인젝싱포함될경우 속도순서(list 200개 이상)
- for i, val in enumerate(list): 
    - val 
- for i in range(len(list)): 
    - list[i]

### 방법1

**2021-01-21**

> min TaseCase : 0.56ms, 10.3MB  
> max TaseCase : 52.38ms, 11MB  

### 방법2

**2021-01-21**

> min TaseCase : 0.76ms, 10.3MB  
> max TaseCase : 78.02ms, 11.2MB  