def find_point(place):
    for h1 in range(5):
        for w1 in range(5):
            point = place[h1][w1]
            if point != 'P':
                continue

            min_w = w1-2 if 0 < w1-2 else 0
            max_w = w1+2 if w1+2 < 5 else 4
            max_h = h1+2 if h1+2 < 5 else 4

            for w2 in range(w1+1,max_w+1):
                point2 = place[h1][w2]
                if point2 == 'X':
                    break
                elif point2 == 'P':
                    return 0
                elif point2 == 'O':
                    h2 = h1+1 if h1+1 < max_h else max_h
                    distance = abs(h1-h2)+abs(w1-w2)
                    if (place[h2][w2] == 'P') and (distance <=2):
                        return 0

            for w2 in range(w1-1,min_w-1,-1):
                point2 = place[h1][w2]
                if point2 == 'X':
                    break
                elif point2 == 'P':
                    return 0
                elif point2 == 'O':
                    h2 = h1+1 if h1+1 < max_h else max_h
                    distance = abs(h1-(h2))+abs(w1-w2)
                    if (place[h2][w2] == 'P') and (distance <=2):
                        return 0

            for h2 in range(h1+1,max_h+1):
                point2 = place[h2][w1]
                if point2 == 'X':
                    break
                elif point2 == 'P':
                    return 0
                elif point2 == 'O':
                    w2 = w1-1 if 0 < w1-1 else min_w
                    distance = abs(h1-h2)+abs(w1-w2)
                    if (place[h2][w2] == 'P') and (distance <=2):
                        return 0
                    w2 = w1+1 if w1+1 < max_w else max_w
                    distance = abs(h1-h2)+abs(w1-w2)
                    if (place[h2][w2] == 'P') and (distance <=2):
                        return 0
    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(find_point(place))

    return answer