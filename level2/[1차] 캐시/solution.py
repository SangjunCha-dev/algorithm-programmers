from collections import deque

def index_cache(cacheSize, cities):
    total_time = 0

    city_cache = []

    for _ in range(len(cities)):
        city = cities.popleft().lower()
        
        # 캐시목록에 해당 정보가 있을 경우
        if city in city_cache:
            # 해당 정보를 가장 최근에 호출된 위치로 이동
            city_cache.remove(city)
            city_cache.append(city)
            total_time += 1
        else:
            # 캐시가 가득찬 경우 오래된 정보 삭제
            if city_cache and (cacheSize <= len(city_cache)):
                city_cache.pop(0)
            city_cache.append(city)
            total_time += 5

    return total_time

def solution(cacheSize, cities):
    answer = 0
    cities = deque(cities)

    # 캐시가 설정된 경우
    if cacheSize:
        answer = index_cache(cacheSize, cities)
    else:
        answer = len(cities) * 5

    return answer