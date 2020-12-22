def solution(s):
    answer = ''
    even = True
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            even = True
        elif even:
            answer += s[i].upper()
            even = False
        else:
            answer += s[i].lower()
            even = True
    return answer