def solution(s):
    return ' '.join([text.capitalize() if text else '' for text in s.split(' ')])