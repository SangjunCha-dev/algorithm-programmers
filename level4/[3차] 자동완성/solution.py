def convert_words(words):
    dict_words = {}

    for word in words:
        dict_word = dict_words
        for w in word:
            if w in dict_word:
                dict_word[w]['count'] += 1
            else:
                dict_word[w] = {'count': 1}
            dict_word = dict_word[w]

    return dict_words

def count_word(dict_words):
    count = 0
    if 'count' in dict_words:
        count = dict_words['count']
        del dict_words['count']
        if count == 1:
            return count

    for words in dict_words.values():
        count += count_word(words)

    return count

def solution(words):
    dict_words = convert_words(words)
    answer = count_word(dict_words)
    return answer