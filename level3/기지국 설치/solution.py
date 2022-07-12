import math


def solution(n, stations, w):
    stations.sort()
    chack_point = 1
    cover_area = w*2 + 1
    setup_stations = 0

    # 전달되지 않은 구역의 범위 구하기
    for station in stations:
        left_cover, right_cover = station - w, station + w
        if chack_point < left_cover:
            blank_area = left_cover - chack_point
            setup_stations += math.ceil(blank_area/cover_area)
        chack_point = right_cover + 1

    # 마지막 스테이션 설치 이후 N까지 공백구역 처리
    if chack_point <= n:
        blank_area = n - (chack_point - 1)
        setup_stations += math.ceil(blank_area/cover_area)

    return setup_stations


if __name__ == '__main__':

    n = 11
    stations = [4, 11]
    w = 1

    result = solution(n, stations, w)
    answer = 3

    print(f"result = {result} / answer = {answer} / {result==answer}")
