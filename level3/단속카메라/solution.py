def solution(routes):
    # 진입 지점과 진출 위치 정렬   
    sort_routes = sorted(routes, key=lambda x: x[1])

    # 나갈 지점 설정
    exit_point = sort_routes[0][1]
    answer = 1

    for route in sort_routes[1:]:
        # 저장된 진출지점보다 현재 진입지점이 뒤에 위치할 경우 새로운 단속 카메라 설치
        if exit_point < route[0]:
            answer += 1
            exit_point = route[1]
        # 현재 진출지점이 저장된 진출지점보다 앞에 위치할 경우 저장된 진출지점을 재설정
        elif route[1] < exit_point:
            exit_point = route[1]

    return answer