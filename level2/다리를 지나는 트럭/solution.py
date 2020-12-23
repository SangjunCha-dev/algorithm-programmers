def solution(bridge_length, weight, truck_weights):
    answer = 0
    bredge_list = []
    while bredge_list or truck_weights:
        # 트럭이 다리를 건넜을때
        if bredge_list:
            if bridge_length < bredge_list[0][1]:
                weight += bredge_list[0][0]
                del bredge_list[0]

        cnt = 1  # 한번에 이동할 거리
        # 트럭 진입
        if truck_weights:
            truck = truck_weights[0]
            # 진입할 트럭의 무게를 다리가 버틸수 있을때
            if 0 <= weight-truck:
                weight -= truck
                bredge_list.append([truck, 1])
                del truck_weights[0]
            else:
                # 트럭 추가 진입이 불가능할때 한번에 계산
                for i in range(1, bridge_length+1):
                    if bridge_length < (bredge_list[0][1] + i):
                        cnt = i
                        break

        # 트럭이 다리를 지나간 정도
        for i in range(len(bredge_list)):
            bredge_list[i][1] += cnt
        answer += cnt
    return answer