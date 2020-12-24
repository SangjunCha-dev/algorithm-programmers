def solution(w,h):
    gcd = 1
    
    dict1 = prime(w)
    dict2 = prime(h)
    # 최대공약수
    for num in dict1:
        if num in dict2:
            gcd *= (num ** min(dict1[num], dict2[num]))
    
    line_pixel = ((w+h)/gcd-1) * gcd
    return w*h-int(line_pixel)

def prime(num):
    num_dict = {}
    i = 2
    while i <= num:
        if num%i == 0:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1
            num //= i
        else:
            i += 1
    return num_dict