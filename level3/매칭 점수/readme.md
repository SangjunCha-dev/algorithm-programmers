## 매칭 점수

분류 : 정규식

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42893)

1. `pages`에서 찾을 수 있는 데이터를 추출한다.
    - `<body>데이터</body>` 태그내 데이터를 추출한다.
    - 추출한 데이터에서 `<a ... /a>` 형식의 외부링크를 삭제한다.
    - 추출한 데이터에서 특수문자, 숫자 등을 공백문자 2개로 치환한다.
    - word를 매칭할때 앞뒤 문자가 공백이어야만 매칭한다.
    - `<meta property="og:url" content="https://페이지링크"/>` 태그에서 페이지 링크를 추출한다.
    - `<a href="https://외부링크></a>`의 외부 링크 목록을 추출한다.
    - 추출하고 매칭한 데이터를 `data` 딕셔너리에 저장한다.
2. `data`에서 링크점수를 계산한다.
3. `data`에서 기본점수와 링크점수를 합산하여 최고점수 페이지의 가장 작은 `index`값을 반환한다.

**추가한 테스트**

|word|pages|return|
|---|---|---|
|"Muzi"|['<meta property=\"og:url\" content=\"https://a.com\"/> <body> muzi </body>', '<meta property=\"og:url\" content=\"https://b.com\"/> <body> 0muzi0muzi0 </body>']|1|

**2022-06-18**

> min TaseCase : 0.13ms, 10.3MB  
> max TaseCase : 1.28ms, 10.3MB  