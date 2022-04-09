def solution(phone_book):
    phone_book.sort()
    book = {}
    for phone in phone_book:
        for i in range(len(phone)):
            if phone[:i+1] in book:
                return False
        else:
            book[phone] = True
    return True