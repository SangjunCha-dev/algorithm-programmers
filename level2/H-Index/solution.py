def solution(citations):
    citations.sort(reverse=True)

    h_index = 0
    list_len = len(citations)
    for i in range(list_len):
        if citations[i] < h_index+1:
            if h_index < list_len-(i+1):
                h_index -= 1
            else:
                break
        else:
            h_index += 1
    return h_index