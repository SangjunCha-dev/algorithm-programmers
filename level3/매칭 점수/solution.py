import re

body_compile = re.compile('<body>(.*?)<\/body>', re.I|re.S)
strgig_compile = re.compile('[^a-zA-Z]')
contents_link_compile = re.compile('<meta property="og:url" content="https://(.*?)"/>', re.I|re.S)
href_link_compile = re.compile('<a href="https://(.*?)">', re.I|re.S)
href_compile = re.compile('(<a)(.*?)(<\/a>)', re.I|re.S)

def solution(word, pages):
    find_pattern = re.compile(f'\W{word.lower()}\W')
    data = {}

    for i, page in enumerate(pages):
        # 기본 점수 계산(단어 매칭 개수)
        body_data = re.findall(body_compile, page)[0]
        body_data = re.sub(href_compile, '', body_data)
        body_data = re.sub(strgig_compile, '  ', body_data)  # 공백 2개로 변환
        base_score = len(re.findall(find_pattern, body_data.lower()))

        # 페이지 링크
        contents_link = contents_link_compile.findall(page)[0]

        # 외부 링크 수
        links = href_link_compile.findall(page)

        data[contents_link] = {
            'index': i,
            'total_score': 0,
            'base_score': base_score,
            'link_score': 0,
            'links': links,
            'links_len': len(links),
        }

    # 링크 점수(기본점수 ÷ 외부 링크 수의 총합)
    for b_link, page in data.items():
        for e_link in page['links']:
            if e_link in data:
                data[e_link]['link_score'] += data[b_link]['base_score'] / data[b_link]['links_len']

    # 최고 점수 페이지 index 찾기
    max_index, max_score = 0, 0
    for page in data.values():
        total_score = page['base_score'] + page['link_score']
        if max_score < total_score:
            max_index = page['index']
            max_score = total_score

    return max_index