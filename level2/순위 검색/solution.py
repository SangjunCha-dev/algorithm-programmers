from copy import deepcopy

def binary_search(data: list, target: int):
    s_idx = 0
    e_idx = len(data)-1
    mid = 0
    if data:
        if data[-1] < target:
            mid = len(data)
        elif data[0] < target:
            while s_idx <= e_idx:
                mid = (s_idx+e_idx)//2
                
                if target < data[mid]:
                    e_idx = mid
                elif data[mid] < target:
                    if e_idx - s_idx == 1:
                        mid = e_idx
                        break
                    elif e_idx == s_idx:
                        mid = e_idx + 1
                        break
                    else:
                        s_idx = mid
                else:
                    e_idx -= 1
    return mid

def dict_count(q_val: list, i_val: list):
    cnt = 0
    key = q_val[0]
    if key == '-':
        for k in i_val:
            cnt += dict_count(q_val=q_val[1:], i_val=i_val[k])
    elif 1 < len(q_val):
        cnt = dict_count(q_val=q_val[1:], i_val=i_val[key])
    elif i_val:
        cnt = len(i_val) - binary_search(data=i_val, target=key)

    return cnt

def solution(info, query):
    answer = []

    soul_food = {'chicken': [], 'pizza': []}
    career = {'junior': deepcopy(soul_food), 'senior': deepcopy(soul_food)}
    job_group = {'backend': deepcopy(career), 'frontend': deepcopy(career)}
    i_info = {'cpp': deepcopy(job_group), 'java': deepcopy(job_group), 'python': deepcopy(job_group)}

    for val in info:
        val = val.split(' ')
        data = i_info[val[0]][val[1]][val[2]][val[3]]
        t_val = int(val[4])
        data.insert(binary_search(data=data, target=t_val), t_val)

    for val in query:
        val = val.split(' and ')
        val[-1], score = val[-1].split(' ')
        val.append(int(score))
        answer.append(dict_count(q_val=val, i_val=i_info))
    
    return answer