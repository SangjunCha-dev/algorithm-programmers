def solution(skill, skill_trees):
    ans = 0
    for s in skill_trees:
        n = s.find(skill[0])
        pos = True
        for i in skill[1:]:
            if (0 <= s.find(i) < n) or (n == -1 and i in s):
                pos = False
                break 
            n = s.find(i)
        if pos: 
            ans += 1
    return ans