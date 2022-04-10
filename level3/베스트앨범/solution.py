import heapq

def solution(genres, plays):
    answer = []

    album = {}
    for i, genre, play in zip(range(len(genres)), genres, plays):
        if genre not in album:
            album[genre] = [-play, []]
        else:
            # 장르별 재생횟수 합산
            album[genre][0] -= play
        # 곡 고유번호 최대힙에 저장
        heapq.heappush(album[genre][1], [-play, i])

    sort_album = []
    for genre in album:
        # 가장 많이 재생된 첫번째 곡 선별
        play1 = heapq.heappop(album[genre][1])

        # 1곡만 수록된 경우
        if not album[genre][1]:
            sort_album.append(play1)
            continue    

        # 가장 많이 재생된 두번째 곡 선별
        play2 = heapq.heappop(album[genre][1])

        # 장르별 재생횟수 및 곡 고유번호 합산
        sort_album.append([album[genre][0], play1[1], play2[1]])

    # 장르별 가장 많이 재생된 횟수 내림차순 정렬
    sort_album.sort(key=lambda x: x[0])

    for genre_album in sort_album:
        answer.extend(genre_album[1:])

    return answer