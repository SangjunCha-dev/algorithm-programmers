def find_block(m, n, board, is_equal_list):
    '''
    같은 블럭 여부 확인
    '''
    for h in range(m-1):
        for w in range(n-1):
            if (board[h][w] != " ") and (board[h][w] == board[h+1][w] == board[h][w+1] == board[h+1][w+1]):
                for i in range(2):
                    for j in range(2):
                        is_equal_list[h+i][w+j] = True

def remove_block_and_counting(m, n, board, is_equal_list):
    '''
    같은 블럭 제거 및 개수세기
    '''
    remove_block_count = 0

    for h in range(m):
        temp_str = ""
        for w in range(n):
            if is_equal_list[h][w]:
                temp_str += " "
                remove_block_count += 1
            else:
                temp_str += board[h][w]
        board[h] = temp_str

    return remove_block_count

def move_bottom_block(m, n, board):
    '''
    블럭 위치 하단으로 이동
    '''
    for w in range(n):
        exist_layer = m-1
        temp_str = ""

        for h in range(m-1, -1, -1):
            compare_value = board[h][w]
            
            if compare_value == " ":
                continue

            temp_str = board[exist_layer][w]
            board[exist_layer] = board[exist_layer][:w] + compare_value + board[exist_layer][w+1:]
            board[h] = board[h][:w] + temp_str + board[h][w+1:]
            exist_layer -= 1

def solution(m, n, board):
    answer = 0

    while True:
        remove_block_count = 0
        is_equal_list = [[False for _ in range(n)] for _ in range(m)]

        # 같은 블럭 여부 확인
        find_block(m, n, board, is_equal_list)

        # 같은 블럭 제거 및 개수세기
        remove_block_count = remove_block_and_counting(m, n, board, is_equal_list)

        # 블럭 위치 하단으로 이동
        move_bottom_block(m, n, board)

        answer += remove_block_count
        if remove_block_count == 0:
            break

    return answer