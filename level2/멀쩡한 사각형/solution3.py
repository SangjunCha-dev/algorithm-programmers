import math

def solution(w,h):
    gcd = math.gcd(w,h)
    
    line_pixel = ((w+h)/gcd-1) * gcd
    return w*h-int(line_pixel)