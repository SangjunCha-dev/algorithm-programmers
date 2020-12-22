def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        else:
            str_ascii = ord(s[i])
            large = True if str_ascii <= 90 else False
            str_ascii += n
            if (90 < str_ascii) and (large):
                str_ascii -= 26
            elif 122 < str_ascii:
                str_ascii -= 26
            answer += chr(str_ascii)
    return answer