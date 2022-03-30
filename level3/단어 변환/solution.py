def word_conversion(begin, target, nodes, stack):
    count = 0
    stack.append(begin)

    # target과 동일한 경우
    if target == begin:
        return len(stack)-1

    path_count = []
    for i in range(len(target)):
        w = f"{begin[:i]}{begin[i+1:]}"

        if w in nodes[i]:
            for word in nodes[i][w]:
                if word not in stack:
                    conversion_result = word_conversion(word, target, nodes, stack)
                    if conversion_result != 0:
                        path_count.append(conversion_result)
                    stack.pop()

    if path_count:
        count = min(path_count)

    return count

def solution(begin, target, words):
    answer = 0
    length = len(target)
    nodes = {i: {} for i in range(length)}

    # 연결관계 정립
    for word in words:
        for i in range(length):
            w = f"{word[:i]}{word[i+1:]}"
            if w in nodes[i]:
                nodes[i][w].append(word)
            else:
                nodes[i][w] = [word]
    
    # DFS -> 재귀
    stack = []
    answer = word_conversion(begin, target, nodes, stack)

    return answer