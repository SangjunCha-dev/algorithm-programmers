def solution(skill,skill_tree):
    ans = 0
    for i in skill_tree:
        res = ''
        for z in i:
            if z in skill:
                res += z
        if res == skill[0:len(res)]:
            ans += 1
    return ans