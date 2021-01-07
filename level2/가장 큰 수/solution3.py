def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True)
    return ''.join(numbers) if numbers[0] != '0' else '0'