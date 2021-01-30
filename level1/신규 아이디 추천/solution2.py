import re
p1 = re.compile(r'[^a-z0-9_.-]')
p2 = re.compile(r'[.]+')
p3 = re.compile(r'^[.]|[.]$')
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(p1, '', new_id)
    new_id = re.sub(p2, '.', new_id)
    new_id = re.sub(p3, '', new_id)
    new_id = new_id if new_id else 'a'
    new_id = new_id[:15] if 15 < len(new_id) else new_id
    new_id = re.sub(p3, '', new_id)
    new_id = new_id if 2 < len(new_id) else (new_id + new_id[-1] if 1 < len(new_id) else new_id*3)
    return new_id