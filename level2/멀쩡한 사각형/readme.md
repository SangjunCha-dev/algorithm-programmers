## 멀쩡한 사각형

분류 : Summer/Winter Coding(2019)

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/62048)

### 방법1

1. `h`값이 정수로 나오기위한 최소 `w`값을 구하기 위해 최대공약수를 `gcd`변수에 대입
2. 이때 색칠된 픽셀의 갯수는 `w+h-1`개
3. `w+h-1` 곱하기 `gcd`값이 색칠된 사각형 갯수 `line_pixel`변수에 대입
4. 반환값은 사각형의 면적인 `w*h`에서 `line_pixel`값을 뺄셈하여 반환 

**2020-12-24**

> min TaseCase : 0.01ms, 10MB  
> max TaseCase : 6345.39ms, 10.1MB  

### 방법2

1. `h`값이 정수로 나오기위한 정수 최소 `w`값을 구하기 위해 최대공약수 구하기 
- 유클리드 호제법 공식으로 최대공약수 구하여 `v_gcd` 변수에 대입
2. 이때 색칠된 픽셀의 갯수는 `w+h-1`개
3. `w+h-1` 곱하기 `gcd`값이 색칠된 사각형 갯수 `line_pixel`변수에 대입
4. 반환값은 사각형의 면적인 `w*h`에서 `line_pixel`값을 뺄셈하여 반환 

**2020-12-27**

> min TaseCase : 0.01ms, 10.1MB  
> max TaseCase : 0.01ms, 10.3MB  

### 방법3

1. `h`값이 정수로 나오기위한 정수 최소 `w`값을 구하기 위해 최대공약수 구하기
- math 라이브러리의 gcd 함수로 구하고 `gcd`변수에 대입
2. 이때 색칠된 픽셀의 갯수는 `w+h-1`개
3. `w+h-1` 곱하기 `gcd`값이 색칠된 사각형 갯수 `line_pixel`변수에 대입
4. 반환값은 사각형의 면적인 `w*h`에서 `line_pixel`값을 뺄셈하여 반환 

**2020-12-24**

> min TaseCase : 0.00ms, 10.3MB  
> max TaseCase : 0.01ms, 10.3MB  