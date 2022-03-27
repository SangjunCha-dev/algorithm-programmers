def solution(n, computers):
    return find_node(computers)

def find_node(computers):
    for i, computer1 in enumerate(computers):
        for j in range(i+1, len(computers)):
            for k, l in zip(computer1, computers[j]):

                # and 연산으로 같은 네트워크 인지 검증
                if k and l:
                    temp_node = []
                    for val1, val2 in zip(computers[j], computer1):
                        # 같은 네트워크 이면 or 연산으로 네트워크 확장
                        temp_node.append(val1 or val2)
                    computers[i] = temp_node

                    # 병합된 연결정보 삭제
                    del computers[j]

                    # 연결정보가 갱신되었으므로 처음부터 다시 연결정보 탐색
                    return find_node(computers)
    return len(computers)