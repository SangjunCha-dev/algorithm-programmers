import re
p1 = re.compile(r'[^a-z0-9_.-]')
p2 = re.compile(r'[.]+')
p3 = re.compile(r'^[.]|[.]$')
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(p1, '', new_id)
    new_id = re.sub(p2, '.', new_id)

    while True:
        new_id = re.sub(p3, '', new_id)
        if not new_id:
            new_id = 'a'
        elif 15 < len(new_id):
            new_id = new_id[:15]
        elif len(new_id) < 3:
            new_id += new_id[-1]
        else:
            break
    return new_id