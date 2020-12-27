def solution(w,h):
    v_gcd = f_gcd(max(w,h), min(w,h))
    
    line_pixel = ((w+h)/v_gcd-1) * v_gcd
    return w*h-int(line_pixel)

def f_gcd(n_max, n_min):
    while n_min != 0:
       t = n_max % n_min
       (n_max, n_min) = (n_min, t)
    return abs(n_max)