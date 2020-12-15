def solution(array, commands):
    answer = []
    
    for command in commands:
        array_ext = array[command[0]-1:command[1]]
        array_ext.sort()
        answer.append(array_ext[command[2]-1])
    
    return answer