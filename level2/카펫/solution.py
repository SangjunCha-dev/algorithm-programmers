def solution(brown, yellow):
    sqrt = int(yellow**0.5)
    while 0 < sqrt:
        if (yellow%sqrt == 0) and ((yellow/sqrt+2)*(sqrt+2) == brown+yellow):
            return [yellow/sqrt+2, sqrt+2]
        sqrt -= 1