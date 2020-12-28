def solution(name):
    move_cnt = 0
    text_len = len(name)
    alphabet = ['A',\
                'B','C','D','E','F','G','H','I','J','K','L','M','N',\
                'Z','Y','X','W','V','U','T','S','R','Q','P','O']
    
    tf_list = [False] * text_len
    for i in range(text_len):
        index = alphabet.index(name[i])
        move_cnt = move_cnt+index if index <= 13 else move_cnt+(index-13)
        if index: tf_list[i] = True
    
    tf_list[0] = False
    i = 0
    while tf_list.count(True):
        distance_r = 0
        distance_l = 0

        for j in range(1, text_len):
            distance_r += 1
            if tf_list[(i+j)%text_len]:
                break
        
        for j in range(1, text_len):
            distance_l += 1
            if tf_list[(i-j)%text_len]:
                break

        i = (i-1)%text_len if distance_l < distance_r else (i+1)%text_len
        tf_list[i] = False
        
        move_cnt += 1

    return move_cnt