def solution(s):
    return ' '.join([text[0].upper() + text[1:].lower() if text else '' for text in s.split(' ')])