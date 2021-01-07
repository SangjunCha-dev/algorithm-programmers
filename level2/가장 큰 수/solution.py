import math

def solution(numbers):
    numbers.sort(key=lambda x: (int(str(x)+(str(x)[0]*(4-int(math.log10(x)+1 if x else 0)))), x%10), reverse=True)
    return ''.join(map(str, numbers)) if numbers[0] != 0 else '0'